from __future__ import annotations

from dataclasses import dataclass, field

from .models import Capability


DEFAULT_CAPABILITIES = (
    "read_files",
    "write_files",
    "execute_shell",
    "git",
    "network",
    "web",
    "github",
    "containers",
)


@dataclass
class CapabilityRegistry:
    capabilities: dict[str, Capability] = field(default_factory=dict)

    @classmethod
    def empty(cls) -> "CapabilityRegistry":
        return cls({name: Capability(name=name, available=False) for name in DEFAULT_CAPABILITIES})

    def set(self, name: str, available: bool, notes: str = "") -> None:
        self.capabilities[name] = Capability(name, available, notes)

    def has(self, name: str) -> bool:
        return self.capabilities.get(name, Capability(name, False)).available

    def snapshot(self) -> dict[str, dict[str, str | bool]]:
        return {
            name: {"available": cap.available, "notes": cap.notes}
            for name, cap in sorted(self.capabilities.items())
        }
