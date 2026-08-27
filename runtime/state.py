from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import ProjectState


class StateStore:
    """Small, dependency-free persistent state store for the reference runtime."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.path = self.root / ".uasep" / "state.json"

    def load(self, project_id: str) -> ProjectState:
        if not self.path.exists():
            return ProjectState(project_id=project_id)
        data: dict[str, Any] = json.loads(self.path.read_text(encoding="utf-8"))
        return ProjectState(
            project_id=data.get("project_id", project_id),
            phase=data.get("phase", "initializing"),
            current_task=data.get("current_task"),
            completed_tasks=set(data.get("completed_tasks", [])),
            blockers=list(data.get("blockers", [])),
            iteration=int(data.get("iteration", 0)),
        )

    def save(self, state: ProjectState) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(state.to_dict(), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
