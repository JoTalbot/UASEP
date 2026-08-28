from __future__ import annotations

from typing import Any


# Ordered migrations: each step transforms state dict in place / returns new dict.
_MIGRATIONS: list[tuple[str, str, str]] = [
    # (from, to, description)
    ("3.1.0", "3.1.1", "no state change"),
    ("3.1.1", "3.1.2", "ensure task_failures default"),
]


def normalize_version(version: str | None) -> str:
    if not version:
        return "3.1.0"
    return version.strip()


def migrate_runtime_state(data: dict[str, Any], target: str = "3.1.2") -> dict[str, Any]:
    """Migrate persisted ProjectState-shaped dict toward target version."""
    out = dict(data)
    current = normalize_version(str(out.get("protocol_version") or out.get("version") or "3.1.0"))
    # Always ensure task_failures for 3.1.2+
    if "task_failures" not in out or out["task_failures"] is None:
        out["task_failures"] = {}
    if not isinstance(out["task_failures"], dict):
        out["task_failures"] = {}
    out["protocol_version"] = target
    out.setdefault("completed_tasks", out.get("completed_tasks") or [])
    out.setdefault("blockers", out.get("blockers") or [])
    out.setdefault("iteration", int(out.get("iteration") or 0))
    out.setdefault("phase", out.get("phase") or "initializing")
    return out


def needs_migration(data: dict[str, Any], target: str = "3.1.2") -> bool:
    current = normalize_version(str(data.get("protocol_version") or data.get("version") or ""))
    return current != target or "task_failures" not in data
