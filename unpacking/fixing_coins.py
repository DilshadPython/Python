"""
Fixing unpacking error using single asterisk operator (`fixing_coins.py`).

Adding `*` in front of `*coins` unpacks the list elements into positional parameters.
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
    """Run fixed positional list unpacking demonstration."""
    coins = [75, 40, 25]

    # ✅ Using *coins unpacks list into length=75, width=40, height=25
    print(total(*coins), "Inch")


if __name__ == "__main__":
    main()