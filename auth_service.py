"""
Authentication Service
Validates user session tokens and access expiration.
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
