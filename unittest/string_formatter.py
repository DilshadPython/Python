"""
Provides text formatting, square calculation utilities, and input validation functions.
"""
# "from module import name" imports type annotations directly into local scope.
from typing import Union

Numeric = Union[int, float]


def format_welcome_message(name: str = 'Python') -> str:
    """
    Format a welcome greeting string for a given name.

    Args:
        name (str): Person or system name to greet.

    Returns:
        str: Formatted welcome greeting string.
    """
    clean_name = str(name).strip()
    if not clean_name:
        clean_name = 'Guest'
    return f"Welcome back to, {clean_name}"


def square_number(number: Numeric) -> Numeric:
    """
    Calculate the square of a given integer or float.

    Args:
        number (Numeric): Number to square.

    Returns:
        Numeric: Result of number * number.

    Raises:
        TypeError: If number is a boolean or non-numeric type.
    """
    if isinstance(number, bool) or not isinstance(number, (int, float)):
        raise TypeError("Input number must be a valid int or float.")
    return number * number
