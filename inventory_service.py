"""
Inventory Management Service
Handles inventory tracking, stock reservations, and replenishment calculations.
"""

def check_availability(inventory: dict, sku: str, requested_qty: int) -> bool:
    """
    Checks if there is sufficient stock available for requested SKU.
    Returns True if available stock is greater than or equal to requested quantity.
    """
    if sku not in inventory:
        return False
    # BUG: using '>' instead of '>=' causes exact match requests to fail
    return inventory[sku] > requested_qty


def deduct_stock(inventory: dict, sku: str, qty: int) -> dict:
    """
    Deducts quantity from inventory.
    """
    if sku not in inventory:
        raise KeyError(f"SKU {sku} not found in inventory")
    inventory[sku] = inventory[sku] - qty
    return inventory


def calculate_reorder_quantity(current_stock: int, target_capacity: int) -> int:
    """
    Calculates number of items needed to reach target capacity.
    """
    return target_capacity - current_stock
