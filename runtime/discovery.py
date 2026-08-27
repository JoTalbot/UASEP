from __future__ import annotations

import os
import shutil
from dataclasses import asdict
from pathlib import Path

from .models import Capability


def discover_project_root(root: str | Path = ".") -> Path:
    """Resolve and validate the host-provided project root."""
    path = Path(root).expanduser().resolve()
    if not path.exists() or not path.is_dir():
        raise ValueError(f"project root is not a directory: {path}")
    return path


def discover_uasep(root: str | Path = ".") -> dict[str, object]:
    """Discover local UASEP state without inventing remote availability."""
    project_root = discover_project_root(root)
    state_dir = project_root / ".uasep"
    manifest = state_dir / "manifest.yaml"
    return {
        "project_root": str(project_root),
        "installed": state_dir.is_dir(),
        "state_exists": manifest.exists(),
        "manifest": str(manifest),
    }


def discover_capabilities(root: str | Path = ".") -> list[Capability]:
    """Discover conservative local capabilities and record their provenance."""
    project_root = discover_project_root(root)
    return [
        Capability("read_files", True, "project root is readable", source="filesystem"),
        Capability(
            "write_files",
            os.access(project_root, os.W_OK),
            "project root writable",
            source="filesystem",
        ),
        Capability(
            "shell",
            shutil.which("python") is not None,
            "local Python executable discovered",
            source="local-process",
        ),
        Capability(
            "git",
            shutil.which("git") is not None,
            "git executable discovered",
            source="local-process",
        ),
        Capability(
            "network",
            False,
            "not inferred; host must explicitly expose it",
            source="host-policy",
        ),
    ]


def capabilities_dict(root: str | Path = ".") -> dict[str, dict]:
    return {item.name: asdict(item) for item in discover_capabilities(root)}
