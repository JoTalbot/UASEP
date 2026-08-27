from pathlib import Path

from runtime.final_bootstrap import bootstrap


def test_bootstrap_creates_new_project_scaffold(tmp_path: Path):
    result = bootstrap(tmp_path)
    assert result.existing is False
    assert result.manifest.exists()


def test_bootstrap_is_idempotent_for_existing_project(tmp_path: Path):
    first = bootstrap(tmp_path)
    second = bootstrap(tmp_path)
    assert first.existing is False
    assert second.existing is True
    assert first.manifest == second.manifest
