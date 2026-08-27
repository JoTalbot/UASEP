from __future__ import annotations

import json
from pathlib import Path

from runtime.bootstrap import bootstrap_project
from runtime.checkpoints import CheckpointStore
from runtime.discovery import capabilities_dict
from runtime.state import StateStore


def test_bootstrap_is_non_destructive(tmp_path: Path) -> None:
    existing = tmp_path / ".uasep" / "manifest.yaml"
    existing.parent.mkdir(parents=True)
    existing.write_text("custom: preserved\n", encoding="utf-8")

    created = bootstrap_project(tmp_path)

    assert existing.read_text(encoding="utf-8") == "custom: preserved\n"
    assert created
    assert (tmp_path / ".uasep" / "state" / "PROJECT_STATE.md").exists()


def test_state_store_round_trip(tmp_path: Path) -> None:
    store = StateStore(tmp_path)
    state = store.load("demo")
    state.iteration = 7
    state.completed_tasks.add("TASK-1")
    store.save(state)

    restored = store.load("demo")
    assert restored.iteration == 7
    assert restored.completed_tasks == {"TASK-1"}


def test_checkpoint_round_trip(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path)
    payload = {"task": "TASK-1", "status": "in_progress"}
    store.save(payload)
    assert store.load() == payload


def test_capability_discovery_is_conservative(tmp_path: Path) -> None:
    data = capabilities_dict(tmp_path)
    assert data["read_files"]["available"] is True
    assert data["network"]["available"] is False
