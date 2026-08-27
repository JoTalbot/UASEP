from __future__ import annotations

from dataclasses import dataclass

from .host_adapter import HostAdapter


@dataclass(frozen=True, slots=True)
class HostProfile:
    name: str
    capabilities: tuple[str, ...]


def apply_profile(adapter: HostAdapter, profile: HostProfile) -> None:
    """Register known capability names as available only when handlers are supplied by the host."""
    for name in profile.capabilities:
        if adapter.can(name):
            continue
