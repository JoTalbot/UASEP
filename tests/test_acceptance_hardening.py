import pytest

from runtime.acceptance import AcceptanceEngine


def test_blank_acceptance_description_is_rejected():
    with pytest.raises(ValueError, match="description must not be empty"):
        AcceptanceEngine().evaluate([("   ", lambda: True)])


def test_non_callable_acceptance_check_is_rejected():
    with pytest.raises(TypeError, match="must be callable"):
        AcceptanceEngine().evaluate([("criterion", None)])


def test_check_exception_remains_a_failed_auditable_result():
    results = AcceptanceEngine().evaluate(
        [("criterion", lambda: 1 / 0)]
    )

    assert len(results) == 1
    assert results[0].criterion == "criterion"
    assert results[0].passed is False
    assert "ZeroDivisionError" in results[0].detail
