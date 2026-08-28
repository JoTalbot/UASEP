from __future__ import annotations

from dataclasses import dataclass

from .models import Task


@dataclass(frozen=True, slots=True)
class ApprovalRequest:
    key: str
    summary: str
    destructive: bool = False
    capability: str | None = None
    target: str | None = None


class ApprovalGate:
    """Policy boundary for concrete actions, not just abstract tasks."""

    def __init__(self, allow_destructive: bool = False, allowed_capabilities: set[str] | None = None) -> None:
        self.allow_destructive = allow_destructive
        self.allowed_capabilities = set(allowed_capabilities or ())

    def allow(self, task: Task, request: ApprovalRequest | None = None) -> bool:
        req = request or ApprovalRequest(
            key=f"execute:{task.id}",
            summary=task.objective,
            destructive=task.risk in {"high", "critical"},
            capability=task.required_capabilities[0] if task.required_capabilities else None,
        )
        if req.capability and self.allowed_capabilities and req.capability not in self.allowed_capabilities:
            return False
        if req.destructive and not self.allow_destructive:
            return False
        return True
