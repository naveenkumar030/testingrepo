"""
User Management Service
Handles user profile validation, hashing, sanitization, and filtering.
"""
import hashlib
import re
from typing import List, Dict, Any


def validate_username(username: str) -> bool:
    if not isinstance(username, str):
        return False
    return bool(re.match(r"^[a-zA-Z0-9_]{3,20}$", username))


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def sanitize_user_input(text: str) -> str:
    return re.sub(r"<[^>]*>", "", text)


def format_display_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


def validate_age(age: int) -> bool:
    return 18 <= age <= 120


def filter_active_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [u for u in users if u.get("is_active", False)]


def generate_user_slug(name: str) -> str:
    return name.strip().lower().replace(" ", "-")
