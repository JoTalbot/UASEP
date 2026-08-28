from __future__ import annotations

import hashlib
import json
from typing import Any

from .models import TERMINAL_SUCCESS, Task, TaskStatus


class TaskGraph:
    """Canonical dependency-aware task graph with persistence and integrity checks."""

    def __init__(self, tasks: list[Task] | None = None) -> None:
        self.tasks: dict[str, Task] = {}
        for task in tasks or []:
            self.add(task, allow_forward_refs=True)
        self.validate()

    def add(self, task: Task, *, allow_forward_refs: bool = False) -> None:
        if task.id in self.tasks:
            raise ValueError(f"duplicate task id: {task.id}")
        if task.id in task.dependencies:
            raise ValueError(f"self-dependency forbidden: {task.id}")
        if not allow_forward_refs:
            missing = set(task.dependencies) - self.tasks.keys()
            if missing:
                raise ValueError(f"unknown dependencies: {sorted(missing)}")
        self.tasks[task.id] = task
        if self._has_cycle():
            del self.tasks[task.id]
            raise ValueError(f"cycle detected involving task: {task.id}")

    def succeeded(self) -> set[str]:
        return {task.id for task in self.tasks.values() if task.status in TERMINAL_SUCCESS}

    def ready(self) -> list[Task]:
        done = self.succeeded()
        return sorted((t for t in self.tasks.values() if t.is_ready(done)), key=lambda t: (-t.priority, t.id))

    def apply(self, task_id: str, status: TaskStatus, evidence_id: str | None = None) -> None:
        task = self.tasks[task_id]
        task.status = status
        if evidence_id and evidence_id not in task.evidence_ids:
            task.evidence_ids.append(evidence_id)
        if status == TaskStatus.FAILED:
            task.failure_count += 1
            task.status = TaskStatus.RETRYABLE

    def validate(self) -> None:
        known = set(self.tasks)
        for task in self.tasks.values():
            if task.id in task.dependencies:
                raise ValueError(f"self-dependency: {task.id}")
            missing = set(task.dependencies) - known
            if missing:
                raise ValueError(f"unknown dependencies on {task.id}: {sorted(missing)}")
        if self._has_cycle():
            raise ValueError("cycle detected in task graph")

    def _has_cycle(self) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {tid: WHITE for tid in self.tasks}

        def dfs(node: str) -> bool:
            color[node] = GRAY
            for dep in self.tasks[node].dependencies:
                if dep not in color:
                    continue
                if color[dep] == GRAY:
                    return True
                if color[dep] == WHITE and dfs(dep):
                    return True
            color[node] = BLACK
            return False

        return any(color[n] == WHITE and dfs(n) for n in self.tasks)

    def fingerprint(self) -> str:
        payload = [self.tasks[key].definition_payload() for key in sorted(self.tasks)]
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def to_dict(self, protocol_version: str = "3.2.0-new") -> dict[str, Any]:
        return {"protocol": "UASEP", "protocol_version": protocol_version, "graph_fingerprint": self.fingerprint(), "tasks": [t.to_dict() for t in self.tasks.values()]}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TaskGraph":
        raw_tasks = data.get("tasks") or []
        tasks = [Task.from_dict(item) for item in raw_tasks]
        graph = cls.__new__(cls)
        graph.tasks = {}
        for task in tasks:
            if task.id in graph.tasks:
                raise ValueError(f"duplicate task id: {task.id}")
            graph.tasks[task.id] = task
        graph.validate()
        stored = data.get("graph_fingerprint")
        if stored and stored != graph.fingerprint():
            raise ValueError("task graph fingerprint mismatch")
        return graph
