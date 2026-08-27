from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .checkpoints import CheckpointManager


@dataclass(frozen=True, slots=True)
class RecoveryResult:
    restored: bool
    checkpoint: str | None = None


class RecoveryManager:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.checkpoints = CheckpointManager(root / ".uasep" / "checkpoints")

    def recover(self) -> RecoveryResult:
        latest = self.checkpoints.latest()
        if latest is None:
            return RecoveryResult(False)
        return RecoveryResult(True, latest.name)
