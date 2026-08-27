from pathlib import Path

from runtime.approval_gate import ApprovalGate, ApprovalRequest
from runtime.checkpoints_v2 import CheckpointStore


def test_checkpoint_journal_restores_latest(tmp_path: Path):
    store = CheckpointStore(tmp_path / ".uasep" / "checkpoints" / "journal.json")
    store.save("task-a", "executing")
    store.save("task-a", "verified")
    assert store.latest()["phase"] == "verified"
    assert store.latest()["sequence"] == 2


def test_destructive_action_requires_approval():
    request = ApprovalRequest("delete-project", "irreversible", destructive=True)
    assert ApprovalGate().check(request) is False
    assert ApprovalGate({"delete-project"}).check(request) is True
    assert ApprovalGate().check(ApprovalRequest("write-file", "normal")) is True
