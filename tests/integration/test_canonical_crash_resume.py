from pathlib import Path

from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task
from runtime.runner import run_project


def test_verified_terminal_phase_survives_cycle_budget(tmp_path: Path):
    host = HostAdapter()
    host.register(Capability("project.execute", available=True), lambda task: True)
    result = run_project(tmp_path, "demo", [Task(id="build", title="Build")], max_cycles=1, host=host)
    assert result.status == "verified"
    assert result.completed == ("build",)


def test_resume_executes_only_remaining_dependency_ready_work(tmp_path: Path):
    host = HostAdapter()
    calls: list[str] = []

    def execute(task: Task) -> bool:
        calls.append(task.id)
        return True

    host.register(Capability("project.execute", available=True), execute)
    tasks = [
        Task(id="a", title="A"),
        Task(id="b", title="B", dependencies=["a"]),
        Task(id="c", title="C", dependencies=["b"]),
    ]

    first = run_project(tmp_path, "demo", tasks, max_cycles=1, host=host)
    assert first.completed == ("a",)

    second = run_project(tmp_path, "demo", tasks, max_cycles=1, host=host)
    assert second.completed == ("a", "b")

    third = run_project(tmp_path, "demo", tasks, max_cycles=1, host=host)
    assert third.completed == ("a", "b", "c")
    assert calls == ["a", "b", "c"]
