from __future__ import annotations

import argparse
from pathlib import Path

from .capabilities import CapabilityRegistry
from .discovery import discover
from .project_bootstrap import bootstrap_project
from .conformance import check_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="uasep")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("capabilities")
    sub.add_parser("bootstrap")
    sub.add_parser("check")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path.cwd()
    if args.command == "capabilities":
        result = discover(root)
        for name in sorted(result):
            print(name)
        return 0
    if args.command == "bootstrap":
        created = bootstrap_project(root)
        for path in created:
            print(path)
        return 0
    results = check_project(root)
    for result in results:
        print(f"{'PASS' if result.passed else 'FAIL'} {result.name}")
    return 0 if all(item.passed for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
