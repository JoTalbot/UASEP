from pathlib import Path

from runtime.models import Task, TaskStatus
from runtime.multi_agent import MultiAgentCoordinator
from runtime.supervisor import Supervisor


def test_parallel_runtime_persists_completion(tmp_path: Path):
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-a")
    coordinator.register("agent-b")
    supervisor = Supervisor.with_project_runtime(tmp_path, executor=lambda task: True, multi_agent=coordinator)
    tasks = [Task("A", "first", write_set=["a.py"]), Task("B", "second", write_set=["b.py"])]

    results = supervisor.run_parallel_once("demo", tasks)
    state = supervisor.state_store.load("demo")

    assert results == [("agent-a", "A", True), ("agent-b", "B", True)]
    assert state.completed_tasks == {"A", "B"}
    assert state.current_task is None
    assert state.iteration == 1
    assert all(task.status == TaskStatus.DONE for task in tasks)


def test_parallel_runtime_does_not_run_write_conflicts_together(tmp_path: Path):
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-a")
    coordinator.register("agent-b")
    supervisor = Supervisor.with_project_runtime(tmp_path, executor=lambda task: True, multi_agent=coordinator)
    tasks = [Task("A", "first", write_set=["shared.py"]), Task("B", "second", write_set=["shared.py"])]

    results = supervisor.run_parallel_once("demo", tasks)

    assert results == [("agent-a", "A", True)]
    assert tasks[0].status == TaskStatus.DONE
    assert tasks[1].status in {TaskStatus.READY, TaskStatus.BACKLOG}


def test_parallel_runtime_applies_acceptance_verification(tmp_path: Path):
    coordinator = MultiAgentCoordinator()
    coordinator.register("agent-a")
    supervisor = Supervisor.with_project_runtime(
        tmp_path,
        executor=lambda task: True,
        multi_agent=coordinator,
        acceptance_provider=lambda task: [("must-pass", lambda: False)],
    )
    task = Task("A", "unverified")

    results = supervisor.run_parallel_once("demo", [task])
    state = supervisor.state_store.load("demo")

    assert results == [("agent-a", "A", True)]
    assert task.status == TaskStatus.FAILED
    assert task.id not in state.completed_tasks
    assert state.task_failures[task.id] == 1
    assert state.phase == "retrying"
