from pathlib import Path

from runtime.models import Task
from runtime.runner import run_project


def test_project_runner_persists_blocked_state_when_executor_is_unavailable(tmp_path: Path):
    tasks = [Task(id="build", title="Build project", status="pending")]
    result = run_project(tmp_path, "demo", tasks, max_cycles=1)
    assert result.status in {"blocked", "BLOCKED"}
    assert "build" not in result.completed


def test_runner_respects_cycle_budget(tmp_path: Path):
    tasks = [Task(id="a", title="A", status="pending")]
    result = run_project(tmp_path, "demo", tasks, max_cycles=1)
    assert result.iterations <= 1
