from pathlib import Path

from runtime.aios2_adapter import ProjectAdapter
from runtime.approval_gate import ApprovalGate, ApprovalRequest
from runtime.autonomous_loop import AutonomousLoop
from runtime.checkpoint_store import CheckpointStore
from runtime.retry_policy import RetryPolicy
from runtime.task_graph import TaskGraph, TaskNode
from runtime.verification import VerificationEngine


def test_conformance_project_adapter_bootstraps(tmp_path: Path):
    adapter = ProjectAdapter(tmp_path, "demo")
    assert adapter.discover()["project_id"] == "demo"
    assert adapter.bootstrap().is_dir()


def test_conformance_verification_is_explicit():
    assert VerificationEngine().verify([]).status == "VERIFIED"
    assert VerificationEngine().verify([("acceptance", lambda: False)]).status == "FAILED"


def test_conformance_approval_boundary():
    request = ApprovalRequest("delete", "irreversible", destructive=True)
    assert ApprovalGate().check(request) is False
    assert ApprovalGate({"delete"}).check(request) is True


def test_conformance_retry_changes_strategy():
    policy = RetryPolicy(3)
    assert policy.decide("x", 0, "a").retry
    assert not policy.decide("x", 1, "a").retry
    assert policy.decide("x", 1, "b").retry


def test_conformance_checkpoint_is_append_only(tmp_path: Path):
    store = CheckpointStore(tmp_path / "journal.json")
    store.save("x", "executing")
    store.save("x", "verified")
    assert [x["sequence"] for x in store.all()] == [1, 2]


def test_conformance_autonomous_loop_completes(tmp_path: Path):
    graph = TaskGraph([TaskNode("x", "X")])
    result = AutonomousLoop(tmp_path, "demo", graph).run_once(
        lambda task: True,
        lambda task: [("acceptance", lambda: True)],
    )
    assert result.status == "VERIFIED"
