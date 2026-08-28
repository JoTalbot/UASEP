from pathlib import Path

import pytest

from runtime.checkpoint_store import CheckpointStore
from runtime.models import Task
from runtime.planner import Planner


def test_checkpoint_rejects_non_list_journal(tmp_path: Path):
    path = tmp_path / "checkpoint.json"
    path.write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="checkpoint journal must contain a list"):
        CheckpointStore(path).all()


def test_planner_rejects_duplicate_ids():
    tasks = [
        Task("same", "first", priority=10),
        Task("same", "second", priority=10),
    ]
    with pytest.raises(ValueError, match="task ids must be unique"):
        Planner().ready_tasks(tasks, set())
