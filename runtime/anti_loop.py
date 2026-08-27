from __future__ import annotations

from collections import deque


class StagnationDetector:
    """Detect repeated outcomes so an agent can change strategy instead of looping."""

    def __init__(self, window: int = 3):
        if window < 2:
            raise ValueError("window must be >= 2")
        self.window = window
        self._history: deque[str] = deque(maxlen=window)

    def record(self, fingerprint: str) -> None:
        self._history.append(fingerprint)

    @property
    def stagnant(self) -> bool:
        return len(self._history) == self.window and len(set(self._history)) == 1

    def reset(self) -> None:
        self._history.clear()
