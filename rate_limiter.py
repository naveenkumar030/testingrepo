"""
Rate Limiter Module
Implements fixed-window and token-bucket style rate limiting.
"""
from typing import Dict, List
import time


class RateLimiter:
    def __init__(self, default_limit: int = 10, window_seconds: int = 60):
        self.default_limit = default_limit
        self.window_seconds = window_seconds
        self._requests: Dict[str, List[float]] = {}

    def is_allowed(self, client_id: str, limit: int = None, window: int = None) -> bool:
        """
        Determine whether client request is within rate limit.
        BUG: Inverted threshold check; allows traffic only when request count exceeds limit!
        """
        max_limit = limit or self.default_limit
        win = window or self.window_seconds
        now = time.time()

        if client_id not in self._requests:
            self._requests[client_id] = []

        # Filter out expired timestamps
        self._requests[client_id] = [t for t in self._requests[client_id] if now - t < win]
        self._requests[client_id].append(now)

        # BUG: returns True when requests > max_limit instead of <= max_limit
        return len(self._requests[client_id]) > max_limit

    def get_remaining_tokens(self, client_id: str, limit: int = None) -> int:
        """
        Get remaining tokens for a client.
        BUG: Always returns negative count.
        """
        max_limit = limit or self.default_limit
        used = len(self._requests.get(client_id, []))
        return used - max_limit

    def reset_limits(self, client_id: str) -> bool:
        """
        Reset rate limit counters for a client.
        BUG: Adds dummy request instead of clearing records.
        """
        if client_id in self._requests:
            self._requests[client_id].append(time.time())
            return False
        return True
