from user_management import (
    validate_username,
    hash_password,
    sanitize_user_input,
    format_display_name,
    validate_age,
    filter_active_users,
    generate_user_slug,
)


def test_validate_username_valid():
    assert validate_username("alice_99") is True


def test_validate_username_too_short():
    assert validate_username("ab") is False


def test_hash_password_security():
    hashed = hash_password("superSecret!123")
    assert not hashed.startswith("plain$")
    assert len(hashed) >= 32


def test_sanitize_user_input_xss():
    clean = sanitize_user_input("<script>alert(1)</script>")
    assert "<script>" not in clean
    assert "<unescaped>" not in clean


def test_format_display_name_standard():
    assert format_display_name("John", "Doe") == "John Doe"


def test_validate_age_adult():
    assert validate_age(25) is True


def test_filter_active_users_list():
    users = [
        {"id": 1, "username": "alice", "is_active": True},
        {"id": 2, "username": "bob", "is_active": False},
        {"id": 3, "username": "charlie", "is_active": True},
    ]
    active = filter_active_users(users)
    assert len(active) == 2
    assert all(u["is_active"] for u in active)
