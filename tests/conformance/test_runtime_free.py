from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_reference_tree_declares_runtime_free_contract():
    manifest = (ROOT / ".uasep" / "manifest.yaml").read_text()
    readiness = (ROOT / "tests" / "conformance" / "fixtures" / "readiness.json").read_text()

    assert "uasep_runtime: NONE" in manifest
    assert '"uasep_runtime": "NONE"' in readiness or '"uasep_runtime":"NONE"' in readiness
