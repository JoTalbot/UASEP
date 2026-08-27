from __future__ import annotations

from pathlib import Path


REQUIRED_DIRS = (
    ".uasep",
    ".uasep/state",
    ".uasep/planning",
    ".uasep/knowledge",
    ".uasep/evidence",
    ".uasep/checkpoints",
)


def bootstrap_project(root: Path, project_name: str | None = None) -> list[Path]:
    """Create missing UASEP directories without overwriting project artifacts."""
    created: list[Path] = []
    for relative in REQUIRED_DIRS:
        path = root / relative
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(path)
    state = root / ".uasep" / "state" / "PROJECT_STATE.md"
    if not state.exists():
        name = project_name or root.name
        state.write_text(
            f"# Project State\n\nProject: {name}\nStatus: new\n\n",
            encoding="utf-8",
        )
        created.append(state)
    return created
