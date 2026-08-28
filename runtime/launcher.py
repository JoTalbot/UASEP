from __future__ import annotations

import argparse
from pathlib import Path

from .discovery import capabilities_dict
from .project_bootstrap import bootstrap_project


def launch(root: Path) -> dict[str, object]:
    """Bootstrap project-local UASEP without fabricating host capabilities."""
    root = root.resolve()
    created = bootstrap_project(root, root.name)
    return {
        "project": root.name,
        "root": str(root),
        "created": [str(path.relative_to(root)) for path in created],
        "capabilities": capabilities_dict(root),
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
