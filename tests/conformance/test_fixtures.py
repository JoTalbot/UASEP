import json
from pathlib import Path

import pytest

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"
FIXTURES = ROOT / "tests" / "conformance" / "fixtures"

FIXTURE_SCHEMAS = {
    "manifest.json": "manifest.schema.json",
    "state.json": "state.schema.json",
    "capabilities.json": "capabilities.schema.json",
    "readiness.json": "readiness.schema.json",
    "ownership.json": "ownership.schema.json",
    "batch.json": "batch.schema.json",
    "task.json": "task.schema.json",
    "evidence.json": "evidence.schema.json",
}


@pytest.mark.skipif(jsonschema is None, reason="jsonschema is not installed")
@pytest.mark.parametrize("fixture,schema", FIXTURE_SCHEMAS.items())
def test_reference_fixture_matches_schema(fixture, schema):
    document = json.loads((FIXTURES / fixture).read_text())
    definition = json.loads((SCHEMAS / schema).read_text())
    jsonschema.Draft202012Validator(definition).validate(document)


def test_all_reference_fixtures_exist():
    for fixture in FIXTURE_SCHEMAS:
        assert (FIXTURES / fixture).is_file(), fixture
