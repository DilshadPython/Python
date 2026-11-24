"""Datetime Formatting Demonstration Module.

This module demonstrates formatting datetime objects using Python strftime directives,
f-strings, and string formatting specifiers (month name, day of year, day of week).
"""

# import standard datetime module for timestamp representation
import datetime
from typing import Optional


def format_datetime_standard(dt: datetime.datetime) -> str:
    """Format a datetime object into standard date-time string representation.

    Args:
        dt: The datetime object to format.

    Returns:
        str: Formatted string in 'Month DD, YYYY, HH:MM:SS' format.

    Raises:
        TypeError: If dt is not a datetime.datetime instance.
    """
    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"Expected datetime object, got {type(dt).__name__}")

    return f"I wrote this code {dt:%B %d, %Y, %H:%M:%S}"


def format_datetime_detailed(dt: datetime.datetime) -> str:
    """Format a datetime object with extended weekday and day-of-year details.

    Args:
        dt: The datetime object to format.

    Returns:
        str: Detailed string containing formatted date, weekday, and day of year.

    Raises:
        TypeError: If dt is not a datetime.datetime instance.
    """
    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"Expected datetime object, got {type(dt).__name__}")

    formatted_date = f"{dt:%B %d, %Y, %H:%M:%S}"
    day_name = f"{dt:%A}"
    day_of_year = f"{dt:%j}"

    return (
        f"I wrote this code {formatted_date} on {day_name} day of the year {day_of_year}"
    )


def print_datetime_demos() -> None:
    """Execute datetime formatting demonstrations."""
    timestamp = datetime.datetime(2026, 1, 30, 3, 20, 33)

    print("=== Raw Datetime Output ===")
    print("I wrote this code", timestamp)

    print("\n=== Standard Formatted Output ===")
    print(format_datetime_standard(timestamp))

    print("\n=== Detailed Formatted Output ===")
    print(format_datetime_detailed(timestamp))


if __name__ == "__main__":
    print_datetime_demos()
