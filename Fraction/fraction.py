"""
Fraction Module: Comprehensive Master Demonstration Entrypoint.

This script demonstrates rational fraction arithmetic, conversions, limit_denominator approximations,
and fraction sequence iterations using Python's standard library fractions.Fraction.
"""
# "from fractions import Fraction" imports rational fraction arithmetic class.
from fractions import Fraction
# "from decimal import Decimal" imports decimal arithmetic support.
from decimal import Decimal
# "from typing import List, Tuple" imports type hint annotations.
from typing import List, Tuple


def demonstrate_fraction_basics() -> Tuple[Fraction, Fraction, Fraction]:
    """
    Demonstrate creating fractions from integers and performing exact addition.

    Returns:
        Tuple[Fraction, Fraction, Fraction]: Returns (a, b, sum_c).
    """
    a = Fraction(2, 7)
    b = Fraction(1, 3)
    c = a + b  # 2/7 + 1/3 = 13/21
    return a, b, c


def demonstrate_fraction_conversions() -> Tuple[Fraction, Tuple[int, int]]:
    """
    Demonstrate limit_denominator approximation and integer ratio extraction.

    Returns:
        Tuple[Fraction, Tuple[int, int]]: Approximated fraction and (num, den) tuple.
    """
    float_val = 0.142857142857
    approx = Fraction(float_val).limit_denominator(10)  # 1/7
    ratio = approx.as_integer_ratio()
    return approx, ratio


if __name__ == "__main__":
    print("=== Python Fractions Master Demonstration ===")
    a, b, c = demonstrate_fraction_basics()
    print(f"  Fraction a        : {a}")
    print(f"  Fraction b        : {b}")
    print(f"  Sum (a + b)       : {c}")

    approx, ratio = demonstrate_fraction_conversions()
    print(f"\n=== Float Approximation & Ratio Extraction ===")
    print(f"  Approximated 1/7  : {approx}")
    print(f"  as_integer_ratio(): {ratio}")
