from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_reference_tree_declares_runtime_free_contract():
    manifest = (ROOT / ".uasep" / "manifest.yaml").read_text()
    readiness = (ROOT / "tests" / "conformance" / "fixtures" / "readiness.json").read_text()

    assert "runtime: NONE" in manifest
    assert '"runtime": "NONE"' in readiness or '"runtime":"NONE"' in readiness
