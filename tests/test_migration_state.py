from pathlib import Path

from runtime.migration import migrate_runtime_state, needs_migration
from runtime.state import StateStore


def test_migrate_adds_task_failures():
    data = {"project_id": "p", "phase": "active", "completed_tasks": []}
    assert needs_migration(data)
    out = migrate_runtime_state(data)
    assert out["task_failures"] == {}
    assert out["protocol_version"] == "3.1.2"


def test_per_project_state_paths(tmp_path: Path):
    store = StateStore(tmp_path, per_project=True)
    st = store.load("alpha")
    st.phase = "verified"
    st.completed_tasks.add("t1")
    store.save(st)
    path = tmp_path / ".uasep" / "state" / "alpha.json"
    assert path.exists()
    restored = store.load("alpha")
    assert restored.phase == "verified"
    assert "t1" in restored.completed_tasks
