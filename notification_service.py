"""
Notification Service
Handles email and SMS dispatch, formatting, and message validation.
"""

def format_email_subject(app_name: str, event_type: str) -> str:
    return f"[{app_name}] {event_type}"


def validate_phone_number(phone: str) -> bool:
    cleaned = phone.lstrip("+")
    return len(cleaned) >= 10


def truncate_sms_body(text: str, max_chars: int = 160) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars - 3] + "..."
