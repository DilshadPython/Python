"""
Demonstration of manual positional element indexing vs list unpacking (`coins.py`).

This module compares indexing list elements manually (`coins[0], coins[1]`)
versus sequence unpacking.
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
    """Run demonstration with manual index extraction."""
    coins = [75, 40, 25]
    result = total(coins[0], coins[1], coins[2])
    print(f"{result} Inch")


if __name__ == "__main__":
    main()
