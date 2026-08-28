from pathlib import Path

import pytest

from runtime.models import Task, TaskStatus
from runtime.planner import Planner
from runtime.supervisor import Supervisor
from runtime.task_graph import TaskGraph, TaskNode


def test_planner_deterministic_tie_break():
    tasks = [
        Task("b", "B", priority=10),
        Task("a", "A", priority=10),
    ]
    assert Planner().next_task(tasks, set()).id == "a"


def test_task_retries_are_bounded():
    task = Task("x", "X", status=TaskStatus.FAILED, max_attempts=2, attempts=1)
    assert task.is_ready(set())
    task.attempts += 1
    assert not task.is_ready(set())


def test_task_graph_rejects_invalid_dependencies():
    graph = TaskGraph()
    with pytest.raises(ValueError):
        graph.add(TaskNode("x", "X", dependencies={"missing"}))


def test_task_graph_rejects_self_dependency():
    graph = TaskGraph()
    with pytest.raises(ValueError):
        graph.add(TaskNode("x", "X", dependencies={"x"}))


def test_supervisor_retry_then_success(tmp_path: Path):
    calls = []

    def execute(task: Task) -> bool:
        calls.append(task.id)
        return len(calls) == 2

    supervisor = Supervisor.with_project_runtime(tmp_path, execute)
    task = Task("x", "X", max_attempts=2)

    first = supervisor.run_once("demo", [task])
    assert first.phase == "blocked"
    assert first.current_task == "x"
    assert task.attempts == 1

    second = supervisor.run_once("demo", [task])
    assert second.phase == "verified"
    assert second.completed_tasks == {"x"}
    assert task.attempts == 2
