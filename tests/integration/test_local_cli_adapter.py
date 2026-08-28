from pathlib import Path

from adapters.local_cli import LocalCliAdapter
from runtime.models import Task
from runtime.store import Store
from runtime.supervisor import Supervisor
from runtime.graph import TaskGraph


def test_local_cli_touch_and_file_exists(tmp_path: Path):
    host = LocalCliAdapter(tmp_path)
    task = Task(
        id="t1",
        objective="create marker",
        notes="touch:out/marker.txt",
        acceptance_criteria=["file_exists:out/marker.txt"],
    )
    assert host.execute(task) is True
    checks = host.checks_for(task)
    assert all(fn() for _, fn in checks)


def test_supervisor_with_local_cli(tmp_path: Path):
    host = LocalCliAdapter(tmp_path)
    store = Store(tmp_path)
    graph = TaskGraph(
        [
            Task(
                id="mk",
                objective="marker",
                notes="touch:done.txt",
                acceptance_criteria=["file_exists:done.txt"],
            )
        ]
    )
    store.save_bundle(store.load_state("p"), graph)
    sup = Supervisor(tmp_path, execute=host.execute, checks=host.checks_for)
    result = sup.run_once("p")
    assert result.status == "VERIFIED"
    assert (tmp_path / "done.txt").is_file()
