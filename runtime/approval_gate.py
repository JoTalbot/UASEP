from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ApprovalRequest:
    operation: str
    reason: str
    destructive: bool = False


class ApprovalGate:
    """Policy boundary. Destructive operations require an explicit decision."""

    def __init__(self, approved: set[str] | None = None) -> None:
        self.approved = approved or set()

    def check(self, request: ApprovalRequest) -> bool:
        if not request.destructive:
            return True
        return request.operation in self.approved
