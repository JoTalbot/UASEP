from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .final_bootstrap import BootstrapResult, bootstrap
from .host_adapter import HostAdapter
from .models import Task
from .canonical_runtime import CanonicalRuntime


@dataclass(frozen=True, slots=True)
class DevelopmentContract:
    """Minimal host-neutral contract for autonomous project development."""

    root: Path
    project_id: str
    host: HostAdapter

    def bootstrap(self) -> BootstrapResult:
        return bootstrap(self.root)

    def runtime(self) -> CanonicalRuntime:
        return CanonicalRuntime(self.root, self.project_id, self.host)

    def run(self, tasks: list[Task], max_cycles: int = 100, *, acceptance: Any = None):
        self.bootstrap()
        return self.runtime().run(tasks, max_cycles=max_cycles, acceptance=acceptance)
