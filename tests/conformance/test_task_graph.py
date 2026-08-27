from runtime.task_graph import TaskGraph, TaskNode


def test_dependencies_gate_tasks():
    graph = TaskGraph([TaskNode("a", "A", priority=1)])
    graph.add(TaskNode("b", "B", priority=10, dependencies={"a"}))
    assert [task.id for task in graph.ready()] == ["a"]
    graph.mark_done("a")
    assert [task.id for task in graph.ready()] == ["b"]


def test_unknown_dependency_rejected():
    graph = TaskGraph()
    try:
        graph.add(TaskNode("x", "X", dependencies={"missing"}))
    except ValueError:
        pass
    else:
        raise AssertionError("unknown dependency must be rejected")
