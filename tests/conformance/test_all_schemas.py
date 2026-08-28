import json
from pathlib import Path

import pytest

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas"
EVIDENCE_DIR = ROOT / ".uasep" / "evidence"

EXPECTED_SCHEMAS = (
    "manifest.schema.json",
    "state.schema.json",
    "capabilities.schema.json",
    "readiness.schema.json",
    "ownership.schema.json",
    "batch.schema.json",
    "task.schema.json",
    "evidence.schema.json",
)


@pytest.mark.skipif(jsonschema is None, reason="jsonschema is not installed")
def test_all_declared_schemas_are_valid():
    for filename in EXPECTED_SCHEMAS:
        schema = json.loads((SCHEMA_DIR / filename).read_text())
        jsonschema.Draft202012Validator.check_schema(schema)


def test_all_declared_schema_files_exist():
    for filename in EXPECTED_SCHEMAS:
        assert (SCHEMA_DIR / filename).is_file(), filename


@pytest.mark.skipif(jsonschema is None, reason="jsonschema is not installed")
def test_machine_readable_state_matches_state_schema():
    schema = json.loads((SCHEMA_DIR / "state.schema.json").read_text())
    state = json.loads((ROOT / ".uasep" / "state" / "state.json").read_text())
    jsonschema.Draft202012Validator(schema).validate(state)
    assert state["protocol"] == "UASEP"
    assert state["protocol_version"] == "3.4.0"
    assert state["project_state"] == "ADOPTED"


@pytest.mark.skipif(yaml is None, reason="pyyaml is not installed")
def test_manifest_projection_matches_machine_readable_state():
    manifest = yaml.safe_load((ROOT / ".uasep" / "manifest.yaml").read_text())
    state = json.loads((ROOT / ".uasep" / "state" / "state.json").read_text())
    for key in ("protocol", "protocol_version", "project_state"):
        assert manifest[key] == state[key]


@pytest.mark.skipif(jsonschema is None, reason="jsonschema is not installed")
def test_all_repository_evidence_records_match_evidence_schema():
    schema = json.loads((SCHEMA_DIR / "evidence.schema.json").read_text())
    records = sorted(EVIDENCE_DIR.glob("*.json"))
    assert records, "no evidence records found"

    evidence_ids = []
    for path in records:
        document = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(document)
        evidence_ids.append(document["evidence_id"])

    assert len(evidence_ids) == len(set(evidence_ids)), "duplicate evidence_id detected"


def test_manifest_is_runtime_free():
    manifest = (ROOT / ".uasep" / "manifest.yaml").read_text()
    assert "runtime: NONE" in manifest
    assert "protocol_version: 3.4.0" in manifest


def test_canonical_truth_statuses_are_present():
    core = (ROOT / "protocol" / "CORE.md").read_text()
    for status in ("VERIFIED", "PARTIALLY_VERIFIED", "UNKNOWN", "FAILED"):
        assert status in core
    assert "INFERRED" not in core
