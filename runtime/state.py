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
        if not isinstance(project_id, str) or not project_id.strip():
            raise ValueError("project_id must be a non-empty string")
        path = self._path_for(project_id)
        # Fallback to shared state.json when per-project file missing
        if not path.exists() and self.per_project and self.path.exists():
            path = self.path
        if not path.exists():
            return ProjectState(project_id=project_id)
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("runtime state must contain an object")
        data: dict[str, Any] = raw
        if needs_migration(data, RUNTIME_VERSION):
            data = migrate_runtime_state(data, RUNTIME_VERSION)
        if not isinstance(data, dict):
            raise ValueError("migrated runtime state must contain an object")

        raw_failures = data.get("task_failures") or {}
        if not isinstance(raw_failures, dict):
            raise ValueError("task_failures must be an object")
        task_failures: dict[str, int] = {}
        for key, value in raw_failures.items():
            if not isinstance(key, str) or not key.strip():
                raise ValueError("task_failures keys must be non-empty strings")
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError("task_failures values must be non-negative integers")
            task_failures[key] = value

        completed = data.get("completed_tasks", [])
        blockers = data.get("blockers", [])
        if not isinstance(completed, list) or not all(isinstance(item, str) and item.strip() for item in completed):
            raise ValueError("completed_tasks must be a list of non-empty strings")
        if not isinstance(blockers, list) or not all(isinstance(item, str) for item in blockers):
            raise ValueError("blockers must be a list of strings")
        iteration = data.get("iteration", 0)
        if isinstance(iteration, bool) or not isinstance(iteration, int) or iteration < 0:
            raise ValueError("iteration must be a non-negative integer")
        phase = data.get("phase", "initializing")
        if not isinstance(phase, str) or not phase.strip():
            raise ValueError("phase must be a non-empty string")
        current_task = data.get("current_task")
        if current_task is not None and (not isinstance(current_task, str) or not current_task.strip()):
            raise ValueError("current_task must be None or a non-empty string")

        return ProjectState(
            project_id=data.get("project_id", project_id),
            phase=phase,
            current_task=current_task,
            completed_tasks=set(completed),
            blockers=list(blockers),
            iteration=iteration,
            task_failures=task_failures,
        )

    def save(self, state: ProjectState) -> None:
        if not isinstance(state, ProjectState):
            raise ValueError("state must be a ProjectState")
        if not isinstance(state.project_id, str) or not state.project_id.strip():
            raise ValueError("state project_id must be a non-empty string")
        path = self._path_for(state.project_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = state.to_dict()
        payload["protocol_version"] = RUNTIME_VERSION
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
