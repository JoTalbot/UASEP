from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from .evidence_store import Evidence, EvidenceStore
from .state import StateStore
from .task_graph import TaskGraph, TaskNode
from .verification import VerificationEngine


@dataclass(frozen=True, slots=True)
class CycleResult:
    task_id: str | None
    status: str
    iterations: int


class AutonomousLoop:
    """One bounded, resumable engineering cycle. Host code supplies execution and checks."""

    def __init__(self, root: Path, project_id: str, graph: TaskGraph) -> None:
        self.root = root
        self.project_id = project_id
        self.graph = graph
        self.state_store = StateStore(root)
        self.evidence = EvidenceStore(root / ".uasep" / "evidence" / "runtime.json")
        self.verifier = VerificationEngine()

    def run_once(self, execute: Callable[[TaskNode], bool], checks: Callable[[TaskNode], Iterable[tuple[str, Callable[[], bool]]]]) -> CycleResult:
        state = self.state_store.load(self.project_id)
        ready = self.graph.ready()
        if not ready:
            state.phase = "complete" if not self.graph.tasks else "blocked"
            self.state_store.save(state)
            return CycleResult(None, state.phase.upper(), state.iteration)

        task = ready[0]
        state.current_task = task.id
        state.phase = "executing"
        state.iteration += 1
        self.state_store.save(state)

        if not execute(task):
            state.phase = "blocked"
            self.evidence.record(Evidence("execution", task.id, "FAILED", "executor returned failure"))
            self.state_store.save(state)
            return CycleResult(task.id, "FAILED", state.iteration)

        verification = self.verifier.verify(checks(task))
        self.evidence.record(Evidence("verification", task.id, verification.status, "; ".join(verification.details)))
        if verification.status != "VERIFIED":
            state.phase = "blocked"
            self.state_store.save(state)
            return CycleResult(task.id, "FAILED", state.iteration)

        self.graph.mark_done(task.id)
        state.completed_tasks.add(task.id)
        state.current_task = None
        state.phase = "complete" if not self.graph.ready() else "active"
        self.state_store.save(state)
        self.evidence.record(Evidence("completion", task.id, "VERIFIED", "acceptance checks passed"))
        return CycleResult(task.id, "VERIFIED", state.iteration)
