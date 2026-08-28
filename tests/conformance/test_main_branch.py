from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_repository_instructions_require_explicit_branch_discipline():
    agents = (ROOT / "AGENTS.md").read_text()
    assert "branch" in agents.lower()
    assert "ownership" in agents.lower()
    assert "write_set" in agents


def test_conformance_does_not_depend_on_hidden_chat_state():
    bootstrap = (ROOT / "bootstrap" / "UASEP_BOOTSTRAP.md").read_text()
    assert "chat history" in bootstrap.lower()
    assert "repository" in bootstrap.lower()
