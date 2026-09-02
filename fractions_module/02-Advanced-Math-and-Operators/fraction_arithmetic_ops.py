"""
Fraction Arithmetic & Comparison Operators Module.

This module demonstrates mathematical arithmetic and relational operations with Fraction objects:
- Arithmetic operators: +, -, *, /, // (floor division), % (modulo), ** (exponentiation)
- Built-in functions: divmod(), abs(), round()
- Relational comparison operators: ==, !=, >, <, >=, <=
- Mixed-type arithmetic: Operations with ints, floats, and Decimals
"""
# "from fractions import Fraction" imports rational fraction class.
from fractions import Fraction
# "from typing import Tuple, Dict, Any" imports type hint annotations.
from typing import Tuple, Dict, Any


def perform_fraction_arithmetic(a: Fraction, b: Fraction) -> Dict[str, Fraction | float]:
    """
    Perform core arithmetic operations between two Fraction instances.

    Args:
        a (Fraction): First operand.
        b (Fraction): Second operand.

    Returns:
        Dict[str, Fraction | float]: Dictionary of arithmetic results.
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
    """
    Compute divmod(a, b) for two Fraction objects.

    divmod(a, b) returns a tuple (quotient, remainder) where quotient = a // b (int)
    and remainder = a % b (Fraction).

    Args:
        a (Fraction): Dividend fraction.
        b (Fraction): Divisor fraction.

    Returns:
        Tuple[int, Fraction]: Quotient int and remainder Fraction.
    """
    return divmod(a, b)


def compare_fractions(a: Fraction, b: Fraction) -> Dict[str, bool]:
    """
    Evaluate all 6 relational comparison operators between two fractions.

    Args:
        a (Fraction): First fraction.
        b (Fraction): Second fraction.

    Returns:
        Dict[str, bool]: Boolean comparison results.
    """
    return {
        "equal": a == b,
        "not_equal": a != b,
        "greater_than": a > b,
        "less_than": a < b,
        "greater_equal": a >= b,
        "less_equal": a <= b,
    }


def mixed_type_arithmetic(frac: Fraction, integer_val: int, float_val: float) -> Dict[str, Fraction | float]:
    """
    Demonstrate mixed-type arithmetic between Fraction, int, and float.

    Note: Operations between Fraction and int return a Fraction.
    Operations between Fraction and float coerce the Fraction to float and return a float.

    Args:
        frac (Fraction): Fraction operand.
        integer_val (int): Integer operand.
        float_val (float): Float operand.

    Returns:
        Dict[str, Fraction | float]: Results showing return types.
    """
    return {
        "frac_plus_int": frac + integer_val,    # Returns Fraction
        "frac_times_int": frac * integer_val,   # Returns Fraction
        "frac_plus_float": frac + float_val,  # Returns float
        "frac_times_float": frac * float_val, # Returns float
    }


if __name__ == "__main__":
    print("=== Step 2: Fraction Arithmetic & Comparison ===")
    a = Fraction(2, 7)
    b = Fraction(1, 3)

    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")
    print(f"divmod(a, b) = {calculate_fraction_divmod(a, b)}")
    print(f"Comparison (a > b): {a > b}")
    print(f"Mixed arithmetic (Fraction + int): {mixed_type_arithmetic(a, 3, 0.5)}")
