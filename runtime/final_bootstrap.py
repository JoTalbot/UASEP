from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .project_bootstrap import bootstrap_project


@dataclass(frozen=True, slots=True)
class BootstrapResult:
    root: Path
    existing: bool
    manifest: Path


def bootstrap(root: Path) -> BootstrapResult:
    """Idempotent universal bootstrap for new and existing projects."""
    root = Path(root).resolve()
    existing = (root / ".uasep" / "manifest.yaml").exists()
    bootstrap_project(root)
    return BootstrapResult(root, existing, root / ".uasep" / "manifest.yaml")
