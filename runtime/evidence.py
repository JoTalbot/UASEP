from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json

from .models import Evidence


class EvidenceStore:
    """Append-only JSONL evidence ledger for completion claims."""

    def __init__(self, root: str | Path):
        self.path = Path(root) / ".uasep" / "evidence" / "runtime.jsonl"

    def record(self, evidence: Evidence) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(asdict(evidence), ensure_ascii=False) + "\n")
