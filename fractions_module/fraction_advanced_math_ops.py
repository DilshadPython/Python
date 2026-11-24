"""Fraction Advanced Math & Integration Module.

Provides functions demonstrating rounding, math functions, list summation, and Decimal interop:
- `math.floor()`, `math.ceil()`, `math.trunc()`, `round()`
- Precision summation via `sum()` over Fraction iterables
- High-precision Decimal to Fraction bi-directional interop
"""

import math
from decimal import Decimal
from fractions import Fraction
from typing import Dict, List, Union


def apply_rounding_and_truncation(frac: Fraction) -> Dict[str, Union[int, float]]:
    """Apply math rounding functions to a Fraction instance.

    Args:
        frac: Input fraction (e.g., 7/3 or -7/3).

    Returns:
        Dictionary of floor, ceiling, truncation, and rounding values.
    """
    return {
        "floor": math.floor(frac),
        "ceil": math.ceil(frac),
        "trunc": math.trunc(frac),
        "round_default": round(frac),
        "round_2_decimals": round(float(frac), 2),
    }


def accumulate_fractions(fractions_list: List[Fraction]) -> Fraction:
    """Sum an iterable of Fraction objects without loss of precision.

    The built-in `sum()` accepts Fraction objects and accumulates them exactly.

    Args:
        fractions_list: List of Fraction instances.

    Returns:
        Exact sum fraction reduced to lowest terms.
    """
    return sum(fractions_list, Fraction(0, 1))


def decimal_fraction_conversion_interop(
    dec: Decimal
) -> Dict[str, Union[Fraction, Decimal]]:
    """Demonstrate seamless, exact bi-directional conversion between Decimal and Fraction.

    Args:
        dec: Fixed-point decimal number.

    Returns:
        Converted fraction and round-trip decimal object.
    """
    frac = Fraction(dec)
    # Convert back to Decimal using numerator / denominator
    roundtrip_dec = Decimal(frac.numerator) / Decimal(frac.denominator)
    return {
        "original_decimal": dec,
        "converted_fraction": frac,
        "roundtrip_decimal": roundtrip_dec,
    }


def main() -> None:
    """Demonstrate advanced math operations and Decimal interop."""
    print("--- Fraction Advanced Math & Decimal Interop ---")

    f = Fraction(7, 3)
    print(f"Fraction: {f} (~{float(f):.4f})")
    print(f"Rounding operations: {apply_rounding_and_truncation(f)}")

    sample_list = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    total = accumulate_fractions(sample_list)
    print(f"\nSum of [1/2, 1/3, 1/6] -> {total}")

    dec_val = Decimal("0.125")
    interop = decimal_fraction_conversion_interop(dec_val)
    print(f"\nDecimal interop: {interop}")


if __name__ == "__main__":
    main()
