"""Repository-native checks for documented protocol invariants."""
from pathlib import Path
import json

ROOT = Path(__file__).parents[2]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_bootstrap_material_is_present():
    assert (ROOT / "AGENTS.md").is_file()
    assert (ROOT / "protocol/AGENT_READINESS.md").is_file()
    assert (ROOT / "bootstrap/UASEP_BOOTSTRAP.md").is_file()
    assert (ROOT / ".uasep/state/state.json").is_file()


def test_readiness_state_is_adopted_and_runtime_free():
    state = json.loads(_read(".uasep/state/state.json"))
    assert state["project_state"] == "ADOPTED"
    assert state["environment"]
    assert state["active_task"] == "M24-M30"
    assert state["active_tasks"] == ["M24", "M25", "M26", "M27", "M28", "M29", "M30"]


def test_durable_state_narratives_do_not_drift():
    state = json.loads(_read(".uasep/state/state.json"))
    project_state = _read(".uasep/state/PROJECT_STATE.md")
    status = _read(".uasep/state/STATUS.md")
    handoff = _read(".uasep/state/HANDOFF.md")

    protocol_version = state["protocol_version"]
    assert f"Status: {state['project_state']}" in project_state
    assert f"Protocol version: {protocol_version}" in project_state
    assert f"Phase: {state['project_state']}" in status
    assert f"- ID: {state['active_task']}" in status
    assert "Current task: M24-M30 maintenance continuation." in handoff
    assert "H20: **UNVERIFIED / EXTERNALLY DEPENDENT**" not in _read(".uasep/planning/NEXT_20.md")
    assert "Fresh-agent acceptance evidence is recorded" in project_state
    assert "Fresh-agent acceptance: VERIFIED" in status


def test_evidence_contract_requires_observable_claims():
    text = _read("protocol/EVIDENCE_SCHEMA.md")
    for required in ("VERIFIED", "UNKNOWN", "FAILED", "evidence"):
        assert required in text


def test_evidence_artifacts_match_schema_contract():
    schema = json.loads(_read("schemas/evidence.schema.json"))
    required = set(schema["required"])
    allowed_results = set(schema["properties"]["result"]["enum"])
    evidence_dir = ROOT / ".uasep" / "evidence"
    ids = set()

    for path in sorted(evidence_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert required.issubset(data.keys())
        assert data["result"] in allowed_results
        assert data["evidence_id"] not in ids
        ids.add(data["evidence_id"])
        assert isinstance(data.get("observed"), str) and data["observed"]


def test_manifest_and_state_are_version_consistent():
    state = json.loads(_read(".uasep/state/state.json"))
    manifest = _read(".uasep/manifest.yaml")
    assert f"protocol: {state['protocol']}" in manifest
    assert f"protocol_version: {state['protocol_version']}" in manifest
    assert f"project_state: {state['project_state']}" in manifest
    assert "runtime: NONE" in manifest


def test_bootstrap_is_repository_bounded():
    text = _read("bootstrap/UASEP_BOOTSTRAP.md").lower()
    assert "repository" in text
    assert "chat history" in text
    assert "durable" in text


def test_runtime_free_active_tree_has_no_runtime_artifacts():
    forbidden_files = (
        "uasep_daemon.py",
        "uasep_runtime.py",
        "uasep_cli.py",
    )
    for filename in forbidden_files:
        matches = list(ROOT.rglob(filename))
        assert not matches, f"runtime artifact present: {filename}"


def test_skill_contract_and_inventory_are_present():
    skills = ROOT / "skills"
    assert skills.is_dir()
    skill_files = [path for path in skills.rglob("*.md") if path.is_file()]
    assert skill_files
    combined = "\n".join(path.read_text(encoding="utf-8") for path in skill_files)
    for required in ("audit", "verify", "handoff"):
        assert required in combined.lower()


def test_examples_reference_normative_protocol_material():
    examples = ROOT / "examples"
    assert examples.is_dir()
    files = [path for path in examples.rglob("*") if path.is_file()]
    assert files
    combined = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in files)
    assert "protocol/" in combined or "AGENTS.md" in combined


def test_no_runtime_dependency_is_introduced_by_protocol_checks():
    text = _read("protocol/CONFORMANCE.md").lower()
    assert "does not require a uasep runtime" in text


def test_capability_claims_are_repository_bounded():
    manifest = _read(".uasep/manifest.yaml")
    assert "source_of_truth: repository" in manifest
    assert "runtime: NONE" in manifest
