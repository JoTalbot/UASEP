from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .models import ProjectState, Task
from .planner import Planner
from .state import StateStore
from .supervisor import Supervisor


@dataclass(frozen=True, slots=True)
class RunResult:
    status: str
    iterations: int
    completed: tuple[str, ...]
    blockers: tuple[str, ...]


def run_project(root: Path, project_id: str, tasks: list[Task], max_cycles: int = 100) -> RunResult:
    """Host-neutral orchestration entry point; execution is intentionally supplied by the host."""
    state_store = StateStore(root)

    def unavailable_executor(task: Task) -> bool:
        # A launcher must never fabricate successful work when no host executor is wired.
        return False

    supervisor = Supervisor(state_store, Planner(), unavailable_executor)
    state: ProjectState = supervisor.run_until_blocked(project_id, tasks, max_cycles=max_cycles)
    return RunResult(
        state.phase,
        state.iteration,
        tuple(sorted(state.completed_tasks)),
        tuple(state.blockers),
    )
