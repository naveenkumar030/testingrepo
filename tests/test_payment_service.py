import pytest
from payment_service import validate_currency_support, calculate_transaction_fee, compute_total_with_tax

def test_validate_usd_supported():
    assert validate_currency_support("USD") is True

def test_validate_eur_supported():
    assert validate_currency_support("EUR") is True

def test_validate_gbp_supported():
    assert validate_currency_support("GBP") is True

def test_calculate_fee_standard():
    # 2.9% fee on 10,000 cents ($100) -> 290 cents
    assert calculate_transaction_fee(10000, 2.9) == 290

def test_calculate_fee_micro():
    # 5.0% fee on 2,000 cents ($20) -> 100 cents
    assert calculate_transaction_fee(2000, 5.0) == 100

def test_compute_total_ten_percent_tax():
    # $100 subtotal + 10% tax = $110
    assert compute_total_with_tax(100.0, 0.10) == 110.0

def test_compute_total_five_percent_tax():
    # $50 subtotal + 5% tax = $52.5
    assert compute_total_with_tax(50.0, 0.05) == 52.5

def test_compute_total_twenty_percent_tax():
    # $200 subtotal + 20% tax = $240
    assert compute_total_with_tax(200.0, 0.20) == 240.0
