import pytest

from runtime.task_graph import TaskGraph, TaskNode


def test_constructor_accepts_forward_references():
    graph = TaskGraph([
        TaskNode("B", "second", dependencies={"A"}),
        TaskNode("A", "first"),
    ])
    assert [task.id for task in graph.ready()] == ["A"]


def test_constructor_rejects_unknown_dependency():
    with pytest.raises(ValueError, match="unknown dependencies"):
        TaskGraph([TaskNode("B", "second", dependencies={"missing"})])


def test_constructor_rejects_cycle():
    with pytest.raises(ValueError, match="cycle"):
        TaskGraph([
            TaskNode("A", "first", dependencies={"B"}),
            TaskNode("B", "second", dependencies={"A"}),
        ])


def test_add_rejects_self_dependency():
    graph = TaskGraph()
    with pytest.raises(ValueError, match="self-dependency"):
        graph.add(TaskNode("A", "first", dependencies={"A"}))
