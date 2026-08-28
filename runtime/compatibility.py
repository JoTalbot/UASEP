"""LegacyRuntime explicitly points at Supervisor, not a second loop."""

from __future__ import annotations

from pathlib import Path

from .supervisor import Supervisor


class LegacyRuntime:
    """Name retained for tests; implementation is Supervisor."""

    def __init__(self, root: str | Path, **kwargs) -> None:
        self.supervisor = Supervisor(root, **kwargs)

    def run_once(self, project_id: str):
        return self.supervisor.run_once(project_id)

    def run_until_idle(self, project_id: str, max_cycles: int = 100):
        return self.supervisor.run_until_idle(project_id, max_cycles=max_cycles)
