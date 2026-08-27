from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Checkpoint:
    sequence: int
    task_id: str | None
    phase: str
    timestamp: str


class CheckpointStore:
    """Append-only checkpoint journal for interruption-safe development."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def save(self, task_id: str | None, phase: str) -> Checkpoint:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        entries = self.all()
        checkpoint = Checkpoint(len(entries) + 1, task_id, phase, datetime.now(timezone.utc).isoformat())
        entries.append(checkpoint.__dict__)
        self.path.write_text(json.dumps(entries, indent=2), encoding="utf-8")
        return checkpoint

    def all(self) -> list[dict]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def latest(self) -> dict | None:
        entries = self.all()
        return entries[-1] if entries else None
