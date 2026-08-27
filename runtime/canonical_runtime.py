from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from .autonomous_loop import CycleResult
from .host_adapter import HostAdapter
from .models import Task
from .runner import RunResult, run_project


@dataclass(frozen=True, slots=True)
class CanonicalRuntime:
    """Single public runtime facade; legacy loops remain compatibility implementations."""

    root: Path
    project_id: str
    host: HostAdapter

    def run(
        self,
        tasks: list[Task],
        max_cycles: int = 100,
        *,
        acceptance: Callable[[Task], Iterable[tuple[str, Callable[[], bool]]]] | None = None,
    ) -> RunResult:
        # Keep one execution authority: runner -> Supervisor -> HostExecutor.
        # Acceptance wiring is intentionally delegated to the canonical Supervisor path.
        return run_project(self.root, self.project_id, tasks, max_cycles=max_cycles, host=self.host)
