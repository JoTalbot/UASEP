from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(slots=True)
class Capability:
    name: str
    available: bool = False
    requires_approval: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


class HostAdapter:
    """Host-neutral capability boundary. UASEP can discover and request capabilities without assuming them."""

    def __init__(self) -> None:
        self._capabilities: dict[str, Capability] = {}
        self._handlers: dict[str, Callable[..., Any]] = {}

    def register(self, capability: Capability, handler: Callable[..., Any] | None = None) -> None:
        self._capabilities[capability.name] = capability
        if handler is not None:
            self._handlers[capability.name] = handler

    def discover(self) -> dict[str, Capability]:
        return dict(self._capabilities)

    def can(self, name: str) -> bool:
        capability = self._capabilities.get(name)
        return capability is not None and capability.available

    def request(self, name: str, *args: Any, approved: bool = False, **kwargs: Any) -> Any:
        capability = self._capabilities.get(name)
        if capability is None or not capability.available:
            raise RuntimeError(f"capability unavailable: {name}")
        if capability.requires_approval and not approved:
            raise PermissionError(f"approval required: {name}")
        handler = self._handlers.get(name)
        if handler is None:
            raise RuntimeError(f"capability has no handler: {name}")
        return handler(*args, **kwargs)
