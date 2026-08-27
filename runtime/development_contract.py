from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .canonical_runtime import CanonicalRuntime
from .discovery import discover_capabilities, discover_project_root, discover_uasep
from .final_bootstrap import BootstrapResult, bootstrap
from .host_adapter import HostAdapter
from .models import Task


@dataclass(frozen=True, slots=True)
class DevelopmentContract:
    """Host-neutral autonomous development entry point."""

    root: Path
    project_id: str
    host: HostAdapter

    def discover(self) -> dict[str, object]:
        root = discover_project_root(self.root)
        return {
            "project_root": root,
            "uasep": discover_uasep(root),
            "capabilities": discover_capabilities(root),
            "host_capabilities": self.host.discover(),
        }

    def bootstrap(self) -> BootstrapResult:
        return bootstrap(self.root)

    def runtime(self) -> CanonicalRuntime:
        return CanonicalRuntime(self.root, self.project_id, self.host)

    def run(self, tasks: list[Task], max_cycles: int = 100, *, acceptance: Any = None):
        self.discover()
        self.bootstrap()
        return self.runtime().run(tasks, max_cycles=max_cycles, acceptance=acceptance)
