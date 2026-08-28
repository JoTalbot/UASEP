from pathlib import Path

from runtime.graph import TaskGraph
from runtime.models import Task, TaskStatus
from runtime.store import Store
from runtime.supervisor import Supervisor


def test_run_once_verifies_and_persists(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph(
        [
            Task(
                id="t1",
                objective="first",
                priority=10,
                acceptance_criteria=["always"],
            ),
            Task(
                id="t2",
                objective="second",
                priority=5,
                dependencies=["t1"],
                acceptance_criteria=["always"],
            ),
        ]
    )
    state = store.load_state("demo")
    state.objective = "demo"
    store.save_bundle(state, graph)

    sup = Supervisor(tmp_path, execute=lambda _t: True)
    r1 = sup.run_once("demo")
    assert r1.status == "VERIFIED"
    assert r1.task_id == "t1"

    loaded_graph = store.load_graph()
    assert loaded_graph.tasks["t1"].status == TaskStatus.VERIFIED

    r2 = sup.run_once("demo")
    assert r2.status == "VERIFIED"
    assert r2.task_id == "t2"

    r3 = sup.run_once("demo")
    assert r3.status == "COMPLETE"


def test_failed_verification_does_not_complete(tmp_path: Path):
    store = Store(tmp_path)
    graph = TaskGraph(
        [Task(id="bad", objective="bad", acceptance_criteria=["must-fail"])]
    )
    store.save_bundle(store.load_state("demo"), graph)

    def checks(task):
        return [(c, lambda: False) for c in task.acceptance_criteria]

    sup = Supervisor(tmp_path, execute=lambda _t: True, checks=checks)
    result = sup.run_once("demo")
    assert result.status == "FAILED"
    assert store.load_graph().tasks["bad"].status == TaskStatus.FAILED
