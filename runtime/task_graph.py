from __future__ import annotations

from dataclasses import dataclass, field


VALID_STATUSES = {"pending", "done", "blocked"}


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
    """Dependency-aware task graph with structural validation."""

    def __init__(self, tasks: list[TaskNode] | None = None) -> None:
        self.tasks = {}
        for task in tasks or []:
            if task.id in self.tasks:
                raise ValueError(f"duplicate task id: {task.id}")
            self.tasks[task.id] = task
        self.validate()

    def add(self, task: TaskNode) -> None:
        if task.id in self.tasks:
            raise ValueError(f"duplicate task id: {task.id}")
        if task.id in task.dependencies:
            raise ValueError(f"self-dependency: {task.id}")
        missing = task.dependencies - self.tasks.keys()
        if missing:
            raise ValueError(f"unknown dependencies: {sorted(missing)}")
        self.tasks[task.id] = task
        try:
            self.validate()
        except ValueError:
            del self.tasks[task.id]
            raise

    def validate(self) -> None:
        known = set(self.tasks)
        for task in self.tasks.values():
            if task.status not in VALID_STATUSES:
                raise ValueError(f"invalid task status: {task.status}")
            if task.id in task.dependencies:
                raise ValueError(f"self-dependency: {task.id}")
            missing = task.dependencies - known
            if missing:
                raise ValueError(f"unknown dependencies on {task.id}: {sorted(missing)}")

        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(task_id: str) -> None:
            if task_id in visiting:
                raise ValueError(f"dependency cycle detected at: {task_id}")
            if task_id in visited:
                return
            visiting.add(task_id)
            for dependency in self.tasks[task_id].dependencies:
                visit(dependency)
            visiting.remove(task_id)
            visited.add(task_id)

        for task_id in self.tasks:
            visit(task_id)

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
