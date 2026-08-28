from runtime.graph import TaskGraph
from runtime.models import Task, TaskStatus


def test_dependencies_gate_and_priority():
    graph = TaskGraph(
        [
            Task(id="a", objective="A", priority=1),
            Task(id="b", objective="B", priority=10, dependencies=["a"]),
        ]
    )
    assert [t.id for t in graph.ready()] == ["a"]
    graph.apply("a", TaskStatus.VERIFIED)
    assert [t.id for t in graph.ready()] == ["b"]


def test_unknown_dependency_rejected():
    try:
        TaskGraph([Task(id="x", objective="X", dependencies=["missing"])])
    except ValueError:
        return
    raise AssertionError("unknown dependency must be rejected")


def test_self_dependency_rejected():
    try:
        TaskGraph([Task(id="x", objective="X", dependencies=["x"])])
    except ValueError:
        return
    raise AssertionError("self-dependency must be rejected")


def test_cycle_rejected_on_add():
    graph = TaskGraph([Task(id="a", objective="A")])
    graph.add(Task(id="b", objective="B", dependencies=["a"]))
    try:
        # creating a cycle a<-b<-a by mutating is not allowed via add of c;
        # add edge back by replacing is not supported; add node that closes cycle:
        graph.tasks["a"].dependencies.append("b")
        graph.validate()
    except ValueError:
        return
    raise AssertionError("cycle must be rejected")
