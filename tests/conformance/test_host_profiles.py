from runtime.host_adapter import Capability, HostAdapter
from runtime.host_profiles import HostProfile, apply_profile


def test_profile_does_not_fabricate_capabilities():
    host = HostAdapter()
    host.register(Capability("git", available=False))
    apply_profile(host, HostProfile("local", ("git", "shell")))
    assert not host.can("git")
    assert not host.can("shell")
