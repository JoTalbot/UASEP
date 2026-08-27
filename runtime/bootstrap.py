from __future__ import annotations

from pathlib import Path


DIRECTORIES = (
    ".uasep/state",
    ".uasep/planning",
    ".uasep/knowledge",
    ".uasep/evidence",
)


def bootstrap_project(root: str | Path = ".") -> list[Path]:
    """Create only missing UASEP project-local scaffolding; never overwrite user data."""
    root = Path(root)
    created: list[Path] = []
    for relative in DIRECTORIES:
        path = root / relative
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(path)

    defaults = {
        ".uasep/manifest.yaml": "protocol: UASEP\nversion: 3.1.0\nproject_state: initializing\nautonomy_level: L0\n",
        ".uasep/state/PROJECT_STATE.md": "# Project State\n\nInitialized by UASEP bootstrap.\n",
        ".uasep/state/HANDOFF.md": "# Handoff\n\nNo handoff recorded.\n",
        ".uasep/planning/MASTER_PLAN.md": "# Master Plan\n\nTo be discovered during audit.\n",
        ".uasep/planning/BACKLOG.md": "# Backlog\n\nTo be populated during planning.\n",
        ".uasep/knowledge/DECISIONS.md": "# Decisions\n\nNo decisions recorded.\n",
        ".uasep/knowledge/FAILURES.md": "# Failures\n\nNo failures recorded.\n",
        ".uasep/evidence/TESTS.md": "# Test Evidence\n\nNo test evidence recorded.\n",
        ".uasep/evidence/BUILDS.md": "# Build Evidence\n\nNo build evidence recorded.\n",
    }
    for relative, content in defaults.items():
        path = root / relative
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            created.append(path)
    return created
