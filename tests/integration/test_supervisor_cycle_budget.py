from pathlib import Path

import pytest

from runtime.planner import Planner
from runtime.state import StateStore
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
