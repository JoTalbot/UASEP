from pathlib import Path

from runtime.launcher import launch


def test_bootstrap_is_idempotent(tmp_path: Path):
    first = launch(tmp_path)
    second = launch(tmp_path)
    assert first["project"] == second["project"]
    assert (tmp_path / ".uasep").is_dir()
    assert second["created"] == []
