"""Number Formatting Demonstration Module.

This module demonstrates floating-point precision control, thousand-separator
formatting for large integers, and data size display utilities in Python.
"""

# import math for pi constant reference
import math
from typing import Union


def format_float_precision(value: float, precision: int = 2) -> str:
    """Format a floating-point number to a specified number of decimal places.

    Args:
        value: Floating-point number to format.
        precision: Number of decimal places (inclusive). Defaults to 2.

    Returns:
        str: Formatted representation of the float.

    Raises:
        TypeError: If value is not numeric or precision is not an integer.
        ValueError: If precision is negative.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"value must be numeric, got {type(value).__name__}")
    if not isinstance(precision, int):
        raise TypeError(f"precision must be an integer, got {type(precision).__name__}")
    if precision < 0:
        raise ValueError(f"precision must be non-negative, got {precision}")

    return f"The Pi is = {value:.{precision}f}"


def format_large_number(number: int, unit: str = "Byte") -> str:
    """Format large integers using commas as thousands separators.

    Args:
        number: Integer value to format.
        unit: Optional unit suffix string (e.g., 'Byte'). Defaults to 'Byte'.

    Returns:
        str: Formatted string with comma separation.

    Raises:
        TypeError: If number is not an integer or unit is not a string.
    """
    if not isinstance(number, int):
        raise TypeError(f"number must be an integer, got {type(number).__name__}")
    if not isinstance(unit, str):
        raise TypeError(f"unit must be a string, got {type(unit).__name__}")

    if unit:
        return f"{number:,} {unit}".strip()
    return f"{number:,}"


def print_number_formatting_demos() -> None:
    """Execute number formatting demonstrations."""
    pi_val = math.pi  # ~3.1415926535...
    print("=== Float Precision Formatting ===")
    print(format_float_precision(pi_val, precision=2))

    print("\n=== Large Integer Thousand Separator Formatting ===")
    mb_bytes = 1000**2
    gb_bytes = 1073741824

    print(f"1 MB is = {format_large_number(mb_bytes, unit='')}")
    print(f"1 GB is = {format_large_number(gb_bytes, unit='Byte')}")


if __name__ == "__main__":
    print_number_formatting_demos()
