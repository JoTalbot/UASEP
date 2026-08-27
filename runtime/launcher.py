from __future__ import annotations

import argparse
from pathlib import Path

from .project_bootstrap import bootstrap_project
from .aios2_adapter import AIOS2Adapter
from .capabilities import CapabilityRegistry


def launch(root: Path) -> dict[str, object]:
    """Initialize the project-local UASEP boundary without touching project artifacts."""
    root = root.resolve()
    created = bootstrap_project(root, root.name)
    adapter = AIOS2Adapter(root, CapabilityRegistry())
    return {
        "project": root.name,
        "root": str(root),
        "created": [str(path.relative_to(root)) for path in created],
        "capabilities": adapter.capability_names(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="uasep-launch")
    parser.add_argument("project", nargs="?", default=".")
    args = parser.parse_args()
    result = launch(Path(args.project))
    print(f"UASEP READY: {result['project']}")
    for item in result["created"]:
        print(f"CREATED {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
