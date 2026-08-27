from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from .executor import HostExecutor
from .host_adapter import HostAdapter
from .models import ProjectState, Task
from .planner import Planner
from .state import StateStore
from .supervisor import Supervisor


AcceptanceProvider = Callable[[Task], Iterable[tuple[str, Callable[[], bool]]]]


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
    *,
    host: HostAdapter | None = None,
    executor: Callable[[Task], bool] | None = None,
    acceptance_provider: AcceptanceProvider | None = None,
) -> RunResult:
    """Canonical project orchestration with persistent verification/evidence/checkpoints."""
    adapter = host or HostAdapter()
    task_executor = executor or HostExecutor(adapter)
    supervisor = Supervisor.with_project_runtime(
        root,
        task_executor,
        planner=Planner(),
        acceptance_provider=acceptance_provider,
    )
    state: ProjectState = supervisor.run_until_blocked(project_id, tasks, max_cycles=max_cycles)
    return RunResult(
        state.phase,
        state.iteration,
        tuple(sorted(state.completed_tasks)),
        tuple(state.blockers),
    )
