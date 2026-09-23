"""
Order Processor Module
Handles pricing, discounts, and tax computation.
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
