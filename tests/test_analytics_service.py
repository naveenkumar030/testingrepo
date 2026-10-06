from analytics_service import (
    compute_average_session_duration,
    aggregate_event_counts,
    calculate_conversion_rate,
    detect_traffic_spike,
    calculate_churn_rate,
    filter_events_by_date,
)


def test_compute_average_session_duration():
    # 60 + 120 + 180 = 360 / 3 = 120.0
    assert compute_average_session_duration([60, 120, 180]) == 120.0


def test_aggregate_event_counts_standard():
    events = ["page_view", "click", "page_view", "signup"]
    counts = aggregate_event_counts(events)
    assert counts == {"page_view": 2, "click": 1, "signup": 1}


def test_calculate_conversion_rate_percentage():
    # 50 conversions out of 1000 visitors = 5.0%
    assert calculate_conversion_rate(1000, 50) == 5.0


def test_detect_traffic_spike_triggered():
    # 600 rps with 200 baseline and 2.0x threshold (400) -> should be True (spike detected)
    assert detect_traffic_spike(600.0, 200.0, 2.0) is True


def test_calculate_churn_rate_basic():
    # 50 lost out of 1000 start users = 0.05
    assert calculate_churn_rate(1000, 50) == 0.05


def test_filter_events_by_date_range():
    events = [
        {"id": 1, "date": "2026-10-01"},
        {"id": 2, "date": "2026-10-02"},
        {"id": 3, "date": "2026-10-03"},
        {"id": 4, "date": "2026-10-10"},
    ]
    filtered = filter_events_by_date(events, "2026-10-01", "2026-10-03")
    assert len(filtered) == 3
    assert [e["id"] for e in filtered] == [1, 2, 3]
