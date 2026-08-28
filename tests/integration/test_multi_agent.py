from runtime.models import Task, TaskStatus
from runtime.multi_agent import MultiAgentCoordinator


def test_assign_ready_tasks_to_free_agents():
    coord = MultiAgentCoordinator()
    coord.register("a1", "developer")
    coord.register("a2", "tester")
    tasks = [Task("t1", "one"), Task("t2", "two"), Task("t3", "three")]
    assigned = coord.assign(tasks)
    assert len(assigned) == 2
    assert assigned[0][0].name == "a1"
    assert assigned[0][1].id == "t1"
    assert assigned[0][1].status == TaskStatus.IN_PROGRESS


def test_run_parallel_releases_agents():
    coord = MultiAgentCoordinator()
    coord.register("w1")
    results = coord.run_parallel(
        [Task("x", "work")],
        execute=lambda _t: True,
    )
    assert results == [("w1", "x", True)]
    assert coord.free_agents()[0].name == "w1"


def test_write_set_conflicts():
    a = Task("a", "A", write_set=["src/a.py"])
    b = Task("b", "B", write_set=["src/a.py", "src/b.py"])
    c = Task("c", "C", write_set=["src/c.py"])
    assert MultiAgentCoordinator.conflicts(a, b) is True
    assert MultiAgentCoordinator.conflicts(a, c) is False
    assert MultiAgentCoordinator.conflicts(a, Task("d", "D")) is False


def test_filter_compatible_skips_overlapping_writes():
    coord = MultiAgentCoordinator()
    coord.register("w1")
    coord.register("w2")
    ready = [
        Task("a", "A", write_set=["f1"]),
        Task("b", "B", write_set=["f1"]),
        Task("c", "C", write_set=["f2"]),
    ]
    selected = coord.filter_compatible(ready)
    assert [t.id for t in selected] == ["a", "c"]
    assigned = coord.assign(ready)
    assert len(assigned) == 2
    assert {t.id for _, t in assigned} == {"a", "c"}
