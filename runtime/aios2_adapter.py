from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .capabilities import CapabilityRegistry
from .models import Task
from .project_bootstrap import bootstrap_project
from .runner import RunResult, run_project


@dataclass(slots=True)
class AIOS2Adapter:
    """Thin host-neutral integration boundary for embedding UASEP into AIOS2."""

    root: Path
    capabilities: CapabilityRegistry

    def discover(self) -> dict[str, object]:
        return {
            "root": str(self.root.resolve()),
            "project_id": self.root.name,
            "exists": self.root.exists(),
            "capabilities": self.capability_names(),
            "protocol": "UASEP",
            "adapter": "aios2",
        }

    def bootstrap(self) -> list[Path]:
        return bootstrap_project(self.root, self.root.name)

    def capability_names(self) -> list[str]:
        return sorted(self.capabilities.available())

    def run(
        self,
        tasks: list[Task],
        *,
        max_cycles: int = 100,
        executor: Callable[[Task], bool] | None = None,
    ) -> RunResult:
        """Execute a task graph through the canonical UASEP runner."""
        return run_project(
            self.root,
            self.root.name,
            tasks,
            max_cycles=max_cycles,
            executor=executor,
        )
