from runtime.replanning import Replanner
from runtime.task_graph import TaskGraph, TaskNode
from runtime.verification import VerificationEngine


def test_verification_requires_explicit_checks():
    result = VerificationEngine().verify([("build", lambda: True), ("test", lambda: False)])
    assert result.status == "FAILED"
    assert result.passed == 1
    assert result.failed == 1


def test_replanner_selects_independent_ready_task():
    graph = TaskGraph([TaskNode("a", "A"), TaskNode("b", "B", priority=10)])
    decision = Replanner().choose(graph, "a")
    assert decision.action == "CONTINUE"
    assert decision.task_id == "b"


def test_replanner_escalates_when_no_alternative():
    graph = TaskGraph([TaskNode("a", "A")])
    decision = Replanner().choose(graph, "a")
    assert decision.action == "ESCALATE"
