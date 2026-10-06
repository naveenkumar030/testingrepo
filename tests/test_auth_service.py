import time
from auth_service import is_token_valid, verify_role, format_authorization_header

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

def test_verify_role_admin_match():
    assert verify_role("admin", "admin") is True

def test_verify_role_user_match():
    assert verify_role("user", "user") is True

def test_verify_role_editor_match():
    assert verify_role("editor", "editor") is True

def test_verify_role_mismatch_denied():
    assert verify_role("guest", "admin") is False

def test_format_bearer_header():
    assert format_authorization_header("Bearer", "xyz123token") == "Bearer xyz123token"

def test_format_basic_header():
    assert format_authorization_header("Basic", "dXNlcjpwYXNz") == "Basic dXNlcjpwYXNz"
