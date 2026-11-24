"""Fraction Arithmetic & Comparison Operators Module.

Provides functions demonstrating exact rational arithmetic and comparison operations:
- Arithmetic operators: +, -, *, /, //, %, **
- Built-in functions: divmod(), abs(), round()
- Relational comparisons: ==, !=, >, <, >=, <=
- Mixed-type operations: Arithmetic between Fraction, int, and float
"""

from fractions import Fraction
from typing import Dict, Tuple, Union


def perform_fraction_arithmetic(
    a: Fraction, b: Fraction
) -> Dict[str, Union[Fraction, float]]:
    """Perform core arithmetic operations between two Fraction instances.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Dictionary of arithmetic operation results.
    """
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor_division": a // b,
        "modulo": a % b,
        "exponentiation": a ** 2,
    }


def calculate_fraction_divmod(a: Fraction, b: Fraction) -> Tuple[int, Fraction]:
    """Compute divmod(a, b) for two Fraction objects.

    `divmod(a, b)` returns a tuple (quotient, remainder) where quotient = a // b (int)
    and remainder = a % b (Fraction).

    Args:
        a: Dividend fraction.
        b: Divisor fraction.

    Returns:
        Tuple pair (quotient_int, remainder_fraction).
    """
    return divmod(a, b)


def compare_fractions(a: Fraction, b: Fraction) -> Dict[str, bool]:
    """Evaluate relational comparison operators between two fractions.

    Args:
        a: First fraction.
        b: Second fraction.

    Returns:
        Dictionary of comparison results.
    """
    return {
        "equal": a == b,
        "not_equal": a != b,
        "greater_than": a > b,
        "less_than": a < b,
        "greater_equal": a >= b,
        "less_equal": a <= b,
    }


def mixed_type_arithmetic(
    frac: Fraction, integer_val: int, float_val: float
) -> Dict[str, Union[Fraction, float]]:
    """Demonstrate mixed-type arithmetic between Fraction, int, and float.

    Note:
    - Operations between Fraction and int return a Fraction.
    - Operations between Fraction and float coerce the Fraction to float and return a float.

    Args:
        frac: Fraction operand.
        integer_val: Integer operand.
        float_val: Float operand.

    Returns:
        Dictionary of results showing returned types.
    """
    return {
        "frac_plus_int": frac + integer_val,
        "frac_times_int": frac * integer_val,
        "frac_plus_float": frac + float_val,
        "frac_times_float": frac * float_val,
    }


def main() -> None:
    """Demonstrate fraction arithmetic and comparison operations."""
    print("--- Fraction Arithmetic & Comparison Operations ---")

    a = Fraction(2, 7)
    b = Fraction(1, 3)

    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")
    print(f"divmod(a, b) = {calculate_fraction_divmod(a, b)}")
    print(f"Comparison (a > b): {a > b}")
    print(f"Mixed arithmetic (Fraction + int): {mixed_type_arithmetic(a, 3, 0.5)}")


if __name__ == "__main__":
    main()
