from __future__ import annotations

from dataclasses import dataclass

from .task_graph import TaskGraph


@dataclass(frozen=True, slots=True)
class ReplanDecision:
    action: str
    task_id: str | None = None
    reason: str = ""


class Replanner:
    """Select an independent ready task after failure without changing policy."""

    def choose(self, graph: TaskGraph, failed_task_id: str) -> ReplanDecision:
        candidates = [task for task in graph.ready() if task.id != failed_task_id]
        if not candidates:
            return ReplanDecision("ESCALATE", reason="no independent ready task")
        candidate = candidates[0]
        return ReplanDecision("CONTINUE", candidate.id, "selected next independent ready task")
