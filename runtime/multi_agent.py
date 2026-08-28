from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
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
    """Deterministic parallel allocation with write-set conflict filtering."""

    agents: list[AgentSlot] = field(default_factory=list)

    def register(self, name: str, role: str = "developer") -> AgentSlot:
        if not name:
            raise ValueError("agent name must not be empty")
        if any(agent.name == name for agent in self.agents):
            raise ValueError(f"agent already registered: {name}")
        slot = AgentSlot(name=name, role=role)
        self.agents.append(slot)
        return slot

    def free_agents(self) -> list[AgentSlot]:
        return [a for a in self.agents if not a.busy]

    @staticmethod
    def conflicts(a: Task, b: Task) -> bool:
        """True when write sets overlap (empty sets never conflict)."""
        if not a.write_set or not b.write_set:
            return False
        return bool(set(a.write_set) & set(b.write_set))

    def filter_compatible(self, ready: list[Task]) -> list[Task]:
        """Greedy deterministic selection of pairwise compatible tasks."""
        selected: list[Task] = []
        for task in ready:
            if any(self.conflicts(task, s) for s in selected):
                continue
            selected.append(task)
        return selected

    def assign(self, ready: list[Task], *, respect_write_sets: bool = True) -> list[tuple[AgentSlot, Task]]:
        pool = self.filter_compatible(ready) if respect_write_sets else list(ready)
        assignments: list[tuple[AgentSlot, Task]] = []
        free = self.free_agents()
        for task, agent in zip(pool, free):
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
        raise ValueError(f"unknown agent: {agent_name}")

    def run_parallel(
        self,
        ready: list[Task],
        execute: Callable[[Task], bool],
        *,
        respect_write_sets: bool = True,
    ) -> list[tuple[str, str, bool]]:
        """Execute compatible assignments concurrently, preserving input order in results."""
        task_ids = [task.id for task in ready]
        if len(task_ids) != len(set(task_ids)):
            duplicates = sorted({task_id for task_id in task_ids if task_ids.count(task_id) > 1})
            raise ValueError(f"duplicate task ids in parallel batch: {', '.join(duplicates)}")

        assignments = self.assign(ready, respect_write_sets=respect_write_sets)
        if not assignments:
            return []

        def run_one(assignment: tuple[AgentSlot, Task]) -> tuple[str, str, bool]:
            agent, task = assignment
            try:
                ok = bool(execute(task))
            except Exception:
                ok = False
            finally:
                self.release(agent.name)
            return agent.name, task.id, ok

        with ThreadPoolExecutor(max_workers=len(assignments), thread_name_prefix="uasep-agent") as pool:
            futures = [pool.submit(run_one, assignment) for assignment in assignments]
            return [future.result() for future in futures]
