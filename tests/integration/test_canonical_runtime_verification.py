from pathlib import Path

from runtime.canonical_runtime import CanonicalRuntime
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_canonical_runtime_requires_acceptance_when_provider_is_supplied(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    runtime = CanonicalRuntime(tmp_path, "demo", host)

    failed = runtime.run(
        [Task(id="build", title="Build")],
        acceptance=lambda task: [("acceptance", lambda: False)],
    )
    assert failed.completed == ()
    assert failed.status == "blocked"

    passed = runtime.run(
        [Task(id="build", title="Build")],
        acceptance=lambda task: [("acceptance", lambda: True)],
    )
    assert passed.completed == ("build",)
