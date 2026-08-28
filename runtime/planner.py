from __future__ import annotations

from .models import Task


class Planner:
    """Deterministic baseline planner with stable priority ordering."""

    def ready_tasks(
        self,
        tasks: list[Task],
        completed: set[str],
        max_failures: int = 3,
    ) -> list[Task]:
        """Return all currently executable tasks in deterministic order."""
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
