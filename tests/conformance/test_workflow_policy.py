"""Behavioral policy checks for GitHub Actions workflows.

These tests replace the former echo-only "audit" workflows (permissions
audit, SHA-pinning check, security scanner, workflow audit) with real,
repository-native assertions that run inside the canonical conformance
suite. A green conformance run now genuinely demonstrates these policies.
"""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS_DIR = ROOT / ".github" / "workflows"

# The complete, deliberate workflow inventory. Adding or removing a workflow
# requires updating this set on purpose — this guard exists so the workflow
# directory can never silently drift back to dozens of no-op stubs.
EXPECTED_WORKFLOWS = {
    "conformance.yml",        # canonical pytest conformance suite
    "release-gate.yml",       # deliberate manual pre-release verification
    "automated-release.yml",  # tag + GitHub release after a passing gate
    "release-verification.yml",  # published-release integrity check
}

# Workflows allowed to hold write permissions. Keep this list short and
# justify every entry.
WRITE_PERMISSION_ALLOWLIST = {
    "automated-release.yml",  # creates the immutable tag and GitHub release
}

SHA_PIN_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-f]{40}$")

SECRET_PATTERNS = (
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)

EXCLUDED_SCAN_DIRS = {".git", "__pycache__", ".pytest_cache"}


def _workflow_files():
    return sorted(list(WORKFLOWS_DIR.glob("*.yml")) + list(WORKFLOWS_DIR.glob("*.yaml")))


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _triggers(workflow):
    on = workflow.get(True, workflow.get("on", {}))
    if isinstance(on, list):
        return {str(item) for item in on}
    if isinstance(on, dict):
        return {str(key) for key in on}
    return set()


def _jobs(workflow):
    return workflow.get("jobs") or {}


def _steps(workflow):
    for job in _jobs(workflow).values():
        for step in job.get("steps", []) or []:
            yield step


def _permission_grants(value):
    if isinstance(value, str):
        return {value}
    if isinstance(value, dict):
        return {str(v) for v in value.values()}
    return set()


def test_workflow_inventory_is_minimal_and_declared():
    files = {path.name for path in _workflow_files()}
    assert files == EXPECTED_WORKFLOWS, (
        "workflow inventory drifted from the declared set: "
        f"unexpected={sorted(files - EXPECTED_WORKFLOWS)} "
        f"missing={sorted(EXPECTED_WORKFLOWS - files)}"
    )


def test_every_workflow_declares_explicit_top_level_permissions():
    for path in _workflow_files():
        workflow = _load(path)
        assert "permissions" in workflow, f"{path.name}: missing top-level permissions block"


def test_write_permissions_are_explicitly_whitelisted():
    for path in _workflow_files():
        workflow = _load(path)
        grants = set()
        grants |= _permission_grants(workflow.get("permissions"))
        for job in _jobs(workflow).values():
            grants |= _permission_grants(job.get("permissions"))
        if "write" in grants:
            assert path.name in WRITE_PERMISSION_ALLOWLIST, (
                f"{path.name}: write permissions require an explicit allowlist entry"
            )


def test_every_action_reference_is_pinned_to_a_full_sha():
    for path in _workflow_files():
        workflow = _load(path)
        for step in _steps(workflow):
            uses = step.get("uses")
            if not uses:
                continue
            if str(uses).startswith("./"):
                continue  # local composite action
            assert SHA_PIN_RE.match(str(uses)), (
                f"{path.name}: action {uses!r} must be pinned to a full 40-char commit SHA"
            )


def test_every_workflow_checks_out_the_repository():
    """A workflow that never checks out code cannot verify anything.

    This guard exists so echo-only theater workflows cannot return.
    """
    for path in _workflow_files():
        workflow = _load(path)
        checkouts = [
            step for step in _steps(workflow)
            if str(step.get("uses", "")).startswith("actions/checkout")
        ]
        assert checkouts, f"{path.name}: no actions/checkout step — cannot inspect the repository"


def test_scheduled_workflows_run_at_most_once_per_day():
    for path in _workflow_files():
        workflow = _load(path)
        schedule = (workflow.get(True, workflow.get("on", {})) or {}).get("schedule") or []
        for entry in schedule:
            cron = str(entry.get("cron", "")).strip()
            fields = cron.split()
            assert len(fields) == 5, f"{path.name}: malformed cron {cron!r}"
            minute, hour = fields[0], fields[1]
            assert minute.isdigit(), (
                f"{path.name}: cron {cron!r} runs more than once per day (minute={minute!r})"
            )
            assert hour.isdigit(), (
                f"{path.name}: cron {cron!r} runs more than once per day (hour={hour!r})"
            )


def test_canonical_conformance_actually_executes_the_test_suite():
    """The canonical CI must install and run the pytest suite.

    Regression guard for the incident where checkout and setup-python were
    removed and the job could no longer run any tests at all.
    """
    workflow = _load(WORKFLOWS_DIR / "conformance.yml")
    run_bodies = [str(step.get("run", "")) for step in _steps(workflow)]
    joined = "\n".join(run_bodies)
    assert "pip install" in joined, "canonical workflow must install its dependencies"
    assert "pytest" in joined and "tests/conformance" in joined, (
        "canonical workflow must run the conformance suite"
    )


def test_release_gate_is_deliberate_and_runs_the_suite():
    workflow = _load(WORKFLOWS_DIR / "release-gate.yml")
    triggers = _triggers(workflow)
    assert triggers == {"workflow_dispatch"}, (
        "the release gate must be dispatched deliberately, not triggered on every push"
    )
    joined = "\n".join(str(step.get("run", "")) for step in _steps(workflow))
    assert "pip install" in joined and "pytest" in joined, (
        "the release gate must install dependencies and run the conformance suite"
    )


def test_automated_release_only_fires_after_the_gate():
    workflow = _load(WORKFLOWS_DIR / "automated-release.yml")
    triggers = _triggers(workflow)
    assert "workflow_run" in triggers and "push" not in triggers and "schedule" not in triggers, (
        "automated releases may only follow a completed release gate run"
    )


def test_no_secrets_are_committed_to_the_repository():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if EXCLUDED_SCAN_DIRS & set(path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            match = pattern.search(text)
            assert match is None, (
                f"{path.relative_to(ROOT)}: potential secret matches {pattern.pattern!r}"
            )
