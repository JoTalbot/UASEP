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
    def __init__(self, path: Path) -> None:
        self.path = path

    def record(self, evidence: Evidence) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        entries = self.all()
        entries.append(asdict(evidence))
        self.path.write_text(json.dumps(entries, indent=2), encoding="utf-8")

    def all(self) -> list[dict]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))
