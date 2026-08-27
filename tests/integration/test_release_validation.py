from pathlib import Path

from runtime.development_contract import DevelopmentContract
from runtime.host_adapter import Capability, HostAdapter
from runtime.models import Task


def test_release_validation_exercises_full_lifecycle(tmp_path: Path):
    host = HostAdapter()
    executed: list[str] = []

    def execute(task: Task) -> bool:
        executed.append(task.id)
        return True

    host.register(Capability("project.execute", available=True), execute)
    tasks = [
        Task(id="a", title="A"),
        Task(id="b", title="B", dependencies=("a",)),
        Task(id="c", title="C", dependencies=("b",)),
    ]

    def accept(task: Task):
        return [("release-acceptance", lambda: True)]

    first = DevelopmentContract(tmp_path, "release", host).run(tasks, max_cycles=1, acceptance=accept)
    assert first.completed == ("a",)

    second = DevelopmentContract(tmp_path, "release", host).run(tasks, max_cycles=1, acceptance=accept)
    assert second.completed == ("a", "b")

    third = DevelopmentContract(tmp_path, "release", host).run(tasks, max_cycles=1, acceptance=accept)
    assert third.completed == ("a", "b", "c")
    assert executed == ["a", "b", "c"]
    assert (tmp_path / ".uasep" / "manifest.yaml").exists()
