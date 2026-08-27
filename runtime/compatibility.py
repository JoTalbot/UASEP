from __future__ import annotations

from .autonomous_loop import AutonomousLoop


class LegacyRuntime:
    """Explicit compatibility boundary for the pre-canonical AutonomousLoop API."""

    def __init__(self, loop: AutonomousLoop) -> None:
        self.loop = loop

    def run_once(self, *args, **kwargs):
        return self.loop.run_once(*args, **kwargs)
