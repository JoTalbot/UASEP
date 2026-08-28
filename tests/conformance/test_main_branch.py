from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_repository_instructions_require_explicit_branch_discipline():
    agents = (ROOT / "AGENTS.md").read_text()
    assert "branch" in agents.lower()
    assert "ownership" in agents.lower()
    assert "write set" in agents.lower()


def test_conformance_does_not_depend_on_hidden_chat_state():
    bootstrap = (ROOT / "bootstrap" / "UASEP_BOOTSTRAP.md").read_text()
    assert "chat history" in bootstrap.lower()
    assert "repository" in bootstrap.lower()


def test_conformance_workflow_is_read_only_and_main_scoped():
    workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text()
    assert "branches:" in workflow
    assert "- main" in workflow
    assert "permissions:" in workflow
    assert "contents: read" in workflow
    assert "contents: write" not in workflow
    assert "packages: write" not in workflow
    assert "actions: write" not in workflow


def test_conformance_workflow_runs_on_push_and_pull_request_to_main():
    workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text()
    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert "branches:" in workflow
    assert workflow.count("- main") >= 2
