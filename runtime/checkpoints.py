from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


class CheckpointStore:
    """Atomic, portable checkpoints for interruption-safe agent handoff."""

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
