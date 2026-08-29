"""Runtime configuration layer."""

from dataclasses import dataclass


@dataclass
class RuntimeConfig:
    name: str = "UASEP"
    environment: str = "development"
