from pathlib import Path

from runtime.autonomous_loop import AutonomousLoop
from runtime.task_graph import TaskGraph, TaskNode


def test_autonomous_loop_executes_and_verifies(tmp_path: Path):
    graph = TaskGraph([TaskNode("build", "Build", priority=10)])
    loop = AutonomousLoop(tmp_path, "demo", graph)
    result = loop.run_once(lambda task: True, lambda task: [("acceptance", lambda: True)])
    assert result.status == "VERIFIED"
    assert result.task_id == "build"
    assert loop.state_store.load("demo").completed_tasks == {"build"}


def test_failed_verification_is_not_completion(tmp_path: Path):
    graph = TaskGraph([TaskNode("build", "Build")])
    loop = AutonomousLoop(tmp_path, "demo", graph)
    result = loop.run_once(lambda task: True, lambda task: [("tests", lambda: False)])
    assert result.status == "FAILED"
    assert graph.tasks["build"].status != "done"
