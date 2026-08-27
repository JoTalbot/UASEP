from pathlib import Path

from runtime.supervisor_engine import Supervisor
from runtime.task_graph import TaskGraph, TaskNode


def test_supervisor_executes_ready_tasks(tmp_path: Path):
    graph = TaskGraph([TaskNode("a", "A", priority=1), TaskNode("b", "B", dependencies={"a"})])
    supervisor = Supervisor(tmp_path, graph)
    result = supervisor.run(lambda task: True)
    assert result.completed == ["a", "b"]
    assert result.blocked == []


def test_supervisor_records_failure(tmp_path: Path):
    graph = TaskGraph([TaskNode("a", "A")])
    supervisor = Supervisor(tmp_path, graph)
    result = supervisor.run(lambda task: False, max_iterations=1)
    assert result.completed == []
    assert result.blocked == ["a"]
    assert supervisor.evidence.all()[0]["status"] == "FAILED"
