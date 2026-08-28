"""Compatibility alias: prefer runtime.store.Store.

On branch `new`, StateStore delegates to Store so older call sites keep working
without a second persistence model.
"""

from __future__ import annotations

from pathlib import Path

from .models import ProjectState
from .store import Store


class StateStore:
    """Thin wrapper over Store.load_state / save_state."""

    def __init__(self, root: str | Path) -> None:
        self._store = Store(root)

    def load(self, project_id: str) -> ProjectState:
        return self._store.load_state(project_id)

    def save(self, state: ProjectState) -> None:
        self._store.save_state(state)
