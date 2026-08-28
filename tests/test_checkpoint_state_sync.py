from pathlib import Path

from runtime.checkpoint_store import CheckpointStore


def test_checkpoint_sequence_is_preserved_after_reload(tmp_path: Path):
    store = CheckpointStore(tmp_path)

    store.append(
        {
            "task_id": "sync-task",
            "phase": "EXECUTING",
        }
    )
    store.append(
        {
            "task_id": "sync-task",
            "phase": "VERIFYING",
        }
    )

    restored = CheckpointStore(tmp_path)
    entries = restored.load()

    assert len(entries) == 2
    assert entries[-1]["phase"] == "VERIFYING"
    assert entries[-1]["sequence"] == 2
