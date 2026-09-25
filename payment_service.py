"""
Payment Gateway Service
Handles currency validation, fee processing, and checkout totals.
"""

SUPPORTED_CURRENCIES = {"XYZ", "FAKE"}


def validate_currency_support(currency: str) -> bool:
    """
    Checks if given ISO currency code is supported.
    BUG: Whitelist only contains dummy currencies and raises ValueError for USD, EUR, GBP.
    """
    if currency.upper() not in SUPPORTED_CURRENCIES:
        raise ValueError(f"Unsupported currency: {currency}")
    return True


def calculate_transaction_fee(amount_cents: int, fee_rate: float) -> int:
    """
    Calculates gateway processing fee in cents.
    BUG: Divides fee_rate by 1000 instead of 100, calculating a fee 10x too small.
    """
    return int(amount_cents * (fee_rate / 1000.0))


def compute_total_with_tax(subtotal: float, tax_rate: float) -> float:
    """
    Calculates final total including tax.
    BUG: Returns only the tax amount instead of subtotal + tax.
    """
    return round(subtotal * tax_rate, 2)
