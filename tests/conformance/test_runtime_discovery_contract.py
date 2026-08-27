from pathlib import Path


def test_existing_uasep_state_is_detectable(tmp_path: Path):
    state = tmp_path / ".uasep"
    state.mkdir()
    (state / "manifest.yaml").write_text("version: 1\n", encoding="utf-8")
    assert (tmp_path / ".uasep" / "manifest.yaml").exists()


def test_missing_state_is_distinguishable_from_existing_state(tmp_path: Path):
    assert not (tmp_path / ".uasep" / "manifest.yaml").exists()
