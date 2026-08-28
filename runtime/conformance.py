from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class CheckResult:
    name: str
    passed: bool
    detail: str = ""


REQUIRED_DIRS = (
    ".uasep",
    ".uasep/state",
    ".uasep/planning",
    ".uasep/knowledge",
    ".uasep/evidence",
)


def check_project(root: Path) -> list[CheckResult]:
    """Structural + minimal ideology checks for a UASEP project instance."""
    root = Path(root)
    results: list[CheckResult] = []
    for relative in REQUIRED_DIRS:
        path = root / relative
        results.append(CheckResult(f"directory:{relative}", path.is_dir()))

    manifest = root / ".uasep" / "manifest.yaml"
    results.append(CheckResult("manifest", manifest.is_file()))

    state_path = root / ".uasep" / "state.json"
    if state_path.is_file():
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
            ok = data.get("protocol") == "UASEP" and "phase" in data
            results.append(CheckResult("state.json", ok, "protocol+phase" if ok else "invalid shape"))
        except json.JSONDecodeError as exc:
            results.append(CheckResult("state.json", False, str(exc)))
    else:
        results.append(CheckResult("state.json", False, "missing"))

    graph_path = root / ".uasep" / "graph.json"
    if graph_path.is_file():
        try:
            data = json.loads(graph_path.read_text(encoding="utf-8"))
            ok = data.get("protocol") == "UASEP" and isinstance(data.get("tasks"), list)
            results.append(CheckResult("graph.json", ok, "protocol+tasks" if ok else "invalid shape"))
        except json.JSONDecodeError as exc:
            results.append(CheckResult("graph.json", False, str(exc)))
    else:
        results.append(CheckResult("graph.json", False, "missing"))

    return results


def is_conformant(root: Path) -> bool:
    return all(result.passed for result in check_project(root))
