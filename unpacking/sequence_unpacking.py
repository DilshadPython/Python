"""
Positional Iterable Sequence Unpacking Module (`sequence_unpacking.py`).

This module demonstrates unpacking sequence iterables (lists, tuples) into positional
function parameters using the single asterisk (`*`) unpacking operator.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for process exit code handling.
# - `from typing import List, Sequence, Tuple`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import List, Sequence, Tuple

# Conversion factor: 1 cubic centimeter = 0.0610237 cubic inches
CM3_TO_INCH3_FACTOR: float = 0.0610237


def calculate_volume_inches(length: float, width: float, height: float) -> float:
    """Calculate volume in cubic inches given dimensions in centimeters.

    Args:
        length (float): Length dimension in centimeters.
        width (float): Width dimension in centimeters.
        height (float): Height dimension in centimeters.

    Returns:
        float: Calculated volume in cubic inches rounded to 4 decimal places.
    """
    volume_cm3 = length * width * height
    volume_inch3 = volume_cm3 * CM3_TO_INCH3_FACTOR
    return round(volume_inch3, 4)


def unpack_sequence_dimensions(dimensions: Sequence[float]) -> float:
    """Unpack a 3-element sequence (list/tuple) into calculate_volume_inches parameters.

    Args:
        dimensions (Sequence[float]): Sequence containing [length, width, height].

    Returns:
        float: Calculated volume in cubic inches.

    Raises:
        ValueError: If sequence does not contain exactly 3 elements.
    """
    if len(dimensions) != 3:
        raise ValueError(f"Expected 3 dimension elements, got {len(dimensions)}")

    # Unpack sequence elements using positional single-asterisk (*) operator
    return calculate_volume_inches(*dimensions)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for sequence unpacking demonstration."""
    print("=== Positional Sequence Unpacking Demonstration ===")

    coins_list: List[float] = [75.0, 40.0, 25.0]
    volume = unpack_sequence_dimensions(coins_list)

    print(f"Dimensions List: {coins_list}")
    print(f"Calculated Volume (total(*coins_list)): {volume} Cubic Inches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
