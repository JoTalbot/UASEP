from __future__ import annotations

from pathlib import Path


def version_file(root: Path) -> str:
    path = root / "VERSION"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def pyproject_version(root: Path) -> str:
    path = root / "pyproject.toml"
    if not path.exists():
        return ""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("version"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def detect_version_drift(root: Path) -> list[str]:
    """Return human-readable drift findings (empty if aligned)."""
    findings: list[str] = []
    vf = version_file(root)
    pf = pyproject_version(root)
    if vf and pf and vf != pf:
        findings.append(f"VERSION ({vf}) != pyproject ({pf})")
    if not vf:
        findings.append("VERSION file missing")
    if not pf:
        findings.append("pyproject version missing")
    return findings
