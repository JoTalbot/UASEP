from pathlib import Path

from runtime.models import Task
from runtime.multi_agent import MultiAgentCoordinator
from runtime.supervisor import Supervisor


def test_supervisor_parallel_once(tmp_path: Path):
    coord = MultiAgentCoordinator()
    coord.register("w1")
    coord.register("w2")
    sup = Supervisor.with_project_runtime(tmp_path, executor=lambda _t: True)
    sup.multi_agent = coord
    tasks = [
        Task("a", "A", write_set=["f1"]),
        Task("b", "B", write_set=["f2"]),
    ]
    results = sup.run_parallel_once("demo", tasks)
    assert len(results) == 2
    assert {r[1] for r in results} == {"a", "b"}
    assert all(r[2] for r in results)
    state = sup.state_store.load("demo")
    assert state.completed_tasks >= {"a", "b"}
