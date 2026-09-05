"""Legacy Percent (%) String Formatting Operations Module.

Provides functions demonstrating C-style printf `%` formatting in Python,
including `%s`, `%r`, `%d`, `%f`, precision/width modifiers, and dict mapping.
"""

from typing import Dict, Any


def format_with_percent_s_and_r(name: str, value: float) -> str:
    """Demonstrate `%s` (calls `str()`) vs `%r` (calls `repr()`).

    Args:
        name: Name string.
        value: Numeric value.

    Returns:
        Formatted string containing both representations.
    """
    # %s formats using str(), %r formats using repr()
    return "Name (str): %s | Value (repr): %r" % (name, value)


def format_numbers_with_percent(
    number: float,
    width: int = 0,
    precision: int = 2
) -> str:
    """Format floating point numbers with width and precision using `%`.

    Args:
        number: Float number to format.
        width: Total minimum width of output string.
        precision: Number of decimal places to round to.

    Returns:
        Formatted floating point string.
    """
    format_spec = "%%%d.%df" % (width, precision)
    return format_spec % number


def format_with_dict_percent(data: Dict[str, Any]) -> str:
    """Format strings using dictionary key lookup with `%`.

    Args:
        data: Dictionary containing named keys.

    Returns:
        Interpolated string using dictionary values.
    """
    return "User %(first_name)s %(last_name)s is %(age)d years old." % data


def main() -> None:
    """Demonstrate `%` formatting operations."""
    print("--- Percent (%) Formatting Operations ---")

    # 1. %s vs %r
    result_sr = format_with_percent_s_and_r("Python", 3.12)
    print(f"[str vs repr] {result_sr}")

    # 2. Float formatting
    val = 234.345678
    print(f"\n[Float Precision] Default (%1.2f): {format_numbers_with_percent(val, 1, 2)}")
    print(f"[Float Width] Padded (%30.4f): '{format_numbers_with_percent(val, 30, 4)}'")

    # 3. Dict interpolation
    user_info = {"first_name": "Dilshad", "last_name": "Abdulla", "age": 30}
    print(f"\n[Dict Interpolation] {format_with_dict_percent(user_info)}")


if __name__ == "__main__":
    main()
