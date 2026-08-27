from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ApprovalLevel(str, Enum):
    NONE = "none"
    HUMAN = "human"


@dataclass(frozen=True, slots=True)
class ApprovalRequest:
    action: str
    reason: str
    level: ApprovalLevel = ApprovalLevel.HUMAN
    approved: bool = False


class ApprovalGate:
    """Policy boundary for actions that should not be performed autonomously."""

    def require(self, action: str, reason: str) -> ApprovalRequest:
        return ApprovalRequest(action=action, reason=reason)

    @staticmethod
    def can_execute(request: ApprovalRequest) -> bool:
        return request.level == ApprovalLevel.NONE or request.approved
