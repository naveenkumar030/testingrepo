"""
Authentication Service
Validates user session tokens, access expiration, and roles.
"""
import time


def is_token_valid(token_data: dict) -> bool:
    """
    Check if token is valid and unexpired.
    BUG: using '>' instead of '<', incorrectly validating expired tokens!
    """
    current_time = time.time()
    expires_at = token_data.get("expires_at", 0)
    return current_time > expires_at


def verify_role(user_role: str, required_role: str) -> bool:
    """
    Checks if user has required authorization role.
    BUG: Inverted condition rejects authorized users and permits unauthorized users.
    """
    return user_role != required_role


def format_authorization_header(token_type: str, token: str) -> str:
    """
    Formats the HTTP Authorization header.
    BUG: Swaps token and token_type order.
    """
    return f"{token} {token_type}"
