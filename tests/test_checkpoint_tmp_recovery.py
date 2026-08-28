from pathlib import Path

from runtime.checkpoint_store import CheckpointStore


def test_tmp_checkpoint_recovery_artifact_exists(tmp_path: Path):
    checkpoint = tmp_path / "checkpoint.json"
    temp_checkpoint = tmp_path / "checkpoint.json.tmp"

    temp_checkpoint.write_text('{"sequence": 1}', encoding="utf-8")

    assert temp_checkpoint.exists()
    assert not checkpoint.exists()


def test_checkpoint_store_can_restore_from_tmp(tmp_path: Path):
    checkpoint = tmp_path / "checkpoint.json"
    temp_checkpoint = tmp_path / "checkpoint.json.tmp"

    store = CheckpointStore(checkpoint)
    store.save("recovery-task", "RUNNING")

    checkpoint.replace(temp_checkpoint)

    assert not checkpoint.exists()
    assert temp_checkpoint.exists()

    assert store.recover() is True
    assert checkpoint.exists()
    assert store.latest()["phase"] == "RUNNING"


def test_checkpoint_store_rejects_corrupted_tmp_checksum(tmp_path: Path):
    checkpoint = tmp_path / "checkpoint.json"
    temp_checkpoint = tmp_path / "checkpoint.json.tmp"

    store = CheckpointStore(checkpoint)
    store.save("checksum-task", "VERIFYING")

    checkpoint.replace(temp_checkpoint)
    content = temp_checkpoint.read_text(encoding="utf-8")
    temp_checkpoint.write_text(content.replace("VERIFYING", "BROKEN"), encoding="utf-8")

    assert store.recover() is False
    assert not checkpoint.exists()
