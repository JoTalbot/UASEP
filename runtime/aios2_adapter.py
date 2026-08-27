from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .capabilities import CapabilityRegistry
from .project_bootstrap import bootstrap_project


@dataclass(slots=True)
class AIOS2Adapter:
    """Thin integration boundary for embedding UASEP into AIOS2.

    It deliberately does not assume that AIOS2 exposes shell, network, or GitHub
    access. The host registers only capabilities it can actually provide.
    """

    root: Path
    capabilities: CapabilityRegistry

    def bootstrap(self) -> list[Path]:
        return bootstrap_project(self.root, self.root.name)

    def capability_names(self) -> list[str]:
        return sorted(self.capabilities.available())
