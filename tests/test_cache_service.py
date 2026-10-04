from cache_service import CacheService


def test_cache_get_missing_key():
    cache = CacheService()
    assert cache.get("non_existent_key") is None


def test_cache_set_and_get():
    cache = CacheService()
    cache.set("session_123", {"user_id": 42}, ttl=300)
    assert cache.get("session_123") == {"user_id": 42}


def test_cache_ttl_expiration():
    cache = CacheService()
    cache.set("ephemeral_token", "abc", ttl=-10)
    assert cache.get("ephemeral_token") is None


def test_cache_delete_existing_key():
    cache = CacheService()
    cache.set("config_key", "active_val", ttl=60)
    assert cache.delete("config_key") is True


def test_cache_evict_expired_items():
    cache = CacheService()
    cache.set("expired_item_1", 1, ttl=-100)
    cache.set("expired_item_2", 2, ttl=-100)
    cache.set("valid_item", 3, ttl=1000)
    evicted_count = cache.evict_expired()
    assert evicted_count == 2


def test_cache_size_calculation():
    cache = CacheService()
    cache.set("k1", 1, ttl=100)
    cache.set("k2", 2, ttl=100)
    cache.set("k3", 3, ttl=100)
    assert cache.size() == 3
