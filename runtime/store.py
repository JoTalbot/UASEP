from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from .graph import TaskGraph
from .models import Evidence, ProjectState


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(payload)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


class Store:
    """Unified persistence for state, graph, evidence, and checkpoints."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.base = self.root / ".uasep"
        self.state_path = self.base / "state.json"
        self.graph_path = self.base / "graph.json"
        self.evidence_path = self.base / "evidence" / "log.jsonl"
        self.checkpoint_path = self.base / "checkpoints" / "journal.jsonl"

    def load_state(self, project_id: str) -> ProjectState:
        if not self.state_path.exists():
            return ProjectState(project_id=project_id)
        data = json.loads(self.state_path.read_text(encoding="utf-8"))
        state = ProjectState.from_dict(data, default_project_id=project_id)
        if project_id and state.project_id and state.project_id != project_id:
            raise ValueError(f"state belongs to project {state.project_id!r}, not {project_id!r}")
        return state

    def save_state(self, state: ProjectState, *, expected_revision: int | None = None) -> None:
        current = 0
        if self.state_path.exists():
            current = int(json.loads(self.state_path.read_text(encoding="utf-8")).get("revision", 0))
        if expected_revision is not None and current != expected_revision:
            raise RuntimeError(f"state revision conflict: expected {expected_revision}, found {current}")
        state.revision = current + 1
        _atomic_write(self.state_path, json.dumps(state.to_dict(), indent=2, sort_keys=True) + "\n")

    def load_graph(self) -> TaskGraph:
        if not self.graph_path.exists():
            return TaskGraph([])
        data = json.loads(self.graph_path.read_text(encoding="utf-8"))
        return TaskGraph.from_dict(data)

    def save_graph(self, graph: TaskGraph, protocol_version: str = "3.2.0-new") -> None:
        _atomic_write(
            self.graph_path,
            json.dumps(graph.to_dict(protocol_version), indent=2, sort_keys=True) + "\n",
        )

    def record_evidence(
        self,
        task_id: str,
        kind: str,
        status: str,
        detail: str,
        source: str = "runtime",
    ) -> str:
        evidence_id = str(uuid4())
        record = Evidence(evidence_id, task_id, kind, status, detail, source)
        self.evidence_path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps({"ts": _utc_now(), **record.to_dict()}, sort_keys=True)
        with self.evidence_path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        return evidence_id

    def checkpoint(self, task_id: str | None, phase: str) -> None:
        self.checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps({"ts": _utc_now(), "task_id": task_id, "phase": phase}, sort_keys=True)
        with self.checkpoint_path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
            fh.flush()
            os.fsync(fh.fileno())

    def load_bundle(self, project_id: str) -> tuple[ProjectState, TaskGraph]:
        state, graph = self.load_state(project_id), self.load_graph()
        fingerprint = graph.fingerprint()
        if state.graph_fingerprint and state.graph_fingerprint != fingerprint:
            raise ValueError("persistent task graph fingerprint mismatch")
        state.graph_fingerprint = fingerprint
        return state, graph

    def save_bundle(self, state: ProjectState, graph: TaskGraph) -> None:
        state.graph_fingerprint = graph.fingerprint()
        self.save_graph(graph, state.protocol_version)
        self.save_state(state)
