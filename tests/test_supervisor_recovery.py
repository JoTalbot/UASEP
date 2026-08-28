from pathlib import Path

from runtime.models import Task, TaskStatus
from runtime.supervisor import Supervisor
from runtime.state import StateStore


def test_failure_count_survives_cold_resume(tmp_path: Path):
    def fail_executor(_task):
        return False

    supervisor = Supervisor.with_project_runtime(
        tmp_path,
        executor=fail_executor,
        max_failures=3,
    )

    task = Task(id="recovery-task", title="simulate failure")
    supervisor.run_once("demo", [task])

    state = StateStore(tmp_path).load("demo")

    assert state.task_failures["recovery-task"] == 1
    assert task.status == TaskStatus.FAILED


def test_runtime_can_restore_persisted_failure_budget(tmp_path: Path):
    def fail_executor(_task):
        return False

    first = Supervisor.with_project_runtime(
        tmp_path,
        executor=fail_executor,
        max_failures=3,
    )
    task = Task(id="cold-resume", title="persist failure")
    first.run_once("demo", [task])

    second = Supervisor.with_project_runtime(
        tmp_path,
        executor=fail_executor,
        max_failures=3,
    )
    restored = Task(id="cold-resume", title="persist failure")
    second.run_once("demo", [restored])

    state = StateStore(tmp_path).load("demo")
    assert state.task_failures["cold-resume"] == 2
