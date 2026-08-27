from __future__ import annotations

from .models import Task


class Planner:
    """Deterministic baseline planner; LLM-driven planners can implement the same contract."""

    def next_task(self, tasks: list[Task], completed: set[str]) -> Task | None:
        ready = [task for task in tasks if task.is_ready(completed)]
        if not ready:
            return None
        return max(ready, key=lambda task: task.priority)
