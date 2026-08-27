from pathlib import Path

from runtime.autonomous_loop import AutonomousLoop
from runtime.checkpoint_store import CheckpointStore
from runtime.task_graph import TaskGraph, TaskNode


def test_full_cycle_records_evidence_and_checkpoint(tmp_path: Path):
    graph = TaskGraph([TaskNode("spec", "Specification"), TaskNode("build", "Build", dependencies={"spec"})])
    loop = AutonomousLoop(tmp_path, "demo", graph)
    for _ in range(2):
        result = loop.run_once(lambda task: True, lambda task: [("acceptance", lambda: True)])
        assert result.status == "VERIFIED"
    assert len(graph.completed()) == 2
    assert len(CheckpointStore(tmp_path / ".uasep" / "checkpoints" / "journal.json").all()) >= 4


def test_resume_uses_project_local_state(tmp_path: Path):
    graph = TaskGraph([TaskNode("a", "A"), TaskNode("b", "B", dependencies={"a"})])
    loop = AutonomousLoop(tmp_path, "demo", graph)
    assert loop.run_once(lambda task: True, lambda task: [("acceptance", lambda: True)]).status == "VERIFIED"
    assert loop.state_store.load("demo").completed_tasks == {"a"}
    assert loop.run_once(lambda task: True, lambda task: [("acceptance", lambda: True)]).task_id == "b"
