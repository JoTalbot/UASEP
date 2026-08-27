from pathlib import Path

from runtime.aios2_adapter import AIOS2Adapter
from runtime.capabilities import CapabilityRegistry


def test_aios2_adapter_discovers_host(tmp_path: Path):
    adapter = AIOS2Adapter(tmp_path, CapabilityRegistry())
    info = adapter.discover()
    assert info["project_id"] == tmp_path.name
    assert info["exists"] is True


def test_aios2_adapter_bootstraps_uasep(tmp_path: Path):
    adapter = AIOS2Adapter(tmp_path, CapabilityRegistry())
    created = adapter.bootstrap()
    assert created
    assert all(path.exists() for path in created)
