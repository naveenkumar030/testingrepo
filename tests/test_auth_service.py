import time
from auth_service import is_token_valid

def test_active_token():
    valid_token = {"user_id": "usr_99", "expires_at": time.time() + 3600}
    # An active future token should be valid
    assert is_token_valid(valid_token) is True

def test_expired_token_rejected():
    expired_token = {"user_id": "usr_99", "expires_at": time.time() - 3600}
    # An expired past token MUST be rejected
    assert is_token_valid(expired_token) is False
