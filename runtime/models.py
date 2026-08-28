from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class TaskStatus(str, Enum):
    QUEUED = "queued"
    READY = "ready"
    RUNNING = "running"
    BLOCKED = "blocked"
    FAILED = "failed"
    VERIFIED = "verified"
    COMPLETE = "complete"
    CANCELLED = "cancelled"


TERMINAL_SUCCESS = {TaskStatus.VERIFIED, TaskStatus.COMPLETE}
ACTIVE_PENDING = {TaskStatus.QUEUED, TaskStatus.READY}


@dataclass
class Capability:
    name: str
    available: bool
    notes: str = ""
    discovered: bool = True
    approval_required: bool = False
    source: str = "host"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Task:
    id: str
    objective: str
    status: TaskStatus = TaskStatus.QUEUED
    priority: float = 50.0
    dependencies: list[str] = field(default_factory=list)
    acceptance_criteria: list[str] = field(default_factory=list)
    risk: str = "low"
    owner: str | None = None
    evidence_ids: list[str] = field(default_factory=list)
    notes: str = ""
    failure_count: int = 0

    def is_ready(self, succeeded: set[str]) -> bool:
        if self.status not in ACTIVE_PENDING:
            return False
        return all(dep in succeeded for dep in self.dependencies)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "objective": self.objective,
            "status": self.status.value,
            "priority": self.priority,
            "dependencies": list(self.dependencies),
            "acceptance_criteria": list(self.acceptance_criteria),
            "risk": self.risk,
            "owner": self.owner,
            "evidence_ids": list(self.evidence_ids),
            "notes": self.notes,
            "failure_count": self.failure_count,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        status = data.get("status", "queued")
        if isinstance(status, TaskStatus):
            st = status
        else:
            st = TaskStatus(str(status))
        return cls(
            id=str(data["id"]),
            objective=str(data.get("objective") or data.get("title") or data["id"]),
            status=st,
            priority=float(data.get("priority", 50)),
            dependencies=list(data.get("dependencies") or []),
            acceptance_criteria=list(data.get("acceptance_criteria") or []),
            risk=str(data.get("risk", "low")),
            owner=data.get("owner"),
            evidence_ids=list(data.get("evidence_ids") or []),
            notes=str(data.get("notes") or ""),
            failure_count=int(data.get("failure_count", 0)),
        )


@dataclass
class Evidence:
    id: str
    task_id: str
    kind: str
    status: str
    detail: str
    source: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ProjectState:
    protocol: str = "UASEP"
    protocol_version: str = "3.2.0-new"
    project_id: str = ""
    phase: str = "initializing"
    autonomy_level: str = "L3"
    environment: str = "unknown"
    objective: str = ""
    active_task: str | None = None
    completed_tasks: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    iteration: int = 0
    last_verified: str | None = None
    next_best_actions: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "protocol": self.protocol,
            "protocol_version": self.protocol_version,
            "project_id": self.project_id,
            "phase": self.phase,
            "autonomy_level": self.autonomy_level,
            "environment": self.environment,
            "objective": self.objective,
            "active_task": self.active_task,
            "completed_tasks": list(self.completed_tasks),
            "blockers": list(self.blockers),
            "iteration": self.iteration,
            "last_verified": self.last_verified,
            "next_best_actions": list(self.next_best_actions),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any], default_project_id: str = "") -> "ProjectState":
        return cls(
            protocol=str(data.get("protocol", "UASEP")),
            protocol_version=str(data.get("protocol_version", "3.2.0-new")),
            project_id=str(data.get("project_id") or default_project_id),
            phase=str(data.get("phase") or data.get("project_state") or "initializing"),
            autonomy_level=str(data.get("autonomy_level", "L3")),
            environment=str(data.get("environment", "unknown")),
            objective=str(data.get("objective", "")),
            active_task=data.get("active_task") or data.get("current_task"),
            completed_tasks=list(data.get("completed_tasks") or []),
            blockers=list(data.get("blockers") or []),
            iteration=int(data.get("iteration", 0)),
            last_verified=data.get("last_verified"),
            next_best_actions=list(data.get("next_best_actions") or []),
        )


@dataclass(frozen=True, slots=True)
class CycleResult:
    task_id: str | None
    status: str
    iteration: int
    reason: str = ""
