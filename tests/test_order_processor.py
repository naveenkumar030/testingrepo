import pytest
from order_processor import apply_discount, compute_tax_ratio

def test_discount_calculation():
    # 20% discount on $100 should yield $80
    assert apply_discount(100.0, 20.0) == 80.0

def test_zero_subtotal_tax():
    # Free item with $0 subtotal should return 0.0% tax, NOT crash with ZeroDivisionError
    assert compute_tax_ratio(0.0, 0.0) == 0.0
