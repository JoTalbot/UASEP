import pytest

from runtime.host_adapter import Capability, HostAdapter


def test_host_adapter_discovers_and_executes_capability():
    host = HostAdapter()
    host.register(Capability("echo", available=True), lambda value: value)
    assert host.can("echo")
    assert host.request("echo", "ok") == "ok"


def test_unavailable_capability_is_not_fabricated():
    host = HostAdapter()
    host.register(Capability("shell", available=False))
    assert not host.can("shell")
    with pytest.raises(RuntimeError, match="capability unavailable"):
        host.request("shell")


def test_approval_is_enforced_at_capability_boundary():
    host = HostAdapter()
    host.register(Capability("delete", available=True, requires_approval=True), lambda: "deleted")
    with pytest.raises(PermissionError, match="approval required"):
        host.request("delete")
    assert host.request("delete", approved=True) == "deleted"
