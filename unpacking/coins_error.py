"""
Demonstration of argument unpacking error (`coins_error.py`).

Passing a single list parameter without the single asterisk `*` operator passes the list object
as the first argument ('length'), missing required positional arguments ('width', 'height').
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


def run_error_demo() -> None:
    """Demonstrate argument error handling."""
    coins = [75, 40, 25]

    try:
        # ❌ Passing list directly causes TypeError: missing 2 required positional arguments
        # type: ignore[call-arg]
        total(coins)  # type: ignore
    except TypeError as error:
        print("Expected Unpacking TypeError Caught:", error)


if __name__ == "__main__":
    run_error_demo()