from __future__ import annotations

from pathlib import Path

from .project_bootstrap import bootstrap_project as _bootstrap_project


def bootstrap_project(root: str | Path = ".") -> list[Path]:
    """Compatibility wrapper around the canonical project bootstrap implementation."""
    return _bootstrap_project(Path(root), Path(root).resolve().name)
