from __future__ import annotations

import argparse
import json
from pathlib import Path

from .bootstrap import bootstrap_project
from .conformance import check_project
from .discovery import capabilities_dict
from .store import Store
from .supervisor import Supervisor


def main() -> int:
    parser = argparse.ArgumentParser(prog="uasep")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("bootstrap", help="create missing project-local UASEP state")
    sub.add_parser("capabilities", help="discover conservative local capabilities")
    sub.add_parser("check", help="check project conformance")

    state_p = sub.add_parser("state", help="show persisted project state")
    state_p.add_argument("--project", default=Path.cwd().name)

    sub.add_parser("graph", help="show task graph summary")

    run_p = sub.add_parser("run", help="run supervisor until idle")
    run_p.add_argument("--project", default=Path.cwd().name)
    run_p.add_argument("--max", type=int, default=100)

    resume_p = sub.add_parser("resume", help="alias for run (load disk state first)")
    resume_p.add_argument("--project", default=Path.cwd().name)
    resume_p.add_argument("--max", type=int, default=100)

    args = parser.parse_args()
    root = Path.cwd()

    if args.command == "bootstrap":
        created = bootstrap_project()
        for path in created:
            print(path)
        return 0
    if args.command == "capabilities":
        print(json.dumps(capabilities_dict(), indent=2, sort_keys=True))
        return 0
    if args.command == "check":
        results = check_project(root)
        for result in results:
            print(f"{'PASS' if result.passed else 'FAIL'} {result.name}")
        return 0 if all(result.passed for result in results) else 1
    if args.command == "state":
        print(json.dumps(Store(root).load_state(args.project).to_dict(), indent=2, sort_keys=True))
        return 0
    if args.command == "graph":
        graph = Store(root).load_graph()
        ready = [t.id for t in graph.ready()]
        summary = {
            "tasks": len(graph.tasks),
            "succeeded": sorted(graph.succeeded()),
            "ready": ready,
            "by_status": {},
        }
        for t in graph.tasks.values():
            summary["by_status"].setdefault(t.status.value, []).append(t.id)
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0
    if args.command in {"run", "resume"}:
        sup = Supervisor(root)
        state = sup.run_until_idle(args.project, max_cycles=args.max)
        print(json.dumps(state.to_dict(), indent=2, sort_keys=True))
        return 0 if state.phase not in {"blocked"} else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
