import pytest
from inventory_service import check_availability, deduct_stock, calculate_reorder_quantity

def test_check_availability_sufficient():
    inv = {"SKU-100": 50, "SKU-200": 10}
    assert check_availability(inv, "SKU-100", 5) is True

def test_check_availability_exact_match():
    inv = {"SKU-100": 5}
    assert check_availability(inv, "SKU-100", 5) is True

def test_check_availability_insufficient():
    inv = {"SKU-100": 2}
    assert check_availability(inv, "SKU-100", 10) is False

def test_deduct_stock_normal():
    inv = {"SKU-A": 100}
    result = deduct_stock(inv, "SKU-A", 20)
    assert result["SKU-A"] == 80

def test_deduct_stock_to_zero():
    inv = {"SKU-B": 15}
    result = deduct_stock(inv, "SKU-B", 15)
    assert result["SKU-B"] == 0

def test_calculate_reorder_normal():
    # Current stock 20, target 100 -> need 80
    assert calculate_reorder_quantity(20, 100) == 80

def test_calculate_reorder_low_stock():
    # Current stock 5, target 50 -> need 45
    assert calculate_reorder_quantity(5, 50) == 45

def test_calculate_reorder_zero_stock():
    # Current stock 0, target 200 -> need 200
    assert calculate_reorder_quantity(0, 200) == 200
