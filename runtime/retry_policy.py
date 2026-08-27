from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RetryDecision:
    retry: bool
    attempt: int
    reason: str


class RetryPolicy:
    """Finite retry policy that requires a strategy fingerprint to change."""

    def __init__(self, max_attempts: int = 3) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        self.max_attempts = max_attempts
        self._last_strategy: dict[str, str] = {}

    def decide(self, task_id: str, attempt: int, strategy: str) -> RetryDecision:
        if attempt >= self.max_attempts:
            return RetryDecision(False, attempt, "maximum attempts reached")
        previous = self._last_strategy.get(task_id)
        if previous == strategy:
            return RetryDecision(False, attempt, "strategy unchanged")
        self._last_strategy[task_id] = strategy
        return RetryDecision(True, attempt + 1, "new strategy permitted")
