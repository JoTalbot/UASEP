from pathlib import Path

from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task
from runtime.runner import run_project


def test_runner_uses_registered_host_executor(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    result = run_project(tmp_path, "demo", [Task(id="build", title="Build")], max_cycles=1, host=host)
    assert result.completed == ("build",)
    assert result.status == "verified"
