from pathlib import Path

from runtime.launcher import launch


def test_launcher_bootstraps_project_without_overwriting(tmp_path: Path):
    marker = tmp_path / "README.md"
    marker.write_text("keep", encoding="utf-8")
    result = launch(tmp_path)
    assert result["project"] == tmp_path.name
    assert (tmp_path / ".uasep" / "state" / "PROJECT_STATE.md").exists()
    assert marker.read_text(encoding="utf-8") == "keep"
