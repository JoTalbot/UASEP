from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .anti_loop import StagnationDetector
from .evidence_store import Evidence, EvidenceStore
from .task_graph import TaskGraph, TaskNode


@dataclass(frozen=True, slots=True)
class SupervisorResult:
    completed: list[str]
    blocked: list[str]
    iterations: int


class Supervisor:
    """Bounded reference supervisor; execution is supplied by the host adapter."""

    def __init__(self, root: Path, graph: TaskGraph) -> None:
        self.root = root
        self.graph = graph
        self.evidence = EvidenceStore(root / ".uasep" / "evidence" / "runtime.json")
        self.stagnation = StagnationDetector()

    def run(self, executor: Callable[[TaskNode], bool], max_iterations: int = 100) -> SupervisorResult:
        completed: list[str] = []
        blocked: list[str] = []
        iterations = 0
        while iterations < max_iterations:
            ready = self.graph.ready()
            if not ready:
                break
            task = ready[0]
            iterations += 1
            success = bool(executor(task))
            if success:
                self.graph.mark_done(task.id)
                completed.append(task.id)
                self.evidence.record(Evidence("task", task.id, "VERIFIED", "executor returned success"))
                self.stagnation.observe(task.id, True)
            else:
                blocked.append(task.id)
                self.evidence.record(Evidence("task", task.id, "FAILED", "executor returned failure"))
                if self.stagnation.observe(task.id, False):
                    break
        return SupervisorResult(completed, blocked, iterations)
