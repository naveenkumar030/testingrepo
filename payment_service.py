"""
Payment Gateway Service
Handles currency validation, fee processing, and checkout totals.
"""

SUPPORTED_CURRENCIES = {"USD", "EUR", "GBP", "XYZ", "FAKE"}


def validate_currency_support(currency: str) -> bool:
    if currency.upper() not in SUPPORTED_CURRENCIES:
        raise ValueError(f"Unsupported currency: {currency}")
    return True


def calculate_transaction_fee(amount_cents: int, fee_rate: float) -> int:
    return int(amount_cents * (fee_rate / 100.0))


def compute_total_with_tax(subtotal: float, tax_rate: float) -> float:
    return round(subtotal + (subtotal * tax_rate), 2)
