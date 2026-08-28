from __future__ import annotations

from .models import TaskStatus


_ALLOWED: dict[TaskStatus, set[TaskStatus]] = {
    TaskStatus.PENDING: {TaskStatus.READY, TaskStatus.RUNNING},
    TaskStatus.READY: {TaskStatus.RUNNING},
    TaskStatus.RUNNING: {TaskStatus.VERIFYING, TaskStatus.FAILED},
    TaskStatus.VERIFYING: {TaskStatus.COMPLETE, TaskStatus.FAILED},
    TaskStatus.FAILED: {TaskStatus.RETRYABLE, TaskStatus.BLOCKED},
    TaskStatus.RETRYABLE: {TaskStatus.RUNNING, TaskStatus.BLOCKED},
}


class InvalidStateTransition(ValueError):
    pass


class StateTransitionValidator:
    """Central guard for task lifecycle transitions."""

    @staticmethod
    def validate(old: TaskStatus, new: TaskStatus, reason: str | None = None) -> None:
        if old == new:
            return
        if new not in _ALLOWED.get(old, set()):
            raise InvalidStateTransition(
                f"invalid transition {old.value} -> {new.value}: {reason or 'no reason'}"
            )
