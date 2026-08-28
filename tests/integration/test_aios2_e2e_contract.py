from pathlib import Path

from runtime.aios2_adapter import AIOS2Adapter
from runtime.capabilities import CapabilityRegistry
from runtime.models import Task


def test_aios2_e2e_discover_bootstrap_run(tmp_path: Path):
    reg = CapabilityRegistry()
    adapter = AIOS2Adapter(tmp_path, reg)
    info = adapter.discover()
    assert info["adapter"] == "aios2"
    assert info["exists"] is True
    created = adapter.bootstrap()
    assert created
    result = adapter.run(
        [
            Task("boot", "bootstrap"),
            Task("work", "work", dependencies=["boot"]),
        ],
        executor=lambda _t: True,
        max_cycles=20,
    )
    assert "boot" in result.completed
    assert "work" in result.completed
    assert result.status in {"verified", "maintenance"}
