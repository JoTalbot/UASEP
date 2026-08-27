from pathlib import Path

from runtime.canonical_runtime import CanonicalRuntime
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_canonical_runtime_uses_host_execution(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    runtime = CanonicalRuntime(tmp_path, "demo", host)
    result = runtime.run([Task(id="build", title="Build")], max_cycles=1)
    assert result.completed == ("build",)
