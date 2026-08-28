from __future__ import annotations

from .models import Task


class Planner:
    """Deterministic baseline planner with stable priority ordering."""

    def validate_tasks(self, tasks: list[Task]) -> None:
        """Validate task graph invariants before planning."""
        ids = [task.id for task in tasks]
        if any(not isinstance(task_id, str) or not task_id.strip() for task_id in ids):
            raise ValueError("task ids must be non-empty strings")
        if len(ids) != len(set(ids)):
            raise ValueError("task ids must be unique")

        known = set(ids)
        for task in tasks:
            if not isinstance(task.dependencies, list):
                raise ValueError(f"task dependencies must be a list: {task.id}")
            missing = [dep for dep in task.dependencies if dep not in known]
            if missing:
                raise ValueError(f"unknown task dependencies: {missing}")

        self._assert_acyclic(tasks)

    def _assert_acyclic(self, tasks: list[Task]) -> None:
        graph = {task.id: task.dependencies for task in tasks}
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(task_id: str) -> None:
            if task_id in visiting:
                raise ValueError("task dependency cycle detected")
            if task_id in visited:
                return
            visiting.add(task_id)
            for dependency in graph.get(task_id, []):
                visit(dependency)
            visiting.remove(task_id)
            visited.add(task_id)

        for task_id in graph:
            visit(task_id)

    def ready_tasks(
        self,
        tasks: list[Task],
        completed: set[str],
        max_failures: int = 3,
    ) -> list[Task]:
        """Return all currently executable tasks in deterministic order."""
        if not isinstance(max_failures, int) or max_failures < 1:
            raise ValueError("max_failures must be a positive integer")
        if not isinstance(completed, set):
            raise ValueError("completed must be a set")
        self.validate_tasks(tasks)
        ready = [
            task
            for task in tasks
            if task.id not in completed and task.is_ready(completed, max_failures)
        ]
        return sorted(ready, key=lambda task: (-task.priority, task.id))

    def next_task(
        self,
        tasks: list[Task],
        completed: set[str],
        max_failures: int = 3,
    ) -> Task | None:
        """Return the highest-priority ready task, or None when blocked."""
        ready = self.ready_tasks(tasks, completed, max_failures)
        return ready[0] if ready else None
