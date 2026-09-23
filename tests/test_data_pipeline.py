import pytest
from data_pipeline import standardize_user_profile

def test_standardize_user_profile():
    raw_payload = {
        "id": 101,
        "name": "Naveen Kumar",
        "email": "Naveen@Example.Com"
    }
    result = standardize_user_profile(raw_payload)
    assert result["display_name"] == "Naveen Kumar"
    assert result["email"] == "naveen@example.com"
