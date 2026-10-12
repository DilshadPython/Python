"""Fraction Conversions & Approximations Module.

Provides functions demonstrating advanced fraction conversion utilities:
- Float approximation using `limit_denominator()`
- Integer ratio extraction using `as_integer_ratio()`
- Casting fractions to primitive types (`int`, `float`, `str`)
- Modern numerator GCD calculation using `math.gcd()`
"""

import math
from decimal import Decimal
from fractions import Fraction
from typing import Dict, Tuple, Union


def approximate_float_to_fraction(val: float, max_denominator: int = 100) -> Fraction:
    """Approximate an inexact binary floating-point value to a simple Fraction.

    Floats like 0.1 or 0.33333333333 cannot be represented exactly in binary floating point,
    resulting in large denominators when converted directly with Fraction(val).
    `limit_denominator()` finds the closest fraction with a denominator <= max_denominator.

    Args:
        val: Floating-point number (e.g. 0.3333333333).
        max_denominator: Maximum denominator bound. Defaults to 100.

    Returns:
        Approximated simple rational fraction (e.g. 1/3).
    """
    exact_frac = Fraction(val)
    return exact_frac.limit_denominator(max_denominator)


def extract_integer_ratio(frac: Fraction) -> Tuple[int, int]:
    """Return numerator and denominator as a 2-tuple (numerator, denominator).

    This method is standardized across `int`, `float`, and `Fraction` in Python 3.8+ (PEP 567).

    Args:
        frac: Input fraction object.

    Returns:
        Tuple pair (numerator, denominator).
    """
    return frac.as_integer_ratio()


def convert_fraction_to_numeric_types(
    frac: Fraction
) -> Dict[str, Union[int, float, str]]:
    """Cast a Fraction instance into standard primitive Python numeric types.

    Args:
        frac: Input fraction instance.

    Returns:
        Converted values across int, float, and str.
    """
    return {
        "float_val": float(frac),
        "int_val": int(frac),  # Truncates towards zero
        "str_val": str(frac),
    }


def compute_fraction_gcd(a: Fraction, b: Fraction) -> int:
    """Compute greatest common divisor of numerators using `math.gcd()`.

    Args:
        a: First fraction.
        b: Second fraction.

    Returns:
        Greatest common divisor of numerators.
    """
    return math.gcd(a.numerator, b.numerator)


def main() -> None:
    """Demonstrate fraction conversion and approximation operations."""
    print("--- Fraction Conversions & Approximations ---")

    float_val = 0.3333333333333333
    exact = Fraction(float_val)
    approx = approximate_float_to_fraction(float_val, max_denominator=10)

    print(f"[exact vs approx] Float 0.3333... exact denominator: {exact.denominator}")
    print(f"[limit_denominator(10)] Approximated fraction -> {approx}")

    f = Fraction(3, 4)
    print(f"\n[as_integer_ratio] {extract_integer_ratio(f)}")
    print(f"[convert_types] {convert_fraction_to_numeric_types(f)}")

    f1 = Fraction(12, 35)
    f2 = Fraction(18, 35)
    print(f"[math.gcd] GCD of numerators (12, 18) -> {compute_fraction_gcd(f1, f2)}")


if __name__ == "__main__":
    main()
