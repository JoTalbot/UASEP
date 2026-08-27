from pathlib import Path

from runtime.execution import ExecutionEngine
from runtime.project_bootstrap import bootstrap_project


def test_execution_captures_adapter_failure():
    result = ExecutionEngine().execute(lambda: 1 / 0)
    assert not result.success
    assert result.error and "ZeroDivisionError" in result.error


def test_bootstrap_is_non_destructive(tmp_path: Path):
    existing = tmp_path / ".uasep" / "state" / "PROJECT_STATE.md"
    existing.parent.mkdir(parents=True)
    existing.write_text("existing", encoding="utf-8")
    bootstrap_project(tmp_path, "demo")
    assert existing.read_text(encoding="utf-8") == "existing"
    assert (tmp_path / ".uasep" / "checkpoints").is_dir()
