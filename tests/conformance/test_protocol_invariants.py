"""Repository-native checks for documented protocol invariants."""
from pathlib import Path
import json

ROOT = Path(__file__).parents[2]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_bootstrap_material_is_present():
    assert (ROOT / "AGENTS.md").is_file()
    assert (ROOT / "protocol/AGENT_READINESS.md").is_file()
    assert (ROOT / ".uasep/state/state.json").is_file()


def test_readiness_state_is_adopted_and_runtime_free():
    state = json.loads(_read(".uasep/state/state.json"))
    assert state["project_state"] == "ADOPTED"
    assert state["environment"]
    assert state["active_task"] is None
    assert state["active_tasks"] == []


def test_durable_state_narratives_do_not_drift():
    state = json.loads(_read(".uasep/state/state.json"))
    project_state = _read(".uasep/state/PROJECT_STATE.md")
    status = _read(".uasep/state/STATUS.md")
    handoff = _read(".uasep/state/HANDOFF.md")

    assert f"Status: {state['project_state']}" in project_state
    assert f"protocol {state['protocol_version'].rsplit('.', 1)[0]}" in project_state
    assert f"Phase: {state['project_state']}" in status
    assert "- ID: NONE" in status
    assert "Current task: NONE." in handoff
    assert "H20: **UNVERIFIED / EXTERNALLY DEPENDENT**" not in _read(
        ".uasep/planning/NEXT_20.md"
    )
    assert "Fresh-agent acceptance evidence is recorded" in project_state
    assert "Fresh-agent acceptance: VERIFIED" in status


def test_capability_claims_are_repository_bounded():
    manifest = _read(".uasep/manifest.yaml")
    assert "source_of_truth: repository" in manifest
    assert "runtime: NONE" in manifest


def test_task_contract_requires_bounded_write_sets():
    text = _read("protocol/TASK_CONTRACT.md")
    for required in ("write_set", "dependencies", "conflicts", "acceptance", "verification"):
        assert required in text
    assert "authorization boundary" in text


def test_batch_manifest_classifies_execution_safety():
    text = _read("protocol/BATCH_MANIFEST.md")
    for required in ("INDEPENDENT", "DEPENDENT", "CONFLICTING", "BLOCKED", "write sets"):
        assert required in text


def test_evidence_contract_requires_observable_claims():
    text = _read("protocol/EVIDENCE_SCHEMA.md")
    for required in ("VERIFIED", "UNKNOWN", "FAILED", "evidence"):
        assert required in text


def test_conformance_forbids_unknown_to_verified_shortcuts():
    text = _read("protocol/CONFORMANCE.md")
    assert "UNKNOWN" in text
    assert "VERIFIED" in text
    assert "independent" in text.lower()


def test_destructive_safeguards_are_documented():
    text = _read("protocol/CONFORMANCE.md").lower()
    assert "destructive" in text
    assert "explicit approval" in text
    assert "recoverable checkpoint" in text


def test_recovery_requires_durable_state():
    text = _read("protocol/CONFORMANCE.md").lower()
    assert "recovery" in text
    assert "durable" in text
    assert "state" in text


def test_no_runtime_dependency_is_introduced_by_protocol_checks():
    text = _read("protocol/CONFORMANCE.md").lower()
    assert "does not require a uasep runtime" in text
