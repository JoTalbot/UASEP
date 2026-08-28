from runtime.models import Task, TaskStatus
from runtime.planner import Planner


def test_ready_tasks_are_sorted_by_priority_then_id() -> None:
    tasks = [
        Task(id="b", title="B", priority=10),
        Task(id="a", title="A", priority=10),
        Task(id="c", title="C", priority=20),
    ]

    ready = Planner().ready_tasks(tasks, set())

    assert [task.id for task in ready] == ["c", "a", "b"]


def test_ready_tasks_respect_dependencies_and_completed() -> None:
    tasks = [
        Task(id="base", title="Base", status=TaskStatus.DONE),
        Task(id="blocked", title="Blocked", dependencies=["missing"]),
        Task(id="ready", title="Ready", dependencies=["base"]),
    ]

    ready = Planner().ready_tasks(tasks, {"base"})

    assert [task.id for task in ready] == ["ready"]


def test_next_task_returns_none_when_nothing_is_ready() -> None:
    task = Task(id="blocked", title="Blocked", dependencies=["missing"])

    assert Planner().next_task([task], set()) is None
