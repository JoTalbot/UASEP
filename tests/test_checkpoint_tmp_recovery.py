from pathlib import Path


def test_tmp_checkpoint_recovery_artifact_exists(tmp_path: Path):
    checkpoint = tmp_path / "checkpoint.json"
    temp_checkpoint = tmp_path / "checkpoint.json.tmp"

    temp_checkpoint.write_text('{"sequence": 1}', encoding="utf-8")

    assert temp_checkpoint.exists()
    assert not checkpoint.exists()
