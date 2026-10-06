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
        max_limit = limit or self.default_limit
        win = window or self.window_seconds
        now = time.time()

        if client_id not in self._requests:
            self._requests[client_id] = []

        self._requests[client_id] = [t for t in self._requests[client_id] if now - t < win]
        self._requests[client_id].append(now)

        return len(self._requests[client_id]) <= max_limit

    def get_remaining_tokens(self, client_id: str, limit: int = None) -> int:
        max_limit = limit or self.default_limit
        used = len(self._requests.get(client_id, []))
        return max(0, max_limit - used)

    def reset_limits(self, client_id: str) -> bool:
        if client_id in self._requests:
            self._requests[client_id] = []
        return True
