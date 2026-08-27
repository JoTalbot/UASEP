from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .models import ProjectState, Task
from .planner import Planner
from .state import StateStore


@dataclass
class Supervisor:
    """Persistent orchestration boundary for CLI, sandbox, or tool-connected hosts."""

    state_store: StateStore
    planner: Planner
    executor: Callable[[Task], bool]

    def run_once(self, project_id: str, tasks: list[Task]) -> ProjectState:
        state = self.state_store.load(project_id)
        state.iteration += 1
        task = self.planner.next_task(tasks, state.completed_tasks)
        if task is None:
            state.phase = "maintenance" if not state.blockers else "blocked"
            self.state_store.save(state)
            return state
        state.phase = "executing"
        state.current_task = task.id
        self.state_store.save(state)
        try:
            success = bool(self.executor(task))
        except Exception as exc:
            state.phase = "blocked"
            state.blockers.append(f"{task.id}: {type(exc).__name__}: {exc}")
            self.state_store.save(state)
            raise
        if success:
            state.completed_tasks.add(task.id)
            state.phase = "verified"
            state.current_task = None
        else:
            state.phase = "blocked"
            state.blockers.append(f"{task.id}: executor reported failure")
        self.state_store.save(state)
        return state

    def run_until_blocked(self, project_id: str, tasks: list[Task], max_cycles: int = 100) -> ProjectState:
        """Continue from persisted state until no work remains, a blocker occurs, or budget is exhausted."""
        state = self.state_store.load(project_id)
        for _ in range(max_cycles):
            state = self.run_once(project_id, tasks)
            if state.phase in {"blocked", "maintenance"}:
                return state
        state.phase = "maintenance"
        self.state_store.save(state)
        return state
