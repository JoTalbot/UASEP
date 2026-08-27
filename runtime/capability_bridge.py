from __future__ import annotations

from typing import Any, Callable

from .host_adapter import Capability, HostAdapter


class CapabilityBridge:
    """Bridge legacy CapabilityRegistry-style hosts into the canonical HostAdapter boundary."""

    def __init__(self, host: HostAdapter) -> None:
        self.host = host

    def register_handler(self, name: str, handler: Callable[..., Any], *, requires_approval: bool = False) -> None:
        self.host.register(Capability(name, available=True, requires_approval=requires_approval), handler)

    def available(self, name: str) -> bool:
        return self.host.can(name)

    def execute(self, name: str, *args: Any, approved: bool = False, **kwargs: Any) -> Any:
        return self.host.request(name, *args, approved=approved, **kwargs)
