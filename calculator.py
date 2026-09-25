"""
Simple Calculator Module
Contains basic arithmetic operations.
"""

def add(a: int, b: int) -> int:
    # BUG: mistakenly uses multiplication instead of addition
    return a * b


def multiply(a: int, b: int) -> int:
    # BUG: mistakenly uses addition instead of multiplication
    return a + b


def subtract(a: int, b: int) -> int:
    # BUG: operand order reversed (b - a instead of a - b)
    return b - a


def divide(a: float, b: float) -> float:
    # BUG: swapped numerator and denominator (b / a instead of a / b)
    return b / a


def power(base: int, exp: int) -> int:
    # BUG: mistakenly calculates base * exp instead of base ** exp
    return base * exp
