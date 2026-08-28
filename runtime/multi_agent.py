from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from .models import Task, TaskStatus


@dataclass
class AgentSlot:
    """Named worker slot with an optional role label."""

    name: str
    role: str = "developer"
    busy: bool = False
    current_task: str | None = None


@dataclass
class MultiAgentCoordinator:
    """Minimal parallel allocation: assign ready tasks to free agent slots.

    Write-set conflicts are the caller's responsibility; this only tracks
    occupancy and returns assignment decisions.
    """

    agents: list[AgentSlot] = field(default_factory=list)

    def register(self, name: str, role: str = "developer") -> AgentSlot:
        slot = AgentSlot(name=name, role=role)
        self.agents.append(slot)
        return slot

    def free_agents(self) -> list[AgentSlot]:
        return [a for a in self.agents if not a.busy]

    def assign(self, ready: list[Task]) -> list[tuple[AgentSlot, Task]]:
        assignments: list[tuple[AgentSlot, Task]] = []
        free = self.free_agents()
        for task, agent in zip(ready, free):
            agent.busy = True
            agent.current_task = task.id
            task.status = TaskStatus.IN_PROGRESS
            assignments.append((agent, task))
        return assignments

    def release(self, agent_name: str) -> None:
        for agent in self.agents:
            if agent.name == agent_name:
                agent.busy = False
                agent.current_task = None
                return

    def run_parallel(
        self,
        ready: list[Task],
        execute: Callable[[Task], bool],
    ) -> list[tuple[str, str, bool]]:
        """Assign and execute; returns (agent, task_id, success)."""
        results: list[tuple[str, str, bool]] = []
        for agent, task in self.assign(ready):
            ok = bool(execute(task))
            results.append((agent.name, task.id, ok))
            self.release(agent.name)
        return results
