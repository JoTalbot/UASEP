from runtime.anti_loop_v2 import StagnationDetector


def test_detector_trips_after_repeated_failures():
    detector = StagnationDetector(threshold=3)
    assert detector.observe("t", False) is False
    assert detector.observe("t", False) is False
    assert detector.observe("t", False) is True


def test_success_breaks_failure_sequence():
    detector = StagnationDetector(threshold=3)
    detector.observe("t", False)
    detector.observe("t", False)
    assert detector.observe("t", True) is False
