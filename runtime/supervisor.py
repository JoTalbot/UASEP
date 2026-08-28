from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable
from pathlib import Path

from .checkpoint_store import CheckpointStore
from .evidence_store import Evidence, EvidenceStore
from .models import ProjectState, Task, TaskStatus
from .planner import Planner
from .state import StateStore
from .verification import VerificationEngine
from .multi_agent import MultiAgentCoordinator


AcceptanceProvider = Callable[[Task], Iterable[tuple[str, Callable[[], bool]]]]


@dataclass
class Supervisor:
    """Canonical persistent orchestration boundary for CLI, sandbox, or tool-connected hosts."""

    state_store: StateStore
    planner: Planner
    executor: Callable[[Task], bool]
    verifier: VerificationEngine | None = None
    acceptance_provider: AcceptanceProvider | None = None
    evidence_store: EvidenceStore | None = None
    checkpoint_store: CheckpointStore | None = None
    multi_agent: MultiAgentCoordinator | None = None
    max_failures: int = 3

    @classmethod
    def with_project_runtime(
        cls,
        root: Path,
        executor: Callable[[Task], bool],
        planner: Planner | None = None,
        acceptance_provider: AcceptanceProvider | None = None,
        max_failures: int = 3,
        multi_agent: MultiAgentCoordinator | None = None,
    ) -> "Supervisor":
        base = root / ".uasep"
        return cls(
            StateStore(root),
            planner or Planner(),
            executor,
            verifier=VerificationEngine(),
            acceptance_provider=acceptance_provider,
            evidence_store=EvidenceStore(base / "evidence" / "runtime.json"),
            checkpoint_store=CheckpointStore(base / "checkpoints" / "journal.json"),
            multi_agent=multi_agent,
            max_failures=max_failures,
        )

    def _checkpoint(self, task_id: str | None, phase: str) -> None:
        if self.checkpoint_store:
            self.checkpoint_store.save(task_id, phase)

    def _evidence(self, kind: str, claim: str, status: str, detail: str = "") -> None:
        if self.evidence_store:
            self.evidence_store.record(Evidence(kind, claim, status, detail))

    def _restore_task_failures(self, state: ProjectState, tasks: list[Task]) -> None:
        """Apply persisted per-task failure counts after a cold process start."""
        for task in tasks:
            if task.id in state.task_failures:
                task.failure_count = max(task.failure_count, state.task_failures[task.id])
                if task.failure_count >= self.max_failures and task.status != TaskStatus.DONE:
                    task.status = TaskStatus.BLOCKED
                elif task.failure_count > 0 and task.status not in {TaskStatus.DONE, TaskStatus.BLOCKED}:
                    task.status = TaskStatus.FAILED

    def _failure(self, state: ProjectState, task: Task, detail: str, phase: str = "failed") -> None:
        task.failure_count += 1
        state.task_failures[task.id] = task.failure_count
        self._evidence("execution", task.id, "FAILED", detail)
        self._checkpoint(task.id, phase)
        state.current_task = None
        if task.failure_count >= self.max_failures:
            task.status = TaskStatus.BLOCKED
            state.phase = "blocked"
            state.blockers.append(
                f"{task.id}: exceeded max failures ({self.max_failures}): {detail}"
            )
        else:
            task.status = TaskStatus.FAILED
            state.phase = "retrying"

    def run_once(self, project_id: str, tasks: list[Task]) -> ProjectState:
        state = self.state_store.load(project_id)
        self._restore_task_failures(state, tasks)
        state.iteration += 1
        task = self.planner.next_task(tasks, state.completed_tasks, self.max_failures)
        if task is None:
            all_task_ids = {item.id for item in tasks}
            exhausted = [
                item.id for item in tasks
                if item.id not in state.completed_tasks
                and item.failure_count >= self.max_failures
            ]
            if all_task_ids.issubset(state.completed_tasks):
                state.phase = "maintenance" if not state.blockers else "blocked"
            elif exhausted:
                state.phase = "blocked"
                state.blockers.append("retry budget exhausted: " + ", ".join(sorted(exhausted)))
            else:
                state.phase = "blocked"
                missing = sorted(all_task_ids - state.completed_tasks)
                if missing:
                    state.blockers.append("no runnable task: " + ", ".join(missing))
            self.state_store.save(state)
            self._checkpoint(None, state.phase)
            return state

        state.phase = "executing"
        state.current_task = task.id
        self.state_store.save(state)
        self._checkpoint(task.id, "executing")
        try:
            success = bool(self.executor(task))
        except Exception as exc:
            detail = f"{type(exc).__name__}: {exc}"
            self._failure(state, task, detail)
            self.state_store.save(state)
            return state

        if not success:
            self._failure(state, task, "executor reported failure")
        else:
            verification = None
            if self.verifier and self.acceptance_provider:
                verification = self.verifier.verify(self.acceptance_provider(task))
                self._evidence("verification", task.id, verification.status, "; ".join(verification.details))
            if verification is not None and verification.status != "VERIFIED":
                self._failure(state, task, "acceptance verification failed", "verification_failed")
            else:
                task.status = TaskStatus.DONE
                state.completed_tasks.add(task.id)
                state.phase = "verified"
                state.current_task = None
                self._evidence("completion", task.id, "VERIFIED", "acceptance checks passed")
                self._checkpoint(task.id, "verified")

        self.state_store.save(state)
        return state

    def run_parallel_once(
        self,
        project_id: str,
        tasks: list[Task],
        *,
        respect_write_sets: bool = True,
    ) -> list[tuple[str, str, bool]]:
        """Execute one deterministic batch of ready tasks through registered agents."""
        if self.multi_agent is None:
            return []
        state = self.state_store.load(project_id)
        self._restore_task_failures(state, tasks)
        ready = self.planner.ready_tasks(tasks, state.completed_tasks, self.max_failures)
        if not ready:
            state.phase = "maintenance" if state.completed_tasks == {t.id for t in tasks} else "blocked"
            state.current_task = None
            self.state_store.save(state)
            self._checkpoint(None, state.phase)
            return []

        state.phase = "executing_parallel"
        state.current_task = None
        self.state_store.save(state)
        self._checkpoint(None, "executing_parallel")
        results = self.multi_agent.run_parallel(
            ready,
            self.executor,
            respect_write_sets=respect_write_sets,
        )
        for agent_name, task_id, ok in results:
            task = next(t for t in tasks if t.id == task_id)
            if ok:
                task.status = TaskStatus.DONE
                state.completed_tasks.add(task.id)
                self._evidence("completion", task.id, "VERIFIED", f"parallel via {agent_name}")
                self._checkpoint(task.id, "verified")
            else:
                self._failure(state, task, f"parallel executor failed on {agent_name}")
        state.current_task = None
        if state.phase == "executing_parallel":
            state.phase = "verified" if results else "blocked"
        self.state_store.save(state)
        return results

    def run_until_blocked(self, project_id: str, tasks: list[Task], max_cycles: int = 100) -> ProjectState:
        """Continue from persisted state until blocked, maintenance, or the cycle budget is exhausted."""
        if max_cycles < 1:
            raise ValueError("max_cycles must be >= 1")
        state = self.state_store.load(project_id)
        self._restore_task_failures(state, tasks)
        state.blockers = [
            blocker for blocker in state.blockers if not blocker.startswith("cycle budget exhausted")
        ]
        if state.phase == "blocked" and not state.blockers:
            state.phase = "active"
            self.state_store.save(state)
        for _ in range(max_cycles):
            state = self.run_once(project_id, tasks)
            if state.phase in {"blocked", "maintenance"}:
                return state
        remaining = [item.id for item in tasks if item.id not in state.completed_tasks]
        if not remaining:
            return state
        if state.phase not in {"blocked", "maintenance"}:
            state.phase = "blocked"
            state.current_task = None
            state.blockers.append(f"cycle budget exhausted ({max_cycles})")
            self.state_store.save(state)
            self._checkpoint(None, "blocked")
        return state
