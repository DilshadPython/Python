"""Modern F-Strings (Formatted String Literals) Module.

Provides functions demonstrating Python 3.6+ f-string syntax, expression evaluation,
self-documenting debug specifiers (`f"{var=}"`), conversion flags (`!r`, `!s`),
and custom formatting options.
"""

from datetime import datetime
from typing import Any


def format_f_string_basics(
    first_name: str,
    last_name: str,
    role: str = "Python Developer",
) -> str:
    """Format string using standard f-string interpolation.

    Args:
        first_name: First name.
        last_name: Last name.
        role: Professional role title.

    Returns:
        Interpolated f-string.
    """
    return f"{first_name} [{last_name}] is a {role}."


def format_f_string_expressions(a: int, b: int) -> str:
    """Evaluate Python math expressions inline inside f-strings.

    Args:
        a: First number.
        b: Second number.

    Returns:
        String containing expression evaluation results.
    """
    return f"Sum of {a} + {b} = {a + b} | Product = {a * b} | Max = {max(a, b)}"


def format_f_string_debug(var1: Any, var2: Any) -> str:
    """Demonstrate Python 3.8+ self-documenting debug specifier `f"{var=}"`.

    Args:
        var1: First variable.
        var2: Second variable.

    Returns:
        String showing variable names and evaluated values.
    """
    return f"Debugging: {var1=} | {var2=}"


def format_f_string_specifiers(amount: float, date_obj: datetime = None) -> str:
    """Format floating numbers, conversion flags (`!r`), and dates inside f-strings.

    Args:
        amount: Floating numeric value.
        date_obj: Datetime object to format.

    Returns:
        Formatted string containing formatted number and date.
    """
    if date_obj is None:
        date_obj = datetime(2026, 9, 5, 21, 0, 0)
        
    formatted_num = f"{amount:,.2f}"
    formatted_date = f"{date_obj:%Y-%m-%d %H:%M}"
    return f"Amount: ${formatted_num} | Date: {formatted_date}"


def main() -> None:
    """Demonstrate f-string operations."""
    print("--- F-String Operations ---")

    # 1. Basics
    print(format_f_string_basics("David", "Smith"))

    # 2. Inline expressions
    print(format_f_string_expressions(15, 27))

    # 3. Debug syntax f"{var=}"
    x = 42
    y = "Active"
    print(format_f_string_debug(x, y))

    # 4. Number & Date formatting
    now = datetime.now()
    print(format_f_string_specifiers(9876543.21, now))


if __name__ == "__main__":
    main()
