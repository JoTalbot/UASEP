from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .executor import HostExecutor
from .host_adapter import HostAdapter
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


def run_project(
    root: Path,
    project_id: str,
    tasks: list[Task],
    max_cycles: int = 100,
    host: HostAdapter | None = None,
) -> RunResult:
    """Run a project with an explicitly supplied host; absent execution remains blocked."""
    state_store = StateStore(root)
    adapter = host or HostAdapter()

    def executor(task: Task) -> bool:
        return HostExecutor(adapter)(task)

    supervisor = Supervisor(state_store, Planner(), executor)
    state: ProjectState = supervisor.run_until_blocked(project_id, tasks, max_cycles=max_cycles)
    return RunResult(
        state.phase,
        state.iteration,
        tuple(sorted(state.completed_tasks)),
        tuple(state.blockers),
    )
