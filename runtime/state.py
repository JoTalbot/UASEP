from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .migration import migrate_runtime_state, needs_migration
from .models import ProjectState

RUNTIME_VERSION = "3.1.2"


class StateStore:
    """Persistent state store; optional per-project files under .uasep/state/."""

    def __init__(self, root: str | Path, *, per_project: bool = False):
        self.root = Path(root)
        self.per_project = per_project
        self.path = self.root / ".uasep" / "state.json"

    def _path_for(self, project_id: str) -> Path:
        if self.per_project:
            return self.root / ".uasep" / "state" / f"{project_id}.json"
        return self.path

    def load(self, project_id: str) -> ProjectState:
        path = self._path_for(project_id)
        # Fallback to shared state.json when per-project file missing
        if not path.exists() and self.per_project and self.path.exists():
            path = self.path
        if not path.exists():
            return ProjectState(project_id=project_id)
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        if needs_migration(data, RUNTIME_VERSION):
            data = migrate_runtime_state(data, RUNTIME_VERSION)
        raw_failures = data.get("task_failures") or {}
        task_failures = {
            str(k): int(v) for k, v in raw_failures.items() if isinstance(v, (int, float))
        }
        return ProjectState(
            project_id=data.get("project_id", project_id),
            phase=data.get("phase", "initializing"),
            current_task=data.get("current_task"),
            completed_tasks=set(data.get("completed_tasks", [])),
            blockers=list(data.get("blockers", [])),
            iteration=int(data.get("iteration", 0)),
            task_failures=task_failures,
        )

    def save(self, state: ProjectState) -> None:
        path = self._path_for(state.project_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = state.to_dict()
        payload["protocol_version"] = RUNTIME_VERSION
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
