"""
Fraction Fundamentals: Instantiation, Representation, and Reduction.

This module demonstrates core rational number operations using fractions.Fraction:
- Instantiation from integers, strings, floats, and Decimals
- Automated reduction to lowest terms (gcd simplification)
- Accessing .numerator and .denominator properties
- String formatting and representations (__str__ and __repr__)
"""
# "from fractions import Fraction" imports rational number class from standard library.
from fractions import Fraction
# "from decimal import Decimal" imports fixed-point decimal arithmetic class.
from decimal import Decimal
# "from typing import Tuple, Dict, Any" imports type hint annotations.
from typing import Tuple, Dict, Any


def create_fraction_from_integers(numerator: int, denominator: int) -> Fraction:
    """
    Create a Fraction object from explicit integer numerator and denominator.

    Python automatically simplifies the fraction to lowest terms by dividing
    both numerator and denominator by their greatest common divisor (GCD).

    Args:
        numerator (int): The top number of the fraction.
        denominator (int): The bottom number of the fraction (must be non-zero).

    Returns:
        Fraction: Standardized reduced fraction object.

    Raises:
        ZeroDivisionError: If denominator is zero.
    """
    if denominator == 0:
        raise ZeroDivisionError("Fraction denominator cannot be zero.")
    return Fraction(numerator, denominator)


def create_fraction_from_string(fraction_str: str) -> Fraction:
    """
    Parse a string representation into a Fraction object.

    Python 3.9+ supports leading/trailing whitespace around numbers and slash.

    Args:
        fraction_str (str): String like '2/7', '-5/3', '0.75', or ' 1 / 4 '.

    Returns:
        Fraction: Parsed fraction object.
    """
    return Fraction(fraction_str)


def create_fraction_from_float_and_decimal(val: float | Decimal) -> Fraction:
    """
    Convert a floating-point number or Decimal object into an exact Fraction.

    Args:
        val (float | Decimal): Numeric float or Decimal value.

    Returns:
        Fraction: Exact rational fraction matching the internal binary/decimal representation.
    """
    return Fraction(val)


def inspect_fraction_components(frac: Fraction) -> Dict[str, Any]:
    """
    Extract key attributes and representations of a Fraction instance.

    Args:
        frac (Fraction): Input fraction instance.

    Returns:
        Dict[str, Any]: Dictionary containing numerator, denominator, str, and repr.
    """
    return {
        "numerator": frac.numerator,
        "denominator": frac.denominator,
        "str": str(frac),
        "repr": repr(frac),
        "is_integer": frac.denominator == 1,
    }


if __name__ == "__main__":
    print("=== Step 1: Fraction Instantiation & Components ===")
    f1 = create_fraction_from_integers(4, 14)
    print(f"Fraction(4, 14) simplified -> {f1} (num: {f1.numerator}, den: {f1.denominator})")

    f2 = create_fraction_from_string(" 3 / 8 ")
    print(f"Fraction(' 3 / 8 ') -> {f2}")

    f3 = create_fraction_from_float_and_decimal(0.25)
    print(f"Fraction(0.25) -> {f3}")

    info = inspect_fraction_components(f1)
    print(f"Inspected components: {info}")
