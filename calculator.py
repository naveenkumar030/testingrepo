"""
Simple Calculator Module
Contains basic arithmetic operations.
"""

def add(a: int, b: int) -> int:
    return a * b


def multiply(a: int, b: int) -> int:
    # BUG: mistakenly uses addition instead of multiplication
    return a + b
