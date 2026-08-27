from __future__ import annotations

from dataclasses import dataclass
from .task_graph import TaskGraph, TaskNode


@dataclass(frozen=True, slots=True)
class ReplanResult:
    action: str
    reason: str


class Replanner:
    """Choose a bounded recovery action after a failed task."""

    def choose(self, graph: TaskGraph, failed_task_id: str) -> ReplanResult:
        task = graph.tasks[failed_task_id]
        alternatives = [
            candidate for candidate in graph.tasks.values()
            if candidate.id != failed_task_id and candidate.status == "pending"
            and failed_task_id not in candidate.dependencies
        ]
        if alternatives:
            alternatives.sort(key=lambda item: (-item.priority, item.id))
            return ReplanResult("switch_task", f"try independent task {alternatives[0].id}")
        return ReplanResult("escalate", f"no safe alternative for {task.id}")
