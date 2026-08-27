from __future__ import annotations

import os
import shutil
from dataclasses import asdict
from pathlib import Path

from .models import Capability


DEFAULT_CAPABILITIES = (
    "read_files",
    "write_files",
    "shell",
    "git",
    "network",
)


def discover_capabilities(root: str | Path = ".") -> list[Capability]:
    """Discover conservative local capabilities without claiming remote/tool access."""
    root = Path(root)
    result: list[Capability] = []
    result.append(Capability("read_files", root.exists(), "project root exists"))
    result.append(Capability("write_files", os.access(root, os.W_OK), "project root writable"))
    result.append(Capability("shell", True, "local Python process is executable"))
    result.append(Capability("git", shutil.which("git") is not None, "git executable discovered"))
    result.append(Capability("network", False, "not inferred; configure explicitly"))
    return result


def capabilities_dict(root: str | Path = ".") -> dict[str, dict]:
    return {item.name: asdict(item) for item in discover_capabilities(root)}
