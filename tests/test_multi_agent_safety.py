import threading

import pytest

from runtime.models import Task
from runtime.multi_agent import MultiAgentCoordinator


def test_duplicate_agent_names_are_rejected():
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-1")
    with pytest.raises(ValueError, match="already registered"):
        coordinator.register("agent-1")


def test_write_set_conflict_allows_only_one_task():
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-1")
    coordinator.register("agent-2")
    first = Task("A", "first", write_set=["src/a.py"])
    second = Task("B", "second", write_set=["src/a.py"])

    results = coordinator.run_parallel([first, second], lambda task: True)

    assert results == [("agent-1", "A", True)]


def test_compatible_tasks_execute_concurrently():
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-1")
    coordinator.register("agent-2")
    started = threading.Barrier(2)

    def execute(task):
        started.wait(timeout=2)
        return True

    tasks = [Task("A", "first", write_set=["src/a.py"]), Task("B", "second", write_set=["src/b.py"])]
    results = coordinator.run_parallel(tasks, execute)

    assert results == [("agent-1", "A", True), ("agent-2", "B", True)]


def test_executor_exception_releases_agent_and_reports_failure():
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-1")

    results = coordinator.run_parallel([Task("A", "boom")], lambda task: 1 / 0)

    assert results == [("agent-1", "A", False)]
    assert coordinator.free_agents()[0].current_task is None
    assert not coordinator.free_agents()[0].busy


def test_unknown_agent_release_is_rejected():
    with pytest.raises(ValueError, match="unknown agent"):
        MultiAgentCoordinator().release("missing")
