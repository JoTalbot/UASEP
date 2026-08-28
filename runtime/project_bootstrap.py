from __future__ import annotations

import json
from pathlib import Path

REQUIRED_DIRS = (
    ".uasep",
    ".uasep/state",
    ".uasep/planning",
    ".uasep/knowledge",
    ".uasep/evidence",
    ".uasep/checkpoints",
)

DEFAULT_MARKDOWN = {
    ".uasep/state/PROJECT_STATE.md": "# Project State\n\nInitialized by UASEP bootstrap.\n",
    ".uasep/state/HANDOFF.md": "# Handoff\n\nNo handoff recorded.\n",
    ".uasep/planning/MASTER_PLAN.md": "# Master Plan\n\nTo be discovered during audit.\n",
    ".uasep/planning/BACKLOG.md": "# Backlog\n\nMachine truth: `.uasep/graph.json`.\n",
    ".uasep/knowledge/DECISIONS.md": "# Decisions\n\nNo decisions recorded.\n",
    ".uasep/knowledge/FAILURES.md": "# Failures\n\nNo failures recorded.\n",
    ".uasep/evidence/TESTS.md": "# Test Evidence\n\nSee evidence/log.jsonl for runtime evidence.\n",
    ".uasep/evidence/BUILDS.md": "# Build Evidence\n\nNo build evidence recorded.\n",
}


def bootstrap_project(root: Path, project_name: str | None = None) -> list[Path]:
    """Create project-local UASEP scaffold without overwriting existing files."""
    root = root.resolve()
    name = project_name or root.name
    created: list[Path] = []

    for relative in REQUIRED_DIRS:
        path = root / relative
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(path)

    manifest = root / ".uasep" / "manifest.yaml"
    if not manifest.exists():
        manifest.write_text(
            "protocol: UASEP\n"
            "protocol_version: 3.2.0-new\n"
            f"project_instance: {name}\n"
            "project_state: initializing\n"
            "autonomy_level: L3\n"
            "source_of_truth: protocol/\n"
            "local_state: .uasep/\n",
            encoding="utf-8",
        )
        created.append(manifest)

    state_path = root / ".uasep" / "state.json"
    if not state_path.exists():
        state = {
            "protocol": "UASEP",
            "protocol_version": "3.2.0-new",
            "project_id": name,
            "phase": "initializing",
            "autonomy_level": "L3",
            "environment": "unknown",
            "objective": "",
            "active_task": None,
            "completed_tasks": [],
            "blockers": [],
            "iteration": 0,
            "last_verified": None,
            "next_best_actions": ["Audit repository", "Build task graph", "Execute highest-value ready task"],
        }
        state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        created.append(state_path)

    graph_path = root / ".uasep" / "graph.json"
    if not graph_path.exists():
        graph = {
            "protocol": "UASEP",
            "protocol_version": "3.2.0-new",
            "tasks": [],
        }
        graph_path.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        created.append(graph_path)

    defaults = dict(DEFAULT_MARKDOWN)
    state_md = ".uasep/state/PROJECT_STATE.md"
    if not (root / state_md).exists():
        defaults[state_md] = f"# Project State\n\nProject: {name}\nStatus: initializing\n\n"

    for relative, content in defaults.items():
        path = root / relative
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            created.append(path)

    return created
