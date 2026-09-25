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

def test_standardize_user_profile_with_alice():
    raw_payload = {
        "id": 102,
        "name": "Alice Smith",
        "email": "Alice@Example.com"
    }
    result = standardize_user_profile(raw_payload)
    assert result["display_name"] == "Alice Smith"

def test_standardize_user_profile_with_bob():
    raw_payload = {
        "id": 103,
        "name": "Bob Jones",
        "email": "Bob@Test.org"
    }
    result = standardize_user_profile(raw_payload)
    assert result["display_name"] == "Bob Jones"

def test_standardize_user_profile_with_charlie():
    raw_payload = {
        "id": 104,
        "name": "Charlie Brown",
        "email": "charlie@peanuts.org"
    }
    result = standardize_user_profile(raw_payload)
    assert result["display_name"] == "Charlie Brown"

def test_standardize_user_profile_with_david():
    raw_payload = {
        "id": 105,
        "name": "David Miller",
        "email": "david@company.io"
    }
    result = standardize_user_profile(raw_payload)
    assert result["display_name"] == "David Miller"

def test_standardize_user_profile_with_emma():
    raw_payload = {
        "id": 106,
        "name": "Emma Watson",
        "email": "emma@cinema.com"
    }
    result = standardize_user_profile(raw_payload)
    assert result["display_name"] == "Emma Watson"
