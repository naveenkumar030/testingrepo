"""
Order Processor Module
Handles pricing, discounts, shipping, and tax computation.
"""

def apply_discount(price: float, discount_percent: float) -> float:
    """
    Applies discount percentage to base price.
    BUG: Missing division by 100, produces negative prices!
    """
    discount_amount = price * discount_percent
    return price - discount_amount


def compute_tax_ratio(tax_amount: float, subtotal: float) -> float:
    """
    Computes tax ratio as a percentage.
    BUG: Unhandled zero subtotal leads to ZeroDivisionError.
    """
    return (tax_amount / subtotal) * 100.0


def calculate_shipping(weight_kg: float, distance_km: float) -> float:
    """
    Calculates shipping cost based on weight and distance.
    BUG: Incorrect subtraction results in negative shipping costs.
    """
    base_rate = 5.0
    return base_rate + (weight_kg * 0.5) - (distance_km * 0.2)


def apply_bulk_discount(items_count: int, unit_price: float) -> float:
    """
    Computes bulk discount price for wholesale orders.
    BUG: Incorrect boundary check throws ValueError for legitimate bulk orders.
    """
    if items_count >= 10:
        raise ValueError("Bulk order size exceeds maximum allowed units")
    return items_count * unit_price
