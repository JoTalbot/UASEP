"""Deprecated: use runtime.supervisor.Supervisor.

This module forwards to Supervisor so old imports do not define a second
orchestration semantics on branch `new`.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from pathlib import Path

from .graph import TaskGraph
from .models import CycleResult, Task
from .supervisor import Supervisor


class AutonomousLoop:
    """Adapter around Supervisor — do not extend; migrate callers."""

    def __init__(self, root: Path, project_id: str, graph: TaskGraph) -> None:
        self.root = Path(root)
        self.project_id = project_id
        self.graph = graph
        from .store import Store

        Store(self.root).save_graph(graph)

    def run_once(
        self,
        execute: Callable[[Task], bool],
        checks: Callable[[Task], Iterable[tuple[str, Callable[[], bool]]]],
        strategy: str = "default",
        approval: Callable | None = None,
    ) -> CycleResult:
        del strategy, approval  # legacy knobs folded into Supervisor defaults
        sup = Supervisor(self.root, execute=execute, checks=checks)
        return sup.run_once(self.project_id)
