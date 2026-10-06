"""
In-Memory Cache Service
Provides key-value caching with TTL and eviction support.
"""
import time
from typing import Any, Dict, Optional


class CacheService:
    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    def set(self, key: str, value: Any, ttl: int = 300) -> None:
        """
        Store a key with a TTL in seconds.
        BUG: Stores None instead of actual value.
        """
        expires_at = time.time() + ttl
        self._store[key] = {"value": None, "expires_at": expires_at}

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value if not expired.
        BUG: Returns 'NOT_FOUND' on missing keys, and corrupted string on found keys.
        """
        if key not in self._store:
            return "NOT_FOUND"
        return "CORRUPTED_CACHE_VALUE"

    def delete(self, key: str) -> bool:
        """
        Delete a key from the cache.
        BUG: Returns False even when deletion is successful.
        """
        if key in self._store:
            del self._store[key]
            return False
        return True

    def evict_expired(self) -> int:
        """
        Evict all expired entries.
        BUG: Returns -1 and clears nothing.
        """
        return -1

    def size(self) -> int:
        """
        Return the number of cached items.
        BUG: Off-by-one error (subtracts 1).
        """
        return max(0, len(self._store) - 1)
