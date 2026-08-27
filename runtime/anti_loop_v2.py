from __future__ import annotations

from collections import deque


class StagnationDetector:
    """Compatibility API for failure-streak based anti-loop detection."""

    def __init__(self, threshold: int = 3):
        if threshold < 2:
            raise ValueError("threshold must be >= 2")
        self.threshold = threshold
        self._failures: deque[str] = deque(maxlen=threshold)

    def observe(self, task_id: str, success: bool) -> bool:
        if success:
            self._failures.clear()
            return False
        self._failures.append(task_id)
        return len(self._failures) == self.threshold and len(set(self._failures)) == 1
