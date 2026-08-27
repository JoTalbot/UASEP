from pathlib import Path

from runtime.development_contract import DevelopmentContract
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_development_contract_bootstraps_and_runs(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    contract = DevelopmentContract(tmp_path, "demo", host)
    result = contract.run(
        [Task(id="build", title="Build")],
        max_cycles=1,
        acceptance=lambda task: [("acceptance", lambda: True)],
    )
    assert result.completed == ("build",)
    assert (tmp_path / ".uasep" / "manifest.yaml").exists()
