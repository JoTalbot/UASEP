from pathlib import Path

from runtime.anti_loop import StagnationDetector
from runtime.models import Task, TaskStatus
from runtime.planner import Planner
from runtime.state import StateStore


def test_planner_respects_dependencies():
    tasks = [
        Task("A", "first", priority=10),
        Task("B", "second", priority=100, dependencies=["A"]),
    ]
    planner = Planner()
    assert planner.next_task(tasks, set()).id == "A"
    assert planner.next_task(tasks, {"A"}).id == "B"


def test_planner_retries_failed_task_within_budget():
    task = Task("A", "retry", status=TaskStatus.FAILED, failure_count=1)
    assert Planner().next_task([task], set(), max_failures=3) is task


def test_planner_excludes_exhausted_failed_task():
    task = Task("A", "exhausted", status=TaskStatus.FAILED, failure_count=3)
    assert Planner().next_task([task], set(), max_failures=3) is None


def test_planner_tie_breaks_by_id():
    tasks = [Task("B", "second", priority=10), Task("A", "first", priority=10)]
    assert Planner().next_task(tasks, set()).id == "A"


def test_state_round_trip(tmp_path: Path):
    store = StateStore(tmp_path)
    state = store.load("demo")
    state.phase = "verified"
    state.completed_tasks.add("A")
    store.save(state)
    restored = store.load("demo")
    assert restored.phase == "verified"
    assert "A" in restored.completed_tasks


def test_stagnation_detector():
    detector = StagnationDetector(window=3)
    detector.record("x")
    detector.record("x")
    assert not detector.stagnant
    detector.record("x")
    assert detector.stagnant
