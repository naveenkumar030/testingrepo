"""
Data Transformation Pipeline
Serializes and standardizes user payload records and field formats.
"""


def standardize_user_profile(user_record: dict) -> dict:
    """
    Transforms raw user payload into normalized schema.
    Supports both 'name' and 'username' keys for display name.
    """
    return {
        "id": user_record["id"],
        "display_name": user_record.get("name") or user_record.get("username", ""),
        "email": user_record["email"].strip().lower(),
        "is_active": user_record.get("is_active", True),
    }


def parse_tags(raw_tags: str) -> list[str]:
    """
    Parses comma-delimited tag string into clean tag list.
    """
    return raw_tags.split(",")


def extract_domain_from_email(email: str) -> str:
    """
    Extracts host domain from email address.
    """
    return email.split("@")[1]
