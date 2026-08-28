from pathlib import Path

from runtime.models import Task, TaskStatus
from runtime.supervisor import Supervisor


def test_supervisor_retries_failed_execution(tmp_path: Path):
    attempts = {"count": 0}

    def execute(_task: Task) -> bool:
        attempts["count"] += 1
        return attempts["count"] == 2

    supervisor = Supervisor.with_project_runtime(
        tmp_path,
        execute,
        max_failures=3,
    )
    task = Task("build", "Build")

    first = supervisor.run_once("demo", [task])
    assert first.phase == "retrying"
    assert task.status == TaskStatus.FAILED
    assert task.failure_count == 1

    second = supervisor.run_once("demo", [task])
    assert second.phase == "verified"
    assert task.status == TaskStatus.DONE
    assert task.failure_count == 1
    assert attempts["count"] == 2


def test_supervisor_blocks_after_retry_budget(tmp_path: Path):
    supervisor = Supervisor.with_project_runtime(
        tmp_path,
        lambda _task: False,
        max_failures=2,
    )
    task = Task("build", "Build")

    first = supervisor.run_once("demo", [task])
    second = supervisor.run_once("demo", [task])

    assert first.phase == "retrying"
    assert second.phase == "blocked"
    assert task.status == TaskStatus.BLOCKED
    assert task.failure_count == 2
