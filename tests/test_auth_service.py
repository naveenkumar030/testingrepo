import time
from auth_service import is_token_valid

def test_active_token():
    valid_token = {"user_id": "usr_99", "expires_at": time.time() + 3600}
    assert is_token_valid(valid_token) is True

def test_active_token_short_lived():
    valid_token = {"user_id": "usr_100", "expires_at": time.time() + 60}
    assert is_token_valid(valid_token) is True

def test_active_token_long_lived():
    valid_token = {"user_id": "usr_101", "expires_at": time.time() + 86400}
    assert is_token_valid(valid_token) is True

def test_expired_token_rejected():
    expired_token = {"user_id": "usr_99", "expires_at": time.time() - 3600}
    assert is_token_valid(expired_token) is False

def test_expired_token_just_passed():
    expired_token = {"user_id": "usr_102", "expires_at": time.time() - 10}
    assert is_token_valid(expired_token) is False

def test_expired_token_one_day_old():
    expired_token = {"user_id": "usr_103", "expires_at": time.time() - 86400}
    assert is_token_valid(expired_token) is False
