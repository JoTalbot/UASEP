from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class TaskNode:
    id: str
    title: str
    priority: int = 0
    dependencies: set[str] = field(default_factory=set)
    status: str = "pending"

    def ready(self, completed: set[str]) -> bool:
        return self.status == "pending" and self.dependencies.issubset(completed)


class TaskGraph:
    """Small dependency-aware task graph used by the reference supervisor."""

    def __init__(self, tasks: list[TaskNode] | None = None) -> None:
        self.tasks = {task.id: task for task in tasks or []}

    def add(self, task: TaskNode) -> None:
        if task.id in self.tasks:
            raise ValueError(f"duplicate task id: {task.id}")
        missing = task.dependencies - self.tasks.keys()
        if missing:
            raise ValueError(f"unknown dependencies: {sorted(missing)}")
        self.tasks[task.id] = task

    def completed(self) -> set[str]:
        return {task.id for task in self.tasks.values() if task.status == "done"}

    def ready(self) -> list[TaskNode]:
        completed = self.completed()
        return sorted(
            (task for task in self.tasks.values() if task.ready(completed)),
            key=lambda task: (-task.priority, task.id),
        )

    def mark_done(self, task_id: str) -> None:
        task = self.tasks[task_id]
        task.status = "done"
