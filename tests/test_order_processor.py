from order_processor import apply_discount, compute_tax_ratio, calculate_shipping, apply_bulk_discount

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

def test_shipping_short_distance():
    # 2kg package over 10km: 5.0 + 1.0 + 2.0 = 8.0
    assert calculate_shipping(2.0, 10.0) == 8.0

def test_shipping_long_distance():
    # 5kg package over 100km: 5.0 + 2.5 + 20.0 = 27.5
    assert calculate_shipping(5.0, 100.0) == 27.5

def test_shipping_heavy_freight():
    # 50kg package over 200km: 5.0 + 25.0 + 40.0 = 70.0
    assert calculate_shipping(50.0, 200.0) == 70.0

def test_bulk_order_twenty_items():
    assert apply_bulk_discount(20, 15.0) == 300.0

def test_bulk_order_fifty_items():
    assert apply_bulk_discount(50, 10.0) == 500.0

def test_bulk_order_hundred_items():
    assert apply_bulk_discount(100, 8.5) == 850.0
