import json
from pathlib import Path

import pytest

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"


def load_schema(name):
    return json.loads((SCHEMAS / name).read_text())


@pytest.mark.skipif(jsonschema is None, reason="jsonschema is not installed")
def test_reference_manifest_matches_schema():
    schema = load_schema("manifest.schema.json")
    manifest = {
        "protocol": "UASEP",
        "protocol_version": (ROOT / "VERSION").read_text().strip(),
        "project_instance": "UASEP",
        "project_state": "ADOPTED",
        "autonomy_level": "L0",
        "source_of_truth": "repository",
        "uasep_runtime": "NONE",
    }
    jsonschema.validate(manifest, schema)


def test_reference_manifest_has_no_legacy_runtime_fields():
    text = (ROOT / ".uasep" / "manifest.yaml").read_text()
    assert f"protocol_version: {(ROOT / 'VERSION').read_text().strip()}" in text
    assert "project_state: ADOPTED" in text
    assert "uasep_runtime: NONE" in text
    assert "runtime_version:" not in text


def test_acceptance_state_is_explicitly_verified():
    status = (ROOT / ".uasep" / "state" / "STATUS.md").read_text()
    assert "Fresh-agent acceptance: VERIFIED" in status
    assert "Canonical conformance:" in status


def test_fresh_agent_acceptance_requires_repository_only_context():
    acceptance = (ROOT / "examples" / "FRESH_AGENT_ACCEPTANCE.md").read_text()
    assert "no access to the originating chat history" in acceptance
    assert "repository and the GitHub-connected capabilities" in acceptance
    assert "MUST NOT require the previous chat" in acceptance
