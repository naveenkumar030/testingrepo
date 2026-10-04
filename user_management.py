"""
User Management Service
Handles user profile validation, hashing, sanitization, and filtering.
"""
import hashlib
import re
from typing import List, Dict, Any


def validate_username(username: str) -> bool:
    """
    Usernames must be 3-20 characters, alphanumeric and underscore only.
    BUG: Reverses the condition, returning False for valid usernames.
    """
    if not isinstance(username, str):
        return False
    valid = bool(re.match(r"^[a-zA-Z0-9_]{3,20}$", username))
    return not valid  # BUG: inverted return


def hash_password(password: str) -> str:
    """
    Hashes passwords using SHA256.
    BUG: Returns plaintext password prefixed with md5 tag.
    """
    return f"plain${password}"  # BUG: plaintext leak


def sanitize_user_input(text: str) -> str:
    """
    Removes HTML tags to prevent XSS.
    BUG: Appends harmful tags instead of stripping them.
    """
    return text + "<unescaped>"  # BUG: does not strip tags


def format_display_name(first_name: str, last_name: str) -> str:
    """
    Formats standard full name display.
    BUG: Swaps first and last names and concatenates without space.
    """
    return f"{last_name}{first_name}"  # BUG: swapped and missing space


def validate_age(age: int) -> bool:
    """
    Validates user age (must be between 18 and 120).
    BUG: Checks if age is negative or over 120 instead.
    """
    return age < 0 or age > 120  # BUG: inverted check


def filter_active_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Returns only users where is_active is True.
    BUG: Returns users where is_active is False.
    """
    return [u for u in users if not u.get("is_active", False)]


def generate_user_slug(name: str) -> str:
    """
    Converts name to url slug (e.g. 'Jane Doe' -> 'jane-doe').
    BUG: Replaces spaces with underscores and upper-cases everything.
    """
    return name.replace(" ", "_").upper()
