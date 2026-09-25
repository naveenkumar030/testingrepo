import pytest
from notification_service import format_email_subject, validate_phone_number, truncate_sms_body

def test_format_order_placed_subject():
    assert format_email_subject("MyApp", "Order Placed") == "[MyApp] Order Placed"

def test_format_password_reset_subject():
    assert format_email_subject("StoreHub", "Password Reset") == "[StoreHub] Password Reset"

def test_validate_international_us_number():
    assert validate_phone_number("+14155552671") is True

def test_validate_international_uk_number():
    assert validate_phone_number("+442071838750") is True

def test_validate_international_in_number():
    assert validate_phone_number("+919876543210") is True

def test_truncate_sms_within_limit():
    short_text = "Your verification code is 482910."
    assert truncate_sms_body(short_text, max_chars=160) == short_text

def test_truncate_sms_standard_sentence():
    # 70-character message should fit easily within 160 chars
    msg = "Hello! Your package has been picked up by the courier and is on its way."
    assert truncate_sms_body(msg, max_chars=160) == msg
