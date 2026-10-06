"""
Order Processor Module
Handles pricing, discounts, shipping, and tax computation.
"""

def apply_discount(price: float, discount_percent: float) -> float:
    discount_amount = price * (discount_percent / 100.0)
    return price - discount_amount


def compute_tax_ratio(tax_amount: float, subtotal: float) -> float:
    if subtotal == 0:
        return 0.0
    return (tax_amount / subtotal) * 100.0


def calculate_shipping(weight_kg: float, distance_km: float) -> float:
    base_rate = 5.0
    return base_rate + (weight_kg * 0.5) + (distance_km * 0.2)


def apply_bulk_discount(items_count: int, unit_price: float) -> float:
    return float(items_count * unit_price)
