from pathlib import Path

from runtime.execution import ExecutionEngine
from runtime.project_bootstrap import bootstrap_project
from runtime.supervisor_engine import Supervisor
from runtime.task_graph import TaskGraph, TaskNode


def test_end_to_end_autonomous_cycle(tmp_path: Path):
    bootstrap_project(tmp_path, "demo")
    graph = TaskGraph([
        TaskNode("discover", "Discover project", priority=10),
        TaskNode("implement", "Implement change", dependencies={"discover"}, priority=5),
        TaskNode("verify", "Verify change", dependencies={"implement"}, priority=5),
    ])
    supervisor = Supervisor(tmp_path, graph)
    engine = ExecutionEngine()

    def executor(task: TaskNode) -> bool:
        result = engine.execute(lambda: True)
        return result.success

    result = supervisor.run(executor)
    assert result.completed == ["discover", "implement", "verify"]
    assert result.blocked == []
    assert not result.stopped_for_stagnation
    assert len(supervisor.evidence.all()) == 3
