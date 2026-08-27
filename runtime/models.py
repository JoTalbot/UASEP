from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TaskStatus(str, Enum):
    BACKLOG = "backlog"
    READY = "ready"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    DONE = "done"
    FAILED = "failed"


@dataclass
class Capability:
    name: str
    available: bool
    notes: str = ""


@dataclass
class Task:
    id: str
    title: str
    priority: int = 50
    status: TaskStatus = TaskStatus.BACKLOG
    dependencies: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_ready(self, completed: set[str]) -> bool:
        return self.status in {TaskStatus.BACKLOG, TaskStatus.READY} and all(
            dep in completed for dep in self.dependencies
        )


@dataclass
class Evidence:
    task_id: str
    kind: str
    status: str
    detail: str
    source: str = ""


@dataclass
class ProjectState:
    project_id: str
    phase: str = "initializing"
    current_task: str | None = None
    completed_tasks: set[str] = field(default_factory=set)
    blockers: list[str] = field(default_factory=list)
    iteration: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_id": self.project_id,
            "phase": self.phase,
            "current_task": self.current_task,
            "completed_tasks": sorted(self.completed_tasks),
            "blockers": self.blockers,
            "iteration": self.iteration,
        }
