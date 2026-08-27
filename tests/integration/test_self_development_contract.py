from pathlib import Path

from runtime.development_contract import DevelopmentContract
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_uasep_can_apply_its_own_development_contract(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    contract = DevelopmentContract(tmp_path, "uasep-self", host)

    result = contract.run(
        [
            Task(id="inspect", title="Inspect UASEP"),
            Task(id="validate", title="Validate UASEP", dependencies=["inspect"]),
            Task(id="checkpoint", title="Persist validated progress", dependencies=["validate"]),
        ],
        max_cycles=10,
        acceptance=lambda task: [(f"verified:{task.id}", lambda: True)],
    )

    assert result.completed == ("checkpoint", "inspect", "validate")
    assert (tmp_path / ".uasep" / "manifest.yaml").exists()
