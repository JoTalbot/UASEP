from __future__ import annotations

from dataclasses import dataclass

from .models import Task


@dataclass(frozen=True, slots=True)
class ApprovalRequest:
    key: str
    summary: str
    destructive: bool = False


class ApprovalGate:
    """Default-allow for non-destructive work; block destructive without policy."""

    def __init__(self, allow_destructive: bool = False) -> None:
        self.allow_destructive = allow_destructive

    def allow(self, task: Task, request: ApprovalRequest | None = None) -> bool:
        req = request or ApprovalRequest(
            key=f"execute:{task.id}",
            summary=task.objective,
            destructive=task.risk in {"high", "critical"},
        )
        if req.destructive and not self.allow_destructive:
            return False
        return True
