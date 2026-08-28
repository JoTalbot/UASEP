from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


SCHEMA_VERSION = 2


@dataclass(frozen=True, slots=True)
class Checkpoint:
    sequence: int
    task_id: str | None
    phase: str
    timestamp: str


class CheckpointStore:
    """Append-only checkpoint journal with integrity metadata."""

    def __init__(self, path: Path) -> None:
        # Older callers passed the checkpoint directory; keep that API working
        # while the canonical API accepts the concrete checkpoint file path.
        if path.exists() and path.is_dir():
            path = path / "checkpoint.json"
        self.path = path

    def save(self, task_id: str | None, phase: str) -> Checkpoint:
        if not isinstance(phase, str) or not phase.strip():
            raise ValueError("checkpoint phase must be a non-empty string")
        if task_id is not None and (not isinstance(task_id, str) or not task_id.strip()):
            raise ValueError("checkpoint task_id must be None or a non-empty string")
        entries = self.all()
        checkpoint = Checkpoint(len(entries) + 1, task_id, phase, datetime.now(timezone.utc).isoformat())
        entries.append(asdict(checkpoint))
        self._write(entries)
        return checkpoint

    def append(self, checkpoint: dict) -> dict:
        """Compatibility API for appending a checkpoint-shaped mapping."""
        if not isinstance(checkpoint, dict):
            raise ValueError("checkpoint entry must be an object")
        entries = self.all()
        entry = dict(checkpoint)
        entry["sequence"] = len(entries) + 1
        if not isinstance(entry.get("phase"), str) or not entry["phase"].strip():
            raise ValueError("checkpoint phase must be a non-empty string")
        task_id = entry.get("task_id")
        if task_id is not None and (not isinstance(task_id, str) or not task_id.strip()):
            raise ValueError("checkpoint task_id must be None or a non-empty string")
        entries.append(entry)
        self._write(entries)
        return entry

    def load(self) -> list[dict]:
        """Compatibility alias for the canonical :meth:`all` API."""
        return self.all()

    def _payload(self, entries: list[dict]) -> dict:
        return {"schema_version": SCHEMA_VERSION, "entries": entries}

    def _checksum(self, payload: dict) -> str:
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def _write(self, entries: list[dict]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = self._payload(entries)
        document = {**payload, "checksum": self._checksum(payload)}
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(json.dumps(document, indent=2), encoding="utf-8")
        temporary.replace(self.path)

    def recover(self) -> bool:
        """Restore main checkpoint from a valid temporary checkpoint."""
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        if not temporary.exists():
            return False
        try:
            document = json.loads(temporary.read_text(encoding="utf-8"))
            if not isinstance(document, dict) or not isinstance(document.get("entries"), list):
                return False
            payload = {"schema_version": document.get("schema_version"), "entries": document["entries"]}
            if document.get("checksum") != self._checksum(payload):
                return False
            self._validate_entries(payload["entries"])
            temporary.replace(self.path)
            return True
        except (OSError, TypeError, ValueError, json.JSONDecodeError):
            return False

    def all(self) -> list[dict]:
        if not self.path.exists():
            self.recover()
        if not self.path.exists():
            return []
        document = json.loads(self.path.read_text(encoding="utf-8"))
        if isinstance(document, list):
            entries = document
        else:
            if not isinstance(document, dict) or not isinstance(document.get("entries"), list):
                raise ValueError("checkpoint journal must contain a list")
            payload = {"schema_version": document.get("schema_version"), "entries": document["entries"]}
            if document.get("checksum") != self._checksum(payload):
                raise ValueError("checkpoint checksum mismatch")
            entries = payload["entries"]
        self._validate_entries(entries)
        return entries

    def _validate_entries(self, entries: object) -> None:
        if not isinstance(entries, list):
            raise ValueError("checkpoint journal must contain a list")
        expected = 1
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError("checkpoint entry must be an object")
            if entry.get("sequence") != expected:
                raise ValueError("checkpoint sequence is invalid")
            if not isinstance(entry.get("phase"), str) or not entry["phase"].strip():
                raise ValueError("checkpoint phase must be a non-empty string")
            task_id = entry.get("task_id")
            if task_id is not None and (not isinstance(task_id, str) or not task_id.strip()):
                raise ValueError("checkpoint task_id must be None or a non-empty string")
            expected += 1

    def latest(self) -> dict | None:
        entries = self.all()
        return entries[-1] if entries else None
