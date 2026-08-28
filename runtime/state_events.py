from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class StateChangeEvent:
    """Immutable audit record for runtime state transitions."""

    task_id: str
    old_state: str
    new_state: str
    reason: str
    source: str
    timestamp: str
    correlation_id: str | None = None

    @classmethod
    def create(
        cls,
        task_id: str,
        old_state: str,
        new_state: str,
        reason: str,
        source: str,
        correlation_id: str | None = None,
    ) -> "StateChangeEvent":
        return cls(
            task_id=task_id,
            old_state=old_state,
            new_state=new_state,
            reason=reason,
            source=source,
            timestamp=datetime.now(timezone.utc).isoformat(),
            correlation_id=correlation_id,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
