from pathlib import Path

from runtime.checkpoint_store import CheckpointStore


def test_checkpoint_tmp_recovery_path_exists(tmp_path: Path):
    store = CheckpointStore(tmp_path)

    checkpoint = {
        "sequence": 1,
        "phase": "RUNNING",
        "task": "recovery-test",
    }

    store.append(checkpoint)

    assert store.latest()["sequence"] == 1


def test_checkpoint_history_remains_after_reload(tmp_path: Path):
    first = CheckpointStore(tmp_path)
    first.append({"sequence": 1, "phase": "PLANNED"})

    second = CheckpointStore(tmp_path)

    assert second.latest()["phase"] == "PLANNED"
