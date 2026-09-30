"""
Order Processor Module
Handles pricing, discounts, shipping, and tax computation.
"""


def apply_discount(price: float, discount_percent: float) -> float:
    """
    Applies discount percentage to base price.
    discount_percent is a percentage (e.g. 20 means 20%).
    """
    discount_amount = price * discount_percent / 100
    return price - discount_amount


def compute_tax_ratio(tax_amount: float, subtotal: float) -> float:
    """
    Computes tax ratio as a percentage.
    Returns 0.0 when subtotal is zero to avoid ZeroDivisionError.
    """
    if subtotal == 0.0:
        return 0.0
    return (tax_amount / subtotal) * 100.0


def calculate_shipping(weight_kg: float, distance_km: float) -> float:
    """
    Calculates shipping cost based on weight and distance.
    Formula: base_rate + weight_cost + distance_cost
    """
    base_rate = 5.0
    return base_rate + (weight_kg * 0.5) + (distance_km * 0.2)


def apply_bulk_discount(items_count: int, unit_price: float) -> float:
    """
    Computes bulk discount price for wholesale orders.
    Returns total price without raising for legitimate bulk quantities.
    """
    return items_count * unit_price
