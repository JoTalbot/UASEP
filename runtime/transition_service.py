from __future__ import annotations

from .models import TaskStatus, Task
from .state_events import StateChangeEvent
from .state_validator import StateTransitionValidator


class StateTransitionService:
    """Single lifecycle gateway for future runtime state mutations."""

    def __init__(self, source: str = "runtime") -> None:
        self.source = source

    def transition(
        self,
        task: Task,
        target: TaskStatus,
        *,
        reason: str,
    ) -> StateChangeEvent:
        previous = task.status
        StateTransitionValidator.validate(previous, target, reason)
        task.status = target
        return StateChangeEvent.create(
            task_id=task.id,
            old_state=previous.value,
            new_state=target.value,
            reason=reason,
            source=self.source,
        )
