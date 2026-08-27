from pathlib import Path

from runtime.aios2_adapter import AIOS2Adapter
from runtime.capabilities import CapabilityRegistry
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task
from runtime.runner import run_project


def test_aios2_adapter_can_be_used_as_host_capability(tmp_path: Path):
    host = HostAdapter()
    registry = CapabilityRegistry.empty()
    registry.set("project.execute", True)
    adapter = AIOS2Adapter(tmp_path, registry)
    calls: list[str] = []

    def execute(task: Task) -> bool:
        calls.append(task.id)
        return True

    host.register(Capability("project.execute", available=True), execute)
    result = run_project(
        tmp_path,
        "aios2-e2e",
        [Task(id="bootstrap", title="Bootstrap AIOS2")],
        max_cycles=1,
        host=host,
        acceptance_provider=lambda task: [("adapter-contract", lambda: "project.execute" in adapter.capability_names())],
    )

    assert result.completed == ("bootstrap",)
    assert calls == ["bootstrap"]
