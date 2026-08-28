from runtime.verification import VerificationEngine


def test_verify_passes_when_all_checks_pass() -> None:
    result = VerificationEngine().verify(
        [("first", lambda: True), ("second", lambda: 1 == 1)]
    )

    assert result.status == "VERIFIED"
    assert result.passed == 2
    assert result.failed == 0
    assert result.details == ("first: PASS", "second: PASS")


def test_verify_fails_when_a_check_returns_false() -> None:
    result = VerificationEngine().verify(
        [("ok", lambda: True), ("bad", lambda: False)]
    )

    assert result.status == "FAILED"
    assert result.passed == 1
    assert result.failed == 1
    assert result.details == ("ok: PASS", "bad: FAIL")


def test_verify_treats_check_exception_as_failure() -> None:
    def broken() -> bool:
        raise RuntimeError("verification unavailable")

    result = VerificationEngine().verify([("broken", broken)])

    assert result.status == "FAILED"
    assert result.passed == 0
    assert result.failed == 1
    assert result.details == ("broken: RuntimeError: verification unavailable",)
