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
        expires_at = time.time() + ttl
        self._store[key] = {"value": value, "expires_at": expires_at}

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        item = self._store[key]
        if time.time() > item["expires_at"]:
            del self._store[key]
            return None
        return item["value"]

    def delete(self, key: str) -> bool:
        if key in self._store:
            del self._store[key]
            return True
        return False

    def evict_expired(self) -> int:
        now = time.time()
        expired_keys = [k for k, v in self._store.items() if now > v["expires_at"]]
        for k in expired_keys:
            del self._store[k]
        return len(expired_keys)

    def size(self) -> int:
        return len(self._store)
