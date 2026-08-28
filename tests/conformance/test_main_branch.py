import json
from pathlib import Path

import pytest

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

ROOT = Path(__file__).resolve().parents[2]


def test_repository_instructions_require_explicit_branch_discipline():
    agents = (ROOT / "AGENTS.md").read_text()
    assert "branch" in agents.lower()
    assert "ownership" in agents.lower()
    assert "write set" in agents.lower()


def test_conformance_does_not_depend_on_hidden_chat_state():
    bootstrap = (ROOT / "bootstrap" / "UASEP_BOOTSTRAP.md").read_text()
    assert "chat history" in bootstrap.lower()
    assert "repository" in bootstrap.lower()


def test_conformance_workflow_is_read_only_and_main_scoped():
    workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text()
    assert "branches:" in workflow
    assert "- main" in workflow
    assert "permissions:" in workflow
    assert "contents: read" in workflow
    assert "contents: write" not in workflow
    assert "packages: write" not in workflow
    assert "actions: write" not in workflow


def test_conformance_workflow_runs_on_push_and_pull_request_to_main():
    workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text()
    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert workflow.count("- main") >= 2


def test_version_file_matches_machine_state_and_manifest():
    state = json.loads((ROOT / ".uasep" / "state" / "state.json").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    manifest = (ROOT / ".uasep" / "manifest.yaml").read_text(encoding="utf-8")
    assert version == state["protocol_version"]
    assert f"protocol_version: {version}" in manifest


def test_all_ownership_records_match_schema_and_are_reconciled():
    schema = json.loads((ROOT / "schemas" / "ownership.schema.json").read_text(encoding="utf-8"))
    ownership_dir = ROOT / ".uasep" / "state"
    records = sorted(ownership_dir.glob("OWNERSHIP_*.json"))
    assert records

    for path in records:
        data = json.loads(path.read_text(encoding="utf-8"))
        if jsonschema is not None:
            jsonschema.Draft202012Validator(schema).validate(data)
        assert data["status"] in {"ACTIVE", "RELEASED", "TRANSFERRED", "STALE", "CONFLICT"}
        if data["status"] == "RELEASED":
            assert data.get("transfer_to") in (None, "")


def test_drift_policy_declares_active_tree_priority():
    text = (ROOT / "protocol" / "DRIFT_DETECTION.md").read_text(encoding="utf-8").lower()
    assert "active tree" in text
    assert "normative" in text
    assert "historical" in text
    assert "conflict" in text
