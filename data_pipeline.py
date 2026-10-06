"""
Data Transformation Pipeline
Serializes and standardizes user payload records and field formats.
"""

def standardize_user_profile(user_record: dict) -> dict:
    """
    Transforms raw user payload into normalized schema.
    """
    display_name = user_record.get("username") or user_record.get("name") or user_record.get("user_name", "")
    return {
        "id": user_record["id"],
        "display_name": display_name,
        "email": user_record["email"].strip().lower(),
        "is_active": user_record.get("is_active", True),
    }


def parse_tags(raw_tags: str) -> list[str]:
    """
    Parses comma-delimited tag string into clean tag list.
    """
    return [t.strip() for t in raw_tags.split(",") if t.strip()]


def extract_domain_from_email(email: str) -> str:
    """
    Extracts host domain from email address.
    """
    return email.split("@")[-1]
