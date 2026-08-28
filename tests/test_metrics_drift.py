from pathlib import Path

from runtime.drift import detect_version_drift
from runtime.metrics import Metrics


def test_metrics_snapshot():
    m = Metrics()
    m.record_start()
    m.record_verified()
    m.record_failed(retry=True)
    m.record_cycle()
    snap = m.snapshot()
    assert snap["tasks_started"] == 1
    assert snap["tasks_verified"] == 1
    assert snap["tasks_failed"] == 1
    assert snap["retries"] == 1
    assert snap["cycles"] == 1


def test_detect_version_aligned(tmp_path: Path):
    (tmp_path / "VERSION").write_text("3.1.2\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text('version = "3.1.2"\n', encoding="utf-8")
    assert detect_version_drift(tmp_path) == []


def test_detect_version_drift(tmp_path: Path):
    (tmp_path / "VERSION").write_text("3.1.1\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text('version = "3.1.2"\n', encoding="utf-8")
    findings = detect_version_drift(tmp_path)
    assert findings
