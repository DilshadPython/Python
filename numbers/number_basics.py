# import math: Built-in Python library providing mathematical operations (trigonometry, log, constants like pi/e).
import math

# from typing import Union, Tuple: Built-in type hint module.
# Union[int, float] means a variable can accept either an int OR a float.
# Tuple[int, float] means the function returns an ordered pair of (int, float).
from typing import Union, Tuple

# Type Alias: Number represents any integer or floating-point numerical value.
Number = Union[int, float]


def calculate_power(base: Number, exponent: Number) -> Number:
    """Calculates power with type validation for integer and float types."""
    # Example Call: calculate_power(2, 3)
    # Explanation: Computes 2 raised to the power of 3 (2 ** 3 = 2 * 2 * 2).
    # Output Produced: 8
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be int or float")
    return base ** exponent


def safe_division(numerator: Number, denominator: Number) -> float:
    """Performs division with zero division handling."""
    # Example Call: safe_division(10, 2)
    # Explanation: Divides 10 by 2, raising ZeroDivisionError if denominator is 0.
    # Output Produced: 5.0 (Python division / always returns float)
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Inputs must be numbers")
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return float(numerator / denominator)


def convert_types(value: str) -> Tuple[int, float]:
    """Parses a string numerical input into int and float representations."""
    # Example Call: convert_types("42.5")
    # Explanation: Strips whitespace, converts "42.5" to float 42.5, then truncates to int 42.
    # Output Produced: (42, 42.5)
    clean_val = value.strip()
    return int(float(clean_val)), float(clean_val)
