from __future__ import annotations

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
    results: list[CheckResult] = []
    for relative in REQUIRED_DIRS:
        path = root / relative
        results.append(CheckResult(f"directory:{relative}", path.is_dir()))
    manifest = root / ".uasep" / "manifest.yaml"
    results.append(CheckResult("manifest", manifest.is_file()))
    return results


def is_conformant(root: Path) -> bool:
    return all(result.passed for result in check_project(root))
