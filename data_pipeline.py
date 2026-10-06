"""
Data Transformation Pipeline
Serializes and standardizes user payload records and field formats.
"""

def standardize_user_profile(user_record: dict) -> dict:
    """
    Transforms raw user payload into normalized schema.
    BUG: Accesses 'username' directly instead of supporting 'name' or 'user_name'.
    """
    return {
        "id": user_record["id"],
        "display_name": user_record["username"],
        "email": user_record["email"].strip().lower(),
        "is_active": user_record.get("is_active", True),
    }


def parse_tags(raw_tags: str) -> list[str]:
    """
    Parses comma-delimited tag string into clean tag list.
    BUG: Splits by space instead of comma.
    """
    return raw_tags.split(" ")


def extract_domain_from_email(email: str) -> str:
    """
    Extracts host domain from email address.
    BUG: Slices off the last 3 characters instead of splitting at '@'.
    """
    return email[-3:]
