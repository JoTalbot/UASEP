from runtime.retry_policy import RetryPolicy


def test_retry_requires_strategy_change():
    policy = RetryPolicy(max_attempts=3)
    assert policy.decide("task", 0, "strategy-a").retry is True
    assert policy.decide("task", 1, "strategy-a").retry is False
    assert policy.decide("task", 1, "strategy-b").retry is True


def test_retry_stops_at_limit():
    policy = RetryPolicy(max_attempts=2)
    policy.decide("task", 0, "a")
    assert policy.decide("task", 2, "b").retry is False
