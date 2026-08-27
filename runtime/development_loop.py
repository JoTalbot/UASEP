from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from .autonomous_loop import AutonomousLoop, CycleResult
from .project_bootstrap import bootstrap_project
from .task_graph import TaskGraph, TaskNode


@dataclass(frozen=True, slots=True)
class DevelopmentResult:
    status: str
    cycles: int
    completed: tuple[str, ...]


class DevelopmentLoop:
    """Bounded project-level loop. Planning is supplied by the host, execution is verified."""

    def __init__(self, root: Path, project_id: str) -> None:
        self.root = root
        self.project_id = project_id

    def run(
        self,
        tasks: Iterable[TaskNode],
        execute: Callable[[TaskNode], bool],
        checks: Callable[[TaskNode], Iterable[tuple[str, Callable[[], bool]]]],
        max_cycles: int = 100,
    ) -> DevelopmentResult:
        bootstrap_project(self.root, self.project_id)
        graph = TaskGraph(list(tasks))
        loop = AutonomousLoop(self.root, self.project_id, graph)
        completed: list[str] = []
        for _ in range(max_cycles):
            result: CycleResult = loop.run_once(execute, checks)
            if result.status == "VERIFIED":
                completed.append(result.task_id or "")
                continue
            if result.status in {"FAILED", "BLOCKED", "COMPLETE"}:
                if result.status == "COMPLETE":
                    return DevelopmentResult("COMPLETE", result.iterations, tuple(completed))
                return DevelopmentResult(result.status, result.iterations, tuple(completed))
            return DevelopmentResult(result.status, result.iterations, tuple(completed))
        return DevelopmentResult("MAX_CYCLES", max_cycles, tuple(completed))
