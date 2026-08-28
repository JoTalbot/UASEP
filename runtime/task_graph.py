"""Deprecated path: use runtime.graph.TaskGraph and runtime.models.Task.

TaskNode is a minimal adapter so remaining call sites compile; new code must
not use this module.
"""

from __future__ import annotations

from .graph import TaskGraph as _TaskGraph
from .models import Task, TaskStatus


class TaskNode(Task):
    """Adapter: title maps to objective; pending/done map to queued/verified."""

    def __init__(
        self,
        id: str,
        title: str = "",
        priority: int = 0,
        dependencies: set[str] | list[str] | None = None,
        status: str = "pending",
        **kwargs,
    ) -> None:
        deps = list(dependencies or [])
        st = TaskStatus.QUEUED if status in {"pending", "queued", "ready"} else (
            TaskStatus.VERIFIED if status in {"done", "verified", "complete"} else TaskStatus.QUEUED
        )
        super().__init__(
            id=id,
            objective=title or kwargs.get("objective") or id,
            status=st,
            priority=float(priority),
            dependencies=deps,
            acceptance_criteria=list(kwargs.get("acceptance_criteria") or []),
        )

    def ready(self, completed: set[str]) -> bool:
        return self.is_ready(completed)


class TaskGraph(_TaskGraph):
    def mark_done(self, task_id: str) -> None:
        self.apply(task_id, TaskStatus.VERIFIED)

    def completed(self) -> set[str]:
        return self.succeeded()
