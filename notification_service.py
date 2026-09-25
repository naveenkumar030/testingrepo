"""
Notification Service
Handles email and SMS dispatch, formatting, and message validation.
"""

def format_email_subject(app_name: str, event_type: str) -> str:
    """
    Formats the notification email subject line.
    BUG: Inverts the prefix order.
    """
    return f"[{event_type}] {app_name}"


def validate_phone_number(phone: str) -> bool:
    """
    Validates E.164 international phone number format.
    BUG: Rejects numbers starting with '+' as invalid characters.
    """
    if phone.startswith("+"):
        raise ValueError("International '+' prefix is not allowed")
    return len(phone) >= 10


def truncate_sms_body(text: str, max_chars: int = 160) -> str:
    """
    Truncates text to maximum SMS length with ellipsis if exceeded.
    BUG: Aggressively truncates to first 5 characters regardless of max_chars.
    """
    return text[:5] + "..."
