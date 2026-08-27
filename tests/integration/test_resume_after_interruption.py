from pathlib import Path

from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task
from runtime.runner import run_project


def test_resume_keeps_persisted_progress(tmp_path: Path):
    host = HostAdapter()
    calls: list[str] = []

    def execute(task: Task) -> bool:
        calls.append(task.id)
        return True

    host.register(Capability("project.execute", available=True), execute)
    tasks = [
        Task(id="a", title="A"),
        Task(id="b", title="B", dependencies=("a",)),
    ]

    first = run_project(tmp_path, "demo", tasks, max_cycles=1, host=host,
                        acceptance_provider=lambda task: [("acceptance", lambda: True)])
    assert first.completed == ("a",)

    second = run_project(tmp_path, "demo", tasks, max_cycles=1, host=host,
                         acceptance_provider=lambda task: [("acceptance", lambda: True)])
    assert second.completed == ("a", "b")
    assert calls == ["a", "b"]
