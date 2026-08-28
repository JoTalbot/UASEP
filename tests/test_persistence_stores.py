from pathlib import Path

import pytest

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


def test_evidence_store_recovers_valid_tmp_after_interrupted_write(tmp_path: Path) -> None:
    path = tmp_path / "evidence.json"
    store = EvidenceStore(path)
    store.record(Evidence("execution", "task-a", "FAILED", "retry"))

    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        '[{"claim": "task-a", "detail": "recovered", "kind": "verification", "status": "VERIFIED", "timestamp": "2026-01-01T00:00:00+00:00"}]',
        encoding="utf-8",
    )
    path.unlink()

    assert store.all()[0]["detail"] == "recovered"
    assert path.exists()
    assert not tmp.exists()


def test_evidence_store_rejects_corrupt_tmp(tmp_path: Path) -> None:
    path = tmp_path / "evidence.json"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text("{broken", encoding="utf-8")

    store = EvidenceStore(path)

    assert store.all() == []
    assert tmp.exists()


def test_evidence_store_rejects_non_object_entries(tmp_path: Path) -> None:
    path = tmp_path / "evidence.json"
    path.write_text('["invalid"]', encoding="utf-8")

    with pytest.raises(ValueError, match="list of objects"):
        EvidenceStore(path).all()
