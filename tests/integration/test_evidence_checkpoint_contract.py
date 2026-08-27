from pathlib import Path

from runtime.runner import run_project
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_verified_task_produces_evidence_and_checkpoint(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    result = run_project(
        tmp_path,
        "demo",
        [Task(id="build", title="Build")],
        max_cycles=1,
        host=host,
        acceptance_provider=lambda task: [("acceptance", lambda: True)],
    )
    assert result.status == "verified"
    assert (tmp_path / ".uasep" / "evidence" / "runtime.json").exists()
    assert (tmp_path / ".uasep" / "checkpoints" / "journal.json").exists()


def test_failed_acceptance_never_marks_task_complete(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    result = run_project(
        tmp_path,
        "demo",
        [Task(id="build", title="Build")],
        max_cycles=1,
        host=host,
        acceptance_provider=lambda task: [("acceptance", lambda: False)],
    )
    assert result.status == "blocked"
    assert result.completed == ()
