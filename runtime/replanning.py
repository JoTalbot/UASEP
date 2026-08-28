from __future__ import annotations

from dataclasses import dataclass

from .graph import TaskGraph


@dataclass(frozen=True, slots=True)
class ReplanDecision:
    action: str
    task_id: str | None = None
    reason: str = ""


class Replanner:
    """Select the next executable task without owning orchestration state."""

    def choose(self, graph: TaskGraph, failed_task_id: str) -> ReplanDecision:
        candidates = [task for task in graph.ready() if task.id != failed_task_id]
        if not candidates:
            return ReplanDecision("RETRY_FAILED", failed_task_id, "no independent ready task")
        candidate = candidates[0]
        return ReplanDecision("CONTINUE", candidate.id, "selected next independent ready task")
