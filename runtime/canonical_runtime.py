from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from .host_adapter import HostAdapter
from .models import Task
from .runner import AcceptanceProvider, RunResult, run_project


@dataclass(frozen=True, slots=True)
class CanonicalRuntime:
    """Single public runtime facade for all supported UASEP hosts."""

    root: Path
    project_id: str
    host: HostAdapter

    def run(
        self,
        tasks: list[Task],
        max_cycles: int = 100,
        *,
        acceptance: AcceptanceProvider | None = None,
    ) -> RunResult:
        """Execute through the canonical Supervisor path with explicit acceptance checks."""
        return run_project(
            self.root,
            self.project_id,
            tasks,
            max_cycles=max_cycles,
            host=self.host,
            acceptance_provider=acceptance,
        )
