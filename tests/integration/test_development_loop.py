from pathlib import Path

from runtime.development_loop import DevelopmentLoop
from runtime.task_graph import TaskNode


def test_project_loop_runs_until_all_tasks_complete(tmp_path: Path):
    tasks = [TaskNode("a", "A"), TaskNode("b", "B", dependencies={"a"})]
    result = DevelopmentLoop(tmp_path, "demo").run(
        tasks,
        lambda task: True,
        lambda task: [("acceptance", lambda: True)],
    )
    assert result.status == "COMPLETE"
    assert result.completed == ("a", "b")


def test_project_loop_stops_on_failed_acceptance(tmp_path: Path):
    tasks = [TaskNode("a", "A")]
    result = DevelopmentLoop(tmp_path, "demo").run(
        tasks,
        lambda task: True,
        lambda task: [("acceptance", lambda: False)],
    )
    assert result.status == "FAILED"
    assert result.completed == ()
