from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass(slots=True)
class Evidence:
    kind: str
    claim: str
    status: str = "UNKNOWN"
    detail: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class EvidenceStore:
    """Persistent evidence journal with atomic replacement semantics."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def record(self, evidence: Evidence) -> None:
        if not isinstance(evidence, Evidence):
            raise ValueError("evidence must be an Evidence instance")
        self._validate_entry(asdict(evidence))
        entries = self.all()
        entries.append(asdict(evidence))
        self._write(entries)

    def _write(self, entries: list[dict]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(entries, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        temporary.replace(self.path)

    def all(self) -> list[dict]:
        if not self.path.exists():
            self._recover_tmp()
        if not self.path.exists():
            return []
        return self._read(self.path)

    def _recover_tmp(self) -> bool:
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        if not temporary.exists():
            return False
        try:
            self._read(temporary)
            temporary.replace(self.path)
            return True
        except (OSError, TypeError, ValueError, json.JSONDecodeError):
            return False

    @classmethod
    def _read(cls, path: Path) -> list[dict]:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list) or any(not isinstance(entry, dict) for entry in data):
            raise ValueError("evidence journal must contain a list of objects")
        for entry in data:
            cls._validate_entry(entry)
        return data

    @staticmethod
    def _validate_entry(entry: dict) -> None:
        required = ("kind", "claim", "status", "detail", "timestamp")
        if any(key not in entry for key in required):
            raise ValueError("evidence entry is missing required fields")
        for key in required:
            if not isinstance(entry[key], str):
                raise ValueError(f"evidence {key} must be a string")
        if not entry["kind"].strip() or not entry["claim"].strip():
            raise ValueError("evidence kind and claim must be non-empty")
        if not entry["status"].strip():
            raise ValueError("evidence status must be non-empty")
        if not entry["timestamp"].strip():
            raise ValueError("evidence timestamp must be non-empty")
