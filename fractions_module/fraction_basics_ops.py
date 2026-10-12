"""Fraction Basics & Instantiation Operations Module.

Provides functions demonstrating core rational number operations using `fractions.Fraction`:
- Instantiation from integers, strings, floats, and Decimals
- Automatic reduction to lowest terms (GCD simplification)
- Accessing `.numerator` and `.denominator` attributes
"""

from decimal import Decimal
from fractions import Fraction
from typing import Any, Dict, Union


def create_fraction_from_integers(numerator: int, denominator: int) -> Fraction:
    """Create a Fraction object from explicit integer numerator and denominator.

    Python automatically simplifies the fraction to lowest terms by dividing
    both numerator and denominator by their greatest common divisor (GCD).

    Args:
        numerator: The top integer of the fraction.
        denominator: The bottom integer of the fraction (must be non-zero).

    Returns:
        Standardized reduced Fraction object.

    Raises:
        ZeroDivisionError: If denominator is zero.
    """
    if denominator == 0:
        raise ZeroDivisionError("Fraction denominator cannot be zero.")
    return Fraction(numerator, denominator)


def create_fraction_from_string(fraction_str: str) -> Fraction:
    """Parse a string representation into a Fraction object.

    Python 3.9+ supports leading/trailing whitespace around numbers and slash.

    Args:
        fraction_str: String like '2/7', '-5/3', '0.75', or ' 1 / 4 '.

    Returns:
        Parsed Fraction object.
    """
    return Fraction(fraction_str)


def create_fraction_from_float_and_decimal(val: Union[float, Decimal]) -> Fraction:
    """Convert a floating-point number or Decimal object into an exact Fraction.

    Args:
        val: Numeric float or Decimal value.

    Returns:
        Exact rational fraction matching internal binary or decimal representation.
    """
    return Fraction(val)


def inspect_fraction_components(frac: Fraction) -> Dict[str, Any]:
    """Extract key attributes and representations of a Fraction instance.

    Args:
        frac: Input fraction instance.

    Returns:
        Dictionary containing numerator, denominator, str, repr, and integer check.
    """
    return {
        "numerator": frac.numerator,
        "denominator": frac.denominator,
        "str": str(frac),
        "repr": repr(frac),
        "is_integer": frac.denominator == 1,
    }


def main() -> None:
    """Demonstrate basic fraction instantiation and inspection operations."""
    print("--- Fraction Basics & Instantiation Operations ---")

    # 1. Integer creation with automatic GCD reduction
    f1 = create_fraction_from_integers(4, 14)
    print(f"[create_from_integers] Fraction(4, 14) simplified -> {f1} (num: {f1.numerator}, den: {f1.denominator})")

    # 2. String parsing
    f2 = create_fraction_from_string(" 3 / 8 ")
    print(f"[create_from_string] Fraction(' 3 / 8 ') -> {f2}")

    # 3. Float and Decimal parsing
    f3 = create_fraction_from_float_and_decimal(0.25)
    print(f"[create_from_float] Fraction(0.25) -> {f3}")

    # 4. Attribute inspection
    info = inspect_fraction_components(f1)
    print(f"\n[inspect_components] {info}")


if __name__ == "__main__":
    main()
