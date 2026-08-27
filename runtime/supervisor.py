from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable
from pathlib import Path

from .checkpoint_store import CheckpointStore
from .evidence_store import Evidence, EvidenceStore
from .models import ProjectState, Task
from .planner import Planner
from .state import StateStore
from .verification import VerificationEngine


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

    @classmethod
    def with_project_runtime(
        cls,
        root: Path,
        executor: Callable[[Task], bool],
        planner: Planner | None = None,
        acceptance_provider: AcceptanceProvider | None = None,
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
        )

    def _checkpoint(self, task_id: str | None, phase: str) -> None:
        if self.checkpoint_store:
            self.checkpoint_store.save(task_id, phase)

    def _evidence(self, kind: str, claim: str, status: str, detail: str = "") -> None:
        if self.evidence_store:
            self.evidence_store.record(Evidence(kind, claim, status, detail))

    def run_once(self, project_id: str, tasks: list[Task]) -> ProjectState:
        state = self.state_store.load(project_id)
        state.iteration += 1
        task = self.planner.next_task(tasks, state.completed_tasks)
        if task is None:
            state.phase = "maintenance" if not state.blockers else "blocked"
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
            state.phase = "blocked"
            state.blockers.append(f"{task.id}: {type(exc).__name__}: {exc}")
            self._evidence("execution", task.id, "FAILED", str(exc))
            self._checkpoint(task.id, "failed")
            self.state_store.save(state)
            raise

        if not success:
            state.phase = "blocked"
            state.blockers.append(f"{task.id}: executor reported failure")
            self._evidence("execution", task.id, "FAILED", "executor reported failure")
            self._checkpoint(task.id, "failed")
        else:
            verification = None
            if self.verifier and self.acceptance_provider:
                verification = self.verifier.verify(self.acceptance_provider(task))
                self._evidence("verification", task.id, verification.status, "; ".join(verification.details))
            if verification is not None and verification.status != "VERIFIED":
                state.phase = "blocked"
                state.blockers.append(f"{task.id}: acceptance verification failed")
                self._checkpoint(task.id, "verification_failed")
            else:
                state.completed_tasks.add(task.id)
                state.phase = "verified"
                state.current_task = None
                self._evidence("completion", task.id, "VERIFIED", "acceptance checks passed")
                self._checkpoint(task.id, "verified")

        self.state_store.save(state)
        return state

    def run_until_blocked(self, project_id: str, tasks: list[Task], max_cycles: int = 100) -> ProjectState:
        """Continue from persisted state until blocked, maintenance, or the cycle budget is exhausted."""
        state = self.state_store.load(project_id)
        for _ in range(max_cycles):
            state = self.run_once(project_id, tasks)
            if state.phase in {"blocked", "maintenance"}:
                return state
        # Preserve the last meaningful phase. A cycle budget is a scheduling limit,
        # not a maintenance state and must not erase a successful checkpoint.
        return state
