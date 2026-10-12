"""
Volume calculation from explicit positional parameters (`totals.py`).

Demonstrates calling total() directly with positional values.
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
    """Calculate volume with explicit arguments."""
    print(total(75, 45, 30), "Inch")


if __name__ == "__main__":
    main()