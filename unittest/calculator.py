"""
Provides basic arithmetic operations (addition, subtraction, multiplication, division, power)
with robust type annotations, docstrings, and defensive error handling for unit testing.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union

# Define numeric type alias for integers and floats
Numeric = Union[int, float]


def add(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Compute the sum of two numeric values.

    Args:
        num1 (Numeric): First operand.
        num2 (Numeric): Second operand.

    Returns:
        Numeric: Sum of num1 and num2.
    """
    return num1 + num2


def subtract(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Compute the difference between two numeric values.

    Args:
        num1 (Numeric): First operand.
        num2 (Numeric): Operand to subtract.

    Returns:
        Numeric: Result of num1 - num2.
    """
    return num1 - num2


def multiply(num1: Numeric, num2: Numeric) -> Numeric:
    """
    Compute the product of two numeric values.

    Args:
        num1 (Numeric): First operand.
        num2 (Numeric): Second operand.

    Returns:
        Numeric: Product of num1 and num2.
    """
    return num1 * num2


def divide(num1: Numeric, num2: Numeric) -> float:
    """
    Compute the quotient of two numeric values.

    Args:
        num1 (Numeric): Dividend operand.
        num2 (Numeric): Divisor operand.

    Returns:
        float: Quotient of num1 / num2.

    Raises:
        ValueError: If divisor (num2) is zero.
    """
    if num2 == 0:
        raise ValueError("Divisor cannot be zero.")
    return num1 / num2


def power(base: Numeric, exponent: Numeric) -> Numeric:
    """
    Compute base raised to the exponent power.

    Args:
        base (Numeric): Base number.
        exponent (Numeric): Exponent power.

    Returns:
        Numeric: Result of base ** exponent.
    """
    return base ** exponent


def square(number: Numeric) -> Numeric:
    """
    Compute the square of a numeric value.

    Args:
        number (Numeric): Number to square.

    Returns:
        Numeric: Result of number * number.
    """
    if isinstance(number, bool) or not isinstance(number, (int, float)):
        raise TypeError("Input number must be a valid int or float.")
    return number * number

