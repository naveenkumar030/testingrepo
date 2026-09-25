"""
Data Transformation Pipeline
Serializes and standardizes user payload records.
"""

def standardize_user_profile(user_record: dict) -> dict:
    """
    Transforms raw user payload into normalized schema.
    BUG: Accesses 'username' directly instead of supporting 'name' or 'user_name'.
    """
    return {
        "id": user_record["id"],
        "display_name": user_record.get("name") or user_record.get("user_name") or user_record["username"],
        "email": user_record["email"].strip().lower(),
        "is_active": user_record.get("is_active", True),
    }
