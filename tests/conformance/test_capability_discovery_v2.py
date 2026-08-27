from pathlib import Path

import pytest

from runtime.discovery import discover_capabilities, discover_project_root, discover_uasep


def test_discovery_reports_provenance_and_policy(tmp_path: Path):
    capabilities = {item.name: item for item in discover_capabilities(tmp_path)}
    assert capabilities["read_files"].discovered is True
    assert capabilities["read_files"].source == "filesystem"
    assert capabilities["network"].available is False
    assert capabilities["network"].source == "host-policy"


def test_project_root_must_be_directory(tmp_path: Path):
    file = tmp_path / "file"
    file.write_text("x", encoding="utf-8")
    with pytest.raises(ValueError):
        discover_project_root(file)


def test_uasep_state_is_distinguished(tmp_path: Path):
    before = discover_uasep(tmp_path)
    assert before["installed"] is False
    (tmp_path / ".uasep").mkdir()
    (tmp_path / ".uasep" / "manifest.yaml").write_text("version: 1\n", encoding="utf-8")
    after = discover_uasep(tmp_path)
    assert after["installed"] is True
    assert after["state_exists"] is True
