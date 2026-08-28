from pathlib import Path

from runtime.graph import TaskGraph
from runtime.models import Task, TaskStatus
from runtime.store import Store
from runtime.supervisor import Supervisor


def test_graph_respects_dependencies():
    graph = TaskGraph(
        [
            Task(id="A", objective="first", priority=10),
            Task(id="B", objective="second", priority=100, dependencies=["A"]),
        ]
    )
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


def test_supervisor_completes_chain(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph(
        [
            Task(id="A", objective="first", acceptance_criteria=["ok"]),
            Task(id="B", objective="second", dependencies=["A"], acceptance_criteria=["ok"]),
        ]
    )
    store.save_bundle(store.load_state("demo"), graph)
    sup = Supervisor(tmp_path, execute=lambda _t: True)
    assert sup.run_once("demo").status == "VERIFIED"
    assert sup.run_once("demo").status == "VERIFIED"
    assert sup.run_once("demo").status == "COMPLETE"
