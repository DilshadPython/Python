"""
Fraction Advanced Math & Integration Module.

This module demonstrates advanced mathematical utilities and standard library integration:
- Floor, ceiling, truncation, and rounding operations with fractions
- Integration with standard library math functions (math.floor, math.ceil, math.trunc)
- Exact arithmetic accumulation using sum() over Fraction iterables
- High-precision Decimal interop and numerator/denominator extraction
"""
# "from fractions import Fraction" imports rational fraction class.
from fractions import Fraction
# "import math" imports mathematical functions.
import math
# "from decimal import Decimal" imports decimal arithmetic support.
from decimal import Decimal
# "from typing import List, Dict" imports type hint symbols.
from typing import List, Dict


def apply_rounding_and_truncation(frac: Fraction) -> Dict[str, int]:
    """
    Apply math rounding functions to a Fraction instance.

    Args:
        frac (Fraction): Input fraction (e.g., 7/3 or -7/3).

    Returns:
        Dict[str, int]: Results for floor, ceiling, truncation, and standard round.
    """
    return {
        "floor": math.floor(frac),
        "ceil": math.ceil(frac),
        "trunc": math.trunc(frac),
        "round_default": round(frac),
        "round_2_decimals": round(float(frac), 2),
    }


def accumulate_fractions(fractions_list: List[Fraction]) -> Fraction:
    """
    Sum an iterable of Fraction objects without loss of precision.

    The built-in sum() accepts Fraction objects and accumulates them exactly.

    Args:
        fractions_list (List[Fraction]): List of fraction instances.

    Returns:
        Fraction: Exact sum fraction reduced to lowest terms.
    """
    return sum(fractions_list, Fraction(0, 1))


def decimal_fraction_conversion_interop(dec: Decimal) -> Dict[str, Fraction | Decimal]:
    """
    Demonstrate seamless, exact bi-directional conversion between Decimal and Fraction.

    Args:
        dec (Decimal): Fixed-point decimal number.

    Returns:
        Dict[str, Fraction | Decimal]: Converted fraction and round-trip decimal object.
    """
    frac = Fraction(dec)
    # Convert back to Decimal using numerator / denominator
    roundtrip_dec = Decimal(frac.numerator) / Decimal(frac.denominator)
    return {
        "original_decimal": dec,
        "converted_fraction": frac,
        "roundtrip_decimal": roundtrip_dec,
    }


if __name__ == "__main__":
    print("=== Step 2: Fraction Advanced Math & Rounding ===")
    f = Fraction(7, 3)
    print(f"Fraction: {f} (~{float(f):.4f})")
    print(f"Rounding operations: {apply_rounding_and_truncation(f)}")

    sample_list = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    total = accumulate_fractions(sample_list)
    print(f"Sum of [1/2, 1/3, 1/6] -> {total}")

    dec_val = Decimal("0.125")
    interop = decimal_fraction_conversion_interop(dec_val)
    print(f"Decimal interop: {interop}")
