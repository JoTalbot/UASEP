from pathlib import Path

from runtime.checkpoint_store import CheckpointStore
from runtime.evidence_store import Evidence, EvidenceStore


def test_checkpoint_store_is_append_only_and_recovers_latest(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoints.json")

    first = store.save("task-a", "executing")
    second = store.save("task-a", "verified")

    assert first.sequence == 1
    assert second.sequence == 2
    assert store.latest() == {
        "sequence": 2,
        "task_id": "task-a",
        "phase": "verified",
        "timestamp": second.timestamp,
    }
    assert len(store.all()) == 2


def test_evidence_store_preserves_order_and_status(tmp_path: Path) -> None:
    store = EvidenceStore(tmp_path / "evidence.json")

    store.record(Evidence("execution", "task-a", "FAILED", "retry"))
    store.record(Evidence("verification", "task-a", "VERIFIED", "tests passed"))

    entries = store.all()
    assert [entry["kind"] for entry in entries] == ["execution", "verification"]
    assert [entry["status"] for entry in entries] == ["FAILED", "VERIFIED"]
