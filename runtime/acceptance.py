from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True, slots=True)
class CriterionResult:
    criterion: str
    passed: bool
    detail: str = ""


class AcceptanceEngine:
    """Evaluate explicit acceptance criteria and return auditable results."""

    def evaluate(self, criteria: Iterable[tuple[str, Callable[[], bool]]]) -> list[CriterionResult]:
        results: list[CriterionResult] = []
        for description, check in criteria:
            try:
                passed = bool(check())
                results.append(CriterionResult(description, passed, "check returned normally"))
            except Exception as exc:
                results.append(CriterionResult(description, False, f"{type(exc).__name__}: {exc}"))
        return results

    @staticmethod
    def accepted(results: Iterable[CriterionResult]) -> bool:
        results = list(results)
        return bool(results) and all(item.passed for item in results)
