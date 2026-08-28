from __future__ import annotations

import argparse
import json
from pathlib import Path

from .bootstrap import bootstrap_project
from .conformance import check_project
from .discovery import capabilities_dict
from .migration import migrate_runtime_state, needs_migration
from .models import Task
from .planner import Planner
from .runner import run_project
from .state import RUNTIME_VERSION, StateStore


def main() -> int:
    parser = argparse.ArgumentParser(prog="uasep")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("bootstrap", help="create missing project-local UASEP state")
    sub.add_parser("capabilities", help="discover conservative local capabilities")
    sub.add_parser("check", help="check project conformance")
    state = sub.add_parser("state", help="show persisted project state")
    state.add_argument("--project", default=Path.cwd().name)
    state.add_argument("--per-project", action="store_true")
    sub.add_parser("status", help="compact phase/blockers summary")
    plan = sub.add_parser("plan", help="show ready tasks for a demo graph")
    plan.add_argument("--json", action="store_true")
    run_p = sub.add_parser("run", help="run a single demo task through the supervisor")
    run_p.add_argument("--task-id", default="demo")
    run_p.add_argument("--title", default="Demo task")
    run_p.add_argument("--cycles", type=int, default=10)
    resume = sub.add_parser("resume", help="continue from persisted state with a demo task if needed")
    resume.add_argument("--cycles", type=int, default=10)
    mig = sub.add_parser("migrate", help="migrate .uasep runtime state to current version")
    mig.add_argument("--project", default=Path.cwd().name)
    mig.add_argument("--per-project", action="store_true")
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
        store = StateStore(".", per_project=getattr(args, "per_project", False))
        print(json.dumps(store.load(args.project).to_dict(), indent=2, sort_keys=True))
        return 0
    if args.command == "status":
        st = StateStore(".").load(Path.cwd().name)
        print(json.dumps({
            "phase": st.phase,
            "current_task": st.current_task,
            "completed": sorted(st.completed_tasks),
            "blockers": st.blockers,
            "iteration": st.iteration,
            "task_failures": st.task_failures,
        }, indent=2, sort_keys=True))
        return 0
    if args.command == "plan":
        demo = [
            Task("A", "bootstrap", priority=10),
            Task("B", "implement", priority=20, dependencies=["A"]),
            Task("C", "verify", priority=30, dependencies=["B"]),
        ]
        ready = Planner().ready_tasks(demo, set())
        if getattr(args, "json", False):
            print(json.dumps([{"id": t.id, "title": t.title, "priority": t.priority} for t in ready], indent=2))
        else:
            for t in ready:
                print(f"{t.priority:3d} {t.id} {t.title}")
        return 0
    if args.command == "run":
        result = run_project(
            Path.cwd(),
            Path.cwd().name,
            [Task(id=args.task_id, title=args.title)],
            max_cycles=args.cycles,
            executor=lambda _t: True,
        )
        print(json.dumps({
            "status": result.status,
            "iterations": result.iterations,
            "completed": list(result.completed),
            "blockers": list(result.blockers),
        }, indent=2, sort_keys=True))
        return 0 if result.status in {"verified", "maintenance"} else 1
    if args.command == "resume":
        project = Path.cwd().name
        store = StateStore(".")
        st = store.load(project)
        if not st.completed_tasks:
            remaining = [Task(id="resume-demo", title="Resume demo")]
        else:
            remaining = [Task(id="noop", title="noop")]
        result = run_project(
            Path.cwd(),
            project,
            remaining,
            max_cycles=args.cycles,
            executor=lambda _t: True,
        )
        print(json.dumps({
            "resumed_phase": st.phase,
            "status": result.status,
            "completed": list(result.completed),
            "blockers": list(result.blockers),
        }, indent=2, sort_keys=True))
        return 0
    if args.command == "migrate":
        store = StateStore(".", per_project=args.per_project)
        path = store._path_for(args.project)
        if not path.exists() and store.path.exists():
            path = store.path
        if not path.exists():
            print(json.dumps({"migrated": False, "reason": "no state file"}))
            return 1
        data = json.loads(path.read_text(encoding="utf-8"))
        if not needs_migration(data, RUNTIME_VERSION):
            print(json.dumps({"migrated": False, "version": RUNTIME_VERSION}))
            return 0
        new_data = migrate_runtime_state(data, RUNTIME_VERSION)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(new_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"migrated": True, "version": RUNTIME_VERSION, "path": str(path)}))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
