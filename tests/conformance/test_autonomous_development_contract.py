from pathlib import Path

from runtime.development_contract import DevelopmentContract
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_contract_requires_verification_for_completion(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    contract = DevelopmentContract(tmp_path, "contract", host)

    blocked = contract.run(
        [Task(id="x", title="X")],
        max_cycles=1,
        acceptance=lambda task: [("acceptance", lambda: False)],
    )
    assert blocked.status == "blocked"
    assert blocked.completed == ()

    verified = contract.run(
        [Task(id="x", title="X")],
        max_cycles=1,
        acceptance=lambda task: [("acceptance", lambda: True)],
    )
    assert verified.completed == ("x",)
