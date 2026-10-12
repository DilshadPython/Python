"""Range Formatting Demonstration Module.

This module demonstrates zero-padded number formatting driven by range() loops
and f-strings / str.format() syntax for creating structured text outputs.
"""

# import typing for type hint annotations
from typing import List


def format_range_numbers(
    start: int, stop: int, width: int = 2, prefix: str = "The number starts from"
) -> List[str]:
    """Format a sequence of numbers from range() with zero-padding.

    Args:
        start: Starting integer (inclusive).
        stop: Ending integer (exclusive).
        width: Minimum field width for zero-padding. Defaults to 2.
        prefix: Custom leading text for each formatted line.

    Returns:
        List[str]: Formatted string lines with zero-padded numbers.

    Raises:
        TypeError: If start, stop, or width are not integers.
        ValueError: If width is less than 1.
    """
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(width, int):
        raise TypeError("start, stop, and width must be integers.")
    if width < 1:
        raise ValueError("width must be at least 1.")

    formatted_lines: List[str] = []
    # Loop over range bounds and apply zero-padded format width
    for num in range(start, stop):
        formatted_lines.append(f"{prefix} {num:0{width}d}")

    return formatted_lines


def print_formatted_ranges() -> None:
    """Print zero-padded range formatted outputs to standard output."""
    print("=== Width 2 Padding (range 1..15) ===")
    for line in format_range_numbers(1, 15, width=2):
        print(line)

    print("\n=== Width 3 Padding (range 1..15) ===")
    for line in format_range_numbers(1, 15, width=3):
        print(line)

    print("\n=== Width 4 Padding (range 10..25) ===")
    for line in format_range_numbers(10, 25, width=4):
        print(line)


if __name__ == "__main__":
    print_formatted_ranges()
