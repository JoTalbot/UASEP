from pathlib import Path

import pytest

from runtime.checkpoint_store import CheckpointStore
from runtime.task_graph import TaskGraph, TaskNode


def test_graph_rejects_cycle():
    with pytest.raises(ValueError):
        TaskGraph([
            TaskNode("a", "A", dependencies={"b"}),
            TaskNode("b", "B", dependencies={"a"}),
        ])


def test_checkpoint_rejects_empty_phase(tmp_path: Path):
    store = CheckpointStore(tmp_path / "checkpoints.json")

    with pytest.raises(ValueError):
        store.save("task-1", "")


def test_checkpoint_rejects_non_list_journal(tmp_path: Path):
    path = tmp_path / "checkpoints.json"
    path.write_text("{}", encoding="utf-8")
    store = CheckpointStore(path)

    with pytest.raises(ValueError):
        store.all()
