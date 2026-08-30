import json
from pathlib import Path

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

ROOT = Path(__file__).resolve().parents[2]


def _version():
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def test_manifest_schema_is_valid_json():
    schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text())
    assert schema["$schema"].endswith("draft/2020-12/schema")
    assert schema["properties"]["protocol"]["const"] == "UASEP"
    assert schema["properties"]["uasep_runtime"]["const"] == "NONE"


def test_reference_manifest_is_conformant_when_validator_available():
    if jsonschema is None:
        return
    schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text())
    manifest = {
        "protocol": "UASEP",
        "protocol_version": _version(),
        "project_instance": "example",
        "project_state": "ADOPTED",
        "autonomy_level": "L0",
        "source_of_truth": "repository",
        "uasep_runtime": "NONE",
    }
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(manifest, schema)


def test_manifest_schema_supports_runtime_projects_without_lying():
    """F1 (M63): a project whose product IS a runtime must be describable.

    uasep_runtime stays NONE (the protocol layer needs no runtime) while
    project_runtime describes the project's own nature, and a project
    extension object carries project-specific metadata.
    """
    if jsonschema is None:
        return
    schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text())
    manifest = {
        "protocol": "UASEP",
        "protocol_version": _version(),
        "project_instance": "example-runtime-project",
        "project_state": "ACTIVE",
        "autonomy_level": "L3",
        "source_of_truth": "repository",
        "uasep_runtime": "NONE",
        "project_runtime": "autonomous agent runtime (FastAPI/uvicorn)",
        "project": {"validation": {"ci": "github-actions", "required": True}},
    }
    jsonschema.validate(manifest, schema)
