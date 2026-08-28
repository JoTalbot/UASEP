from __future__ import annotations

from collections.abc import Callable, Iterable
from pathlib import Path

from .graph import TaskGraph
from .lock import project_lock
from .models import CycleResult, ProjectState, Task, TaskStatus
from .retry_policy import RetryPolicy
from .safety import ApprovalGate, ApprovalRequest
from .store import Store
from .verify import VerificationEngine

ExecuteFn = Callable[[Task], bool]
ChecksFn = Callable[[Task], Iterable[tuple[str, Callable[[], bool]]]]


class Supervisor:
    """Canonical orchestration boundary: one serialized cycle implementation."""

    def __init__(self, root: str | Path, *, execute: ExecuteFn | None = None,
                 checks: ChecksFn | None = None, approval: ApprovalGate | None = None,
                 max_failures: int = 3) -> None:
        self.root = Path(root)
        self.store = Store(root)
        self.verifier = VerificationEngine()
        self.approval = approval or ApprovalGate()
        self.retry_policy = RetryPolicy(max_failures)
        self._execute = execute or (lambda _task: True)
        self._checks = checks or (
            lambda task: [(c, lambda: True) for c in task.acceptance_criteria]
            or [("noop", lambda: True)]
        )

    def run_once(self, project_id: str) -> CycleResult:
        with project_lock(self.root):
            return self._run_once(project_id)

    def _run_once(self, project_id: str) -> CycleResult:
        state, graph = self.store.load_bundle(project_id)
        state.project_id = project_id or state.project_id
        try:
            graph.validate()
        except ValueError as exc:
            state.phase = "blocked"
            state.add_blocker(str(exc))
            self.store.save_state(state)
            return CycleResult(None, "BLOCKED", state.iteration, str(exc))

        ready = graph.ready()
        if not ready:
            if not graph.tasks or len(graph.succeeded()) == len(graph.tasks):
                state.phase = "complete" if graph.tasks else "maintenance"
            else:
                state.phase = "blocked"
            state.active_task = None
            self.store.save_bundle(state, graph)
            self.store.checkpoint(None, state.phase)
            return CycleResult(None, state.phase.upper(), state.iteration)

        task = ready[0]
        state.iteration += 1
        state.active_task = task.id
        state.phase = "active"
        graph.apply(task.id, TaskStatus.RUNNING)
        self.store.save_bundle(state, graph)
        self.store.checkpoint(task.id, "running")

        request = ApprovalRequest(
            key=f"execute:{task.id}:{task.failure_count}",
            summary=task.objective,
            destructive=task.risk in {"high", "critical"},
            capability=task.required_capabilities[0] if task.required_capabilities else None,
        )
        if not self.approval.allow(task, request):
            graph.apply(task.id, TaskStatus.BLOCKED)
            state.phase = "blocked"
            state.add_blocker(f"{task.id}: approval required")
            state.active_task = None
            self.store.save_bundle(state, graph)
            self.store.checkpoint(task.id, "blocked")
            return CycleResult(task.id, "BLOCKED", state.iteration, "approval required")

        try:
            ok = bool(self._execute(task))
        except Exception as exc:  # noqa: BLE001
            return self._failed(state, graph, task, f"{type(exc).__name__}: {exc}")

        if not ok:
            return self._failed(state, graph, task, "executor reported failure")

        verification = self.verifier.verify(self._checks(task))
        eid = self.store.record_evidence(task.id, "verification", verification.status, "; ".join(verification.details))
        if verification.status != "VERIFIED":
            return self._failed(state, graph, task, "; ".join(verification.details), evidence_id=eid)

        graph.apply(task.id, TaskStatus.VERIFIED, eid)
        if task.id not in state.completed_tasks:
            state.completed_tasks.append(task.id)
        state.active_task = None
        state.last_verified = task.id
        state.last_error = None
        state.phase = "complete" if not graph.ready() and len(graph.succeeded()) == len(graph.tasks) else "active"
        self.store.record_evidence(task.id, "completion", "VERIFIED", "acceptance checks passed")
        self.store.checkpoint(task.id, "verified")
        self.store.save_bundle(state, graph)
        return CycleResult(task.id, "VERIFIED", state.iteration)

    def _failed(self, state: ProjectState, graph: TaskGraph, task: Task, detail: str,
                evidence_id: str | None = None) -> CycleResult:
        eid = evidence_id or self.store.record_evidence(task.id, "execution", "FAILED", detail)
        graph.apply(task.id, TaskStatus.FAILED, eid)
        previous = task.retry_strategy
        next_strategy = f"retry-{task.failure_count + 1}"
        decision = self.retry_policy.decide(task.id, task.failure_count, next_strategy, previous)
        state.last_error = detail
        if decision.retry:
            task.retry_strategy = next_strategy
            task.status = TaskStatus.RETRYABLE
            state.phase = "active"
            reason = f"retry scheduled: {task.retry_strategy}"
        else:
            task.status = TaskStatus.BLOCKED
            state.add_blocker(f"{task.id}: {decision.reason}")
            state.phase = "active" if any(t.id != task.id for t in graph.ready()) else "blocked"
            reason = decision.reason
        state.active_task = None
        self.store.checkpoint(task.id, task.status.value)
        self.store.save_bundle(state, graph)
        return CycleResult(task.id, "FAILED", state.iteration, f"{detail}; {reason}")

    def run_until_idle(self, project_id: str, max_cycles: int = 100) -> ProjectState:
        state = self.store.load_state(project_id)
        for _ in range(max_cycles):
            result = self.run_once(project_id)
            state = self.store.load_state(project_id)
            if result.status in {"COMPLETE", "BLOCKED", "MAINTENANCE"}:
                return state
            if state.phase in {"complete", "blocked", "maintenance", "handoff"}:
                return state
        return state
