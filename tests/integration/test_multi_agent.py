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
