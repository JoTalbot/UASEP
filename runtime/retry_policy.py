from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RetryDecision:
    retry: bool
    attempt: int
    reason: str


class RetryPolicy:
    """Pure finite retry policy; attempt and strategy state live in Task."""

    def __init__(self, max_attempts: int = 3) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        self.max_attempts = max_attempts

    def decide(
        self,
        task_id: str,
        attempt: int,
        strategy: str,
        previous_strategy: str | None = None,
    ) -> RetryDecision:
        del task_id
        if attempt >= self.max_attempts:
            return RetryDecision(False, attempt, "maximum attempts reached")
        if previous_strategy is not None and previous_strategy == strategy:
            return RetryDecision(False, attempt, "strategy unchanged")
        return RetryDecision(True, attempt + 1, "new strategy permitted")
