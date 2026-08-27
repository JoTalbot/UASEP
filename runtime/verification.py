from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True, slots=True)
class VerificationResult:
    status: str
    passed: int
    failed: int
    details: tuple[str, ...] = ()


class VerificationEngine:
    """Runs explicit acceptance checks and never infers verification from execution alone."""

    def verify(self, checks: Iterable[tuple[str, Callable[[], bool]]]) -> VerificationResult:
        passed = failed = 0
        details: list[str] = []
        for name, check in checks:
            try:
                ok = bool(check())
            except Exception as exc:
                ok = False
                details.append(f"{name}: {type(exc).__name__}: {exc}")
            else:
                details.append(f"{name}: {'PASS' if ok else 'FAIL'}")
            passed += int(ok)
            failed += int(not ok)
        status = "VERIFIED" if failed == 0 else "FAILED"
        return VerificationResult(status, passed, failed, tuple(details))
