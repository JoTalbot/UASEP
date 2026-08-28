from pathlib import Path

import pytest

from runtime.graph import TaskGraph
from runtime.models import Task, TaskStatus
from runtime.safety import ApprovalGate
from runtime.store import Store
from runtime.supervisor import Supervisor


def test_graph_respects_dependencies():
    graph = TaskGraph([
        Task(id="A", objective="first", priority=10),
        Task(id="B", objective="second", priority=100, dependencies=["A"]),
    ])
    assert [t.id for t in graph.ready()] == ["A"]
    graph.apply("A", TaskStatus.VERIFIED)
    assert [t.id for t in graph.ready()] == ["B"]


def test_state_round_trip(tmp_path: Path):
    store = Store(tmp_path)
    state = store.load_state("demo")
    state.phase = "active"
    state.completed_tasks.append("A")
    store.save_state(state)
    restored = store.load_state("demo")
    assert restored.phase == "active"
    assert "A" in restored.completed_tasks
    assert restored.revision == 1


def test_supervisor_completes_chain(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph([
        Task(id="A", objective="first", acceptance_criteria=["ok"]),
        Task(id="B", objective="second", dependencies=["A"], acceptance_criteria=["ok"]),
    ])
    store.save_bundle(store.load_state("demo"), graph)
    sup = Supervisor(tmp_path, execute=lambda _t: True)
    assert sup.run_once("demo").status == "VERIFIED"
    assert sup.run_once("demo").status == "VERIFIED"
    assert sup.run_once("demo").status == "COMPLETE"


def test_failed_task_is_retried_after_persistence(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph([Task(id="A", objective="flaky")])
    store.save_bundle(store.load_state("demo"), graph)
    calls = {"n": 0}

    def flaky(_task):
        calls["n"] += 1
        return calls["n"] >= 2

    Supervisor(tmp_path, execute=flaky).run_once("demo")
    restored = Store(tmp_path).load_graph().tasks["A"]
    assert restored.failure_count == 1
    assert restored.status == TaskStatus.RETRYABLE
    assert Supervisor(tmp_path, execute=flaky).run_once("demo").status == "VERIFIED"


def test_verification_failure_never_completes_task(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph([Task(id="A", objective="bad", acceptance_criteria=["must-pass"])])
    store.save_bundle(store.load_state("demo"), graph)
    result = Supervisor(tmp_path, execute=lambda _t: True, checks=lambda _t: [("must-pass", lambda: False)]).run_once("demo")
    assert result.status == "FAILED"
    assert Store(tmp_path).load_graph().tasks["A"].status == TaskStatus.RETRYABLE


def test_graph_fingerprint_detects_tampering(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph([Task(id="A", objective="original")])
    store.save_bundle(store.load_state("demo"), graph)
    raw = store.graph_path.read_text(encoding="utf-8").replace("original", "tampered")
    store.graph_path.write_text(raw, encoding="utf-8")
    with pytest.raises(ValueError, match="fingerprint"):
        store.load_graph()


def test_destructive_action_requires_approval():
    task = Task(id="A", objective="delete", risk="critical")
    assert not ApprovalGate().allow(task)
    assert ApprovalGate(allow_destructive=True).allow(task)
