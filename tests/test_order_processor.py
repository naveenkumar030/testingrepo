import pytest
from order_processor import apply_discount, compute_tax_ratio

def test_discount_calculation():
    # 20% discount on $100 should yield $80
    assert apply_discount(100.0, 20.0) == 80.0

def test_discount_ten_percent():
    assert apply_discount(50.0, 10.0) == 45.0

def test_discount_fifty_percent():
    assert apply_discount(200.0, 50.0) == 100.0

def test_discount_five_percent():
    assert apply_discount(80.0, 5.0) == 76.0

def test_discount_twenty_five_percent():
    assert apply_discount(40.0, 25.0) == 30.0

def test_zero_subtotal_tax():
    # Free item with $0 subtotal should return 0.0% tax, NOT crash with ZeroDivisionError
    assert compute_tax_ratio(0.0, 0.0) == 0.0

def test_zero_subtotal_with_tax_amount():
    assert compute_tax_ratio(5.0, 0.0) == 0.0
