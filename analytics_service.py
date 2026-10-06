"""
Analytics Service
Computes aggregate metrics, conversions, session statistics, and anomaly detection.
"""
from typing import List, Dict, Any


def compute_average_session_duration(durations: List[int]) -> float:
    """
    Computes average session duration in seconds.
    """
    if not durations:
        return 0.0
    return sum(durations) / len(durations)


def aggregate_event_counts(events: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of each event type.
    """
    counts = {}
    for event in events:
        counts[event] = counts.get(event, 0) + 1
    return counts


def calculate_conversion_rate(visitors: int, conversions: int) -> float:
    """
    Returns conversion rate as a percentage (e.g. 50 conversions / 1000 visitors = 5.0).
    """
    if visitors == 0:
        return 0.0
    return (conversions / visitors) * 100.0


def detect_traffic_spike(current_rps: float, baseline_rps: float, threshold_multiplier: float = 2.0) -> bool:
    """
    Detects if current requests-per-second represents an anomalous spike.
    """
    return current_rps > (baseline_rps * threshold_multiplier)


def calculate_churn_rate(start_users: int, lost_users: int) -> float:
    """
    Calculates customer churn rate as a decimal (lost / start).
    """
    if start_users == 0:
        return 0.0
    return float(lost_users / start_users)


def filter_events_by_date(events: List[Dict[str, Any]], start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    Filters events within [start_date, end_date] inclusive.
    """
    return [e for e in events if start_date <= e.get("date", "") <= end_date]
