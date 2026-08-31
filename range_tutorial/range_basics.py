"""Range Basics Demonstration Module.

This module provides clear, PEP 8 compliant functions demonstrating fundamental
usage of Python's built-in range() sequence generator, including start/stop/step
parameters, nested sequence grids, and horizontal line formatting.
"""

# import typing for explicit static type annotations
from typing import List


def generate_sequence(start: int, stop: int, step: int = 1) -> List[int]:
    """Generate a list of integers from a range sequence.

    Args:
        start: The starting value of the range (inclusive).
        stop: The end boundary of the range (exclusive).
        step: The increment or decrement step size. Defaults to 1.

    Returns:
        List[int]: Generated integer sequence.

    Raises:
        TypeError: If start, stop, or step are not integers.
        ValueError: If step is zero.
    """
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        raise TypeError("start, stop, and step must all be integers.")
    if step == 0:
        raise ValueError("range() arg 3 must not be zero.")

    return list(range(start, stop, step))


def format_grid(rows: int = 5, cols: int = 5) -> List[str]:
    """Generate coordinate string rows using nested range loops.

    Args:
        rows: Number of grid rows. Defaults to 5.
        cols: Number of grid columns. Defaults to 5.

    Returns:
        List[str]: List of formatted coordinate lines.

    Raises:
        TypeError: If rows or cols are not integers.
        ValueError: If rows or cols are non-positive.
    """
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError("rows and cols must be integers.")
    if rows <= 0 or cols <= 0:
        raise ValueError("rows and cols must be positive integers.")

    grid_lines: List[str] = []
    # Loop through row indices
    for row in range(rows):
        row_elements: List[str] = []
        # Loop through column indices for each row
        for col in range(cols):
            row_elements.append(f"{row}x{col}y")
        grid_lines.append("  ".join(row_elements))

    return grid_lines


def format_horizontal_sequence(start: int = 0, stop: int = 30) -> str:
    """Format a space-separated string sequence of integers.

    Args:
        start: Starting integer (inclusive). Defaults to 0.
        stop: Ending integer (exclusive). Defaults to 30.

    Returns:
        str: Space-delimited string of numbers in range.
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("start and stop must be integers.")

    # Convert range values to string items and join with single space
    return " ".join(str(num) for num in range(start, stop))


def print_range_demos() -> None:
    """Execute and display interactive range demonstrations to console."""
    print("=== 1. Basic Single and Dual Parameter Ranges ===")
    print("range(0, 10):", generate_sequence(0, 10))
    print("range(10, 21):", generate_sequence(10, 21))

    print("\n=== 2. Nested Iteration Grid (5x5) ===")
    grid = format_grid(5, 5)
    for line in grid:
        print(line)

    print("\n=== 3. Horizontal Sequence ===")
    print(format_horizontal_sequence(0, 30))


if __name__ == "__main__":
    print_range_demos()
