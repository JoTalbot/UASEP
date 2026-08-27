import pytest

from runtime.executor import HostExecutor
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_host_executor_uses_registered_host_capability():
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: task.id == "build")
    assert HostExecutor(host)(Task("build", "Build")) is True


def test_host_executor_refuses_missing_capability():
    host = HostAdapter()
    with pytest.raises(RuntimeError, match="capability unavailable"):
        HostExecutor(host)(Task("build", "Build"))
