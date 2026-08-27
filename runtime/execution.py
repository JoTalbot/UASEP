from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    success: bool
    value: Any = None
    error: str | None = None


class ExecutionEngine:
    """Capability-aware execution boundary. The host supplies the actual operation."""

    def execute(self, operation: Callable[[], Any]) -> ExecutionResult:
        try:
            return ExecutionResult(True, operation())
        except Exception as exc:  # boundary intentionally captures adapter failures
            return ExecutionResult(False, error=f"{type(exc).__name__}: {exc}")
