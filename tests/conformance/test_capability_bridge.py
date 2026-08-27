import pytest

from runtime.capability_bridge import CapabilityBridge
from runtime.host_adapter import HostAdapter


def test_bridge_registers_and_executes():
    bridge = CapabilityBridge(HostAdapter())
    bridge.register_handler("project.execute", lambda task: task.id)
    task = type("Task", (), {"id": "build"})()
    assert bridge.available("project.execute")
    assert bridge.execute("project.execute", task) == "build"


def test_bridge_preserves_approval_boundary():
    bridge = CapabilityBridge(HostAdapter())
    bridge.register_handler("delete", lambda: "deleted", requires_approval=True)
    with pytest.raises(PermissionError):
        bridge.execute("delete")
    assert bridge.execute("delete", approved=True) == "deleted"
