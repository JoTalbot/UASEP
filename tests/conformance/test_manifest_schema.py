import json
from pathlib import Path

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

ROOT = Path(__file__).resolve().parents[2]


def test_manifest_schema_is_valid_json():
    schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text())
    assert schema["$schema"].endswith("draft/2020-12/schema")
    assert schema["properties"]["protocol"]["const"] == "UASEP"


def test_reference_manifest_is_conformant_when_validator_available():
    if jsonschema is None:
        return
    schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text())
    manifest = {
        "protocol": "UASEP",
        "protocol_version": "3.1.0",
        "project_instance": "example",
        "project_state": "active",
        "autonomy_level": "L4",
    }
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(manifest, schema)
