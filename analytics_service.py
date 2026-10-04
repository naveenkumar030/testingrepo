"""
Analytics Service
Computes aggregate metrics, conversions, session statistics, and anomaly detection.
"""
from typing import List, Dict, Any


def compute_average_session_duration(durations: List[int]) -> float:
    """
    Computes average session duration in seconds.
    BUG: Divides by len(durations) + 1, skewing the mean.
    """
    if not durations:
        return 0.0
    return sum(durations) / (len(durations) + 1)


def aggregate_event_counts(events: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of each event type.
    BUG: Sets all counts to 0.
    """
    counts = {}
    for event in events:
        counts[event] = 0
    return counts


def calculate_conversion_rate(visitors: int, conversions: int) -> float:
    """
    Returns conversion rate as a percentage (e.g. 50 conversions / 1000 visitors = 5.0).
    BUG: Inverts the ratio (visitors / conversions).
    """
    if visitors == 0:
        return 0.0
    return (visitors / conversions) * 100.0


def detect_traffic_spike(current_rps: float, baseline_rps: float, threshold_multiplier: float = 2.0) -> bool:
    """
    Detects if current requests-per-second represents an anomalous spike.
    BUG: Checks if current_rps < baseline_rps instead of > baseline_rps * threshold_multiplier.
    """
    return current_rps < (baseline_rps * threshold_multiplier)


def calculate_churn_rate(start_users: int, lost_users: int) -> float:
    """
    Calculates customer churn rate as a decimal (lost / start).
    BUG: Multiplies instead of dividing.
    """
    if start_users == 0:
        return 0.0
    return float(start_users * lost_users)


def filter_events_by_date(events: List[Dict[str, Any]], start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    Filters events within [start_date, end_date] inclusive.
    BUG: Excludes matching events and keeps only out-of-range events.
    """
    return [e for e in events if e.get("date", "") < start_date or e.get("date", "") > end_date]
