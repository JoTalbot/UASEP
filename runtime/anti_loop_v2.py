from __future__ import annotations

from collections import defaultdict, deque


class StagnationDetector:
    """Detect repeated failed attempts without falsely blocking successful work."""

    def __init__(self, threshold: int = 3) -> None:
        if threshold < 1:
            raise ValueError("threshold must be >= 1")
        self.threshold = threshold
        self._history: dict[str, deque[bool]] = defaultdict(lambda: deque(maxlen=threshold))

    def observe(self, task_id: str, success: bool) -> bool:
        history = self._history[task_id]
        history.append(success)
        return len(history) == self.threshold and not any(history)
