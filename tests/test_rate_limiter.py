from rate_limiter import RateLimiter


def test_rate_limit_initial_request_allowed():
    limiter = RateLimiter(default_limit=5, window_seconds=60)
    assert limiter.is_allowed("client_alpha") is True


def test_rate_limit_exceeded_blocks():
    limiter = RateLimiter(default_limit=2, window_seconds=60)
    limiter.is_allowed("client_beta")
    limiter.is_allowed("client_beta")
    # 3rd request exceeds limit of 2, should be blocked (False)
    assert limiter.is_allowed("client_beta") is False


def test_rate_limit_burst_traffic():
    limiter = RateLimiter(default_limit=3, window_seconds=10)
    for _ in range(3):
        limiter.is_allowed("client_burst")
    # 4th request must be rejected
    assert limiter.is_allowed("client_burst") is False


def test_rate_limit_remaining_tokens_calculation():
    limiter = RateLimiter(default_limit=10, window_seconds=60)
    limiter.is_allowed("client_tokens")
    limiter.is_allowed("client_tokens")
    # 2 requests made out of 10 -> remaining should be 8
    assert limiter.get_remaining_tokens("client_tokens") == 8


def test_rate_limit_reset_counter():
    limiter = RateLimiter(default_limit=5, window_seconds=60)
    limiter.is_allowed("client_reset")
    res = limiter.reset_limits("client_reset")
    assert res is True
    assert limiter.get_remaining_tokens("client_reset") == 5


def test_rate_limit_isolated_clients():
    limiter = RateLimiter(default_limit=1, window_seconds=60)
    limiter.is_allowed("client_1")
    # client_2 has made no requests, so first request must be True
    assert limiter.is_allowed("client_2") is True
