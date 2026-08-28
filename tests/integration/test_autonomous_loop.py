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


def test_failed_execution_persists_recovery_state(tmp_path: Path):
    graph = TaskGraph([TaskNode("build", "Build")])
    loop = AutonomousLoop(tmp_path, "demo", graph)
    result = loop.run_once(lambda task: False, lambda task: [])

    state = loop.state_store.load("demo")
    assert result.status == "FAILED"
    assert state.phase == "blocked"
    assert state.current_task == "build"
    assert state.iteration == 1


def test_approval_rejection_persists_blocked_state(tmp_path: Path):
    graph = TaskGraph([TaskNode("build", "Build")])
    loop = AutonomousLoop(tmp_path, "demo", graph)
    result = loop.run_once(
        lambda task: True,
        lambda task: [],
        approval=lambda request: False,
    )

    state = loop.state_store.load("demo")
    assert result.status == "BLOCKED"
    assert result.reason == "approval required"
    assert state.phase == "blocked"
    assert state.current_task == "build"
