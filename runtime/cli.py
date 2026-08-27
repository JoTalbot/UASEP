from __future__ import annotations

import argparse
import json
from pathlib import Path

from .bootstrap import bootstrap_project
from .conformance import check_project
from .discovery import capabilities_dict
from .state import StateStore


def main() -> int:
    parser = argparse.ArgumentParser(prog="uasep")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("bootstrap", help="create missing project-local UASEP state")
    sub.add_parser("capabilities", help="discover conservative local capabilities")
    sub.add_parser("check", help="check project conformance")
    state = sub.add_parser("state", help="show persisted project state")
    state.add_argument("--project", default=Path.cwd().name)
    args = parser.parse_args()

    if args.command == "bootstrap":
        created = bootstrap_project()
        for path in created:
            print(path)
        return 0
    if args.command == "capabilities":
        print(json.dumps(capabilities_dict(), indent=2, sort_keys=True))
        return 0
    if args.command == "check":
        results = check_project(Path.cwd())
        for result in results:
            print(f"{'PASS' if result.passed else 'FAIL'} {result.name}")
        return 0 if all(result.passed for result in results) else 1
    if args.command == "state":
        print(json.dumps(StateStore(".").load(args.project).to_dict(), indent=2, sort_keys=True))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
