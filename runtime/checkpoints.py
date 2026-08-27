from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class NamedCheckpoint:
    name: str
    task_id: str
    payload: dict[str, Any]
    timestamp: str


class CheckpointStore:
    """Atomic, portable state checkpoint for the canonical runtime."""

    def __init__(self, root: str | Path):
        self.path = Path(root) / ".uasep" / "checkpoints.json"

    def save(self, state: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, self.path)

    def load(self) -> dict[str, Any] | None:
        if not self.path.exists():
            return None
        return json.loads(self.path.read_text(encoding="utf-8"))


class CheckpointManager:
    """Compatibility journal used by RecoveryManager and older integrations."""

    def __init__(self, directory: str | Path):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / "journal.json"

    def _all(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def create(self, task_id: str, payload: dict[str, Any]) -> NamedCheckpoint:
        entries = self._all()
        timestamp = datetime.now(timezone.utc).isoformat()
        name = f"{len(entries) + 1:06d}-{task_id}"
        record = {"name": name, "task_id": task_id, "payload": payload, "timestamp": timestamp}
        entries.append(record)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(entries, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, self.path)
        return NamedCheckpoint(name, task_id, payload, timestamp)

    def latest(self) -> NamedCheckpoint | None:
        entries = self._all()
        if not entries:
            return None
        item = entries[-1]
        return NamedCheckpoint(item["name"], item["task_id"], item.get("payload", {}), item["timestamp"])
