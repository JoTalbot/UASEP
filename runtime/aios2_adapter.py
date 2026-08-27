from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .capabilities import CapabilityRegistry
from .project_bootstrap import bootstrap_project


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
        }

    def bootstrap(self) -> list[Path]:
        return bootstrap_project(self.root, self.root.name)

    def capability_names(self) -> list[str]:
        return sorted(self.capabilities.available())
