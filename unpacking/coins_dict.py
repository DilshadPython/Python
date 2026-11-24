"""
Demonstration of dictionary keyword unpacking (`coins_dict.py`).

This module demonstrates unpacking dictionary key-value pairs into named keyword parameters
using double asterisk (`**coins`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from sequence_unpacking import calculate_volume_inches`: Volume helper.
# =========================================================================
try:
    from unpacking.sequence_unpacking import calculate_volume_inches
except ImportError:
    from sequence_unpacking import calculate_volume_inches


def total(length: float, width: float, height: float) -> float:
    """Calculate volume in cubic inches from dimensions in centimeters."""
    return calculate_volume_inches(length, width, height)


def main() -> None:
    """Run dictionary keyword unpacking demonstration."""
    coins = {"length": 15, "width": 10, "height": 8}
    print(total(coins["length"], coins["width"], coins["height"]), "Inch")

    print("\nWe use ** for dictionary unpacking:")
    print(total(**coins), "Inch")


if __name__ == "__main__":
    main()