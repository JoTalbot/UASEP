from __future__ import annotations

from dataclasses import asdict, dataclass
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
        if not phase:
            raise ValueError("checkpoint phase must not be empty")

        entries = self.all()
        checkpoint = Checkpoint(
            len(entries) + 1,
            task_id,
            phase,
            datetime.now(timezone.utc).isoformat(),
        )
        entries.append(asdict(checkpoint))
        self._write(entries)
        return checkpoint

    def _write(self, entries: list[dict]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(json.dumps(entries, indent=2), encoding="utf-8")
        temporary.replace(self.path)

    def all(self) -> list[dict]:
        if not self.path.exists():
            return []
        entries = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(entries, list):
            raise ValueError("checkpoint journal must contain a list")
        return entries

    def latest(self) -> dict | None:
        entries = self.all()
        return entries[-1] if entries else None
