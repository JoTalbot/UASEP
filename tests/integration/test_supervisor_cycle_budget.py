from pathlib import Path

import pytest

from runtime.supervisor import Supervisor


def test_run_until_blocked_rejects_zero_cycle_budget(tmp_path: Path) -> None:
    supervisor = Supervisor.with_project_runtime(tmp_path, lambda task: True)

    with pytest.raises(ValueError, match="max_cycles"):
        supervisor.run_until_blocked("demo", [], max_cycles=0)


def test_run_until_blocked_respects_cycle_budget(tmp_path: Path) -> None:
    supervisor = Supervisor.with_project_runtime(tmp_path, lambda task: False)
    tasks = []

    state = supervisor.run_until_blocked("demo", tasks, max_cycles=2)

    assert state.iteration == 1
    assert state.phase == "maintenance"


def test_run_until_blocked_marks_unresolved_retry_as_blocked(tmp_path: Path) -> None:
    from runtime.models import Task

    supervisor = Supervisor.with_project_runtime(tmp_path, lambda task: False)

    state = supervisor.run_until_blocked(
        "demo", [Task(id="build", title="Build")], max_cycles=1
    )

    assert state.phase == "blocked"
    assert state.current_task is None
    assert "cycle budget exhausted (1)" in state.blockers
