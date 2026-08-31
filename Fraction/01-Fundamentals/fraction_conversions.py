"""
Fraction Conversions: Approximations, Ratio Extraction, and Numeric Types.

This module demonstrates advanced fraction conversion utilities:
- Exact vs. approximate float representations using limit_denominator()
- Extracting (numerator, denominator) tuples using as_integer_ratio()
- Converting fractions to int, float, and Decimal numeric types
- Integrating standard library math functions like math.gcd()
"""
# "from fractions import Fraction" imports rational fraction class.
from fractions import Fraction
# "import math" imports standard mathematical functions including gcd.
import math
# "from decimal import Decimal" imports decimal arithmetic support.
from decimal import Decimal
# "from typing import Tuple, Dict" imports typing annotations.
from typing import Tuple, Dict


def approximate_float_to_fraction(val: float, max_denominator: int = 100) -> Fraction:
    """
    Approximate an inexact binary floating-point value to a simple Fraction.

    Floats like 0.1 or 0.33333333333 cannot be represented exactly in binary floating point,
    resulting in high-precision denominators when converted directly with Fraction(val).
    limit_denominator() finds the closest fraction with a denominator <= max_denominator.

    Args:
        val (float): Floating-point number (e.g. 0.3333333333).
        max_denominator (int): Maximum denominator bound. Defaults to 100.

    Returns:
        Fraction: Approximated simple rational fraction (e.g. 1/3).
    """
    exact_frac = Fraction(val)
    simplified_frac = exact_frac.limit_denominator(max_denominator)
    return simplified_frac


def extract_integer_ratio(frac: Fraction) -> Tuple[int, int]:
    """
    Return numerator and denominator as a 2-tuple (numerator, denominator).

    This method is standardized across int, float, and Fraction in Python 3.8+ (PEP 567/CPython API).

    Args:
        frac (Fraction): Input fraction object.

    Returns:
        Tuple[int, int]: Tuple pair (numerator, denominator).
    """
    return frac.as_integer_ratio()


def convert_fraction_to_numeric_types(frac: Fraction) -> Dict[str, int | float | str]:
    """
    Cast a Fraction instance into standard primitive Python numeric types.

    Args:
        frac (Fraction): Input fraction instance.

    Returns:
        Dict[str, int | float | str]: Converted values across int, float, and str.
    """
    return {
        "float_val": float(frac),
        "int_val": int(frac),  # Truncates towards zero
        "str_val": str(frac),
    }


def compute_fraction_gcd(a: Fraction, b: Fraction) -> int:
    """
    Compute greatest common divisor of numerators using modern math.gcd().

    Note: In Python 2.7–3.8, fractions.gcd() was used; in Python 3.9+,
    fractions.gcd() was removed in favor of math.gcd().

    Args:
        a (Fraction): First fraction.
        b (Fraction): Second fraction.

    Returns:
        int: Greatest common divisor of numerators.
    """
    return math.gcd(a.numerator, b.numerator)


if __name__ == "__main__":
    print("=== Step 1: Fraction Conversions & Approximations ===")
    float_val = 0.3333333333333333
    exact = Fraction(float_val)
    approx = approximate_float_to_fraction(float_val, max_denominator=10)

    print(f"Float 0.3333333333333333 exact Fraction denominator: {exact.denominator}")
    print(f"limit_denominator(10) approximation -> {approx}")

    f = Fraction(3, 4)
    print(f"as_integer_ratio() -> {extract_integer_ratio(f)}")
    print(f"Converted types -> {convert_fraction_to_numeric_types(f)}")
