from pathlib import Path

from runtime.bootstrap import bootstrap_project
from runtime.checkpoints import CheckpointManager
from runtime.recovery import RecoveryManager


def test_recovery_finds_latest_checkpoint(tmp_path: Path):
    bootstrap_project(tmp_path)
    manager = CheckpointManager(tmp_path / ".uasep" / "checkpoints")
    checkpoint = manager.create("active-task", {"task": "implement", "attempt": 1})
    result = RecoveryManager(tmp_path).recover()
    assert result.restored
    assert result.checkpoint == checkpoint.name
