"""3D Visual Graphics and Pattern Generator Module.

This module demonstrates nested loops and string repetition driven by Python's
range() sequence generator to render formatted ASCII geometric patterns.
"""

# import List from typing module for explicit return type annotations
from typing import List


def generate_decreasing_space_pattern(height: int = 11) -> List[str]:
    """Generate ASCII lines with decreasing leading spaces and a terminal hash.

    Args:
        height: Total line count of the output (must be at least 1).

    Returns:
        List[str]: Formatted rows representing the pattern.

    Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 1.
    """
    if not isinstance(height, int):
        raise TypeError(f"Height must be an integer, got {type(height).__name__}")
    if height < 1:
        raise ValueError(f"Height must be at least 1, got {height}")

    pattern_lines: List[str] = []
    # Driven by range(height) to decrement leading space counts
    for level in range(height):
        spaces = " " * (height - level)
        pattern_lines.append(f"{spaces}#")

    return pattern_lines


def generate_single_sided_pyramid(height: int = 11) -> List[str]:
    """Generate single-sided right-aligned ASCII pyramid rows using range().

    Args:
        height: Total height level of the pyramid. Defaults to 11.

    Returns:
        List[str]: Formatted pyramid rows.

    Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 1.
    """
    if not isinstance(height, int):
        raise TypeError(f"Height must be an integer, got {type(height).__name__}")
    if height < 1:
        raise ValueError(f"Height must be at least 1, got {height}")

    pattern_lines: List[str] = []
    # Increment zero block count using range iterator level
    for level in range(height):
        spaces = " " * (height - level)
        zeros = "0" * (level + 1)
        pattern_lines.append(f"{spaces}{zeros}")

    return pattern_lines


def generate_ascii_pyramid(height: int = 11) -> List[str]:
    """Generate a symmetric 3D ASCII pyramid using range() indexing.

    Args:
        height: Total height level of the pyramid (must be positive).

    Returns:
        List[str]: Formatted rows representing the symmetric pyramid.

    Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 1.
    """
    if not isinstance(height, int):
        raise TypeError(f"Height must be an integer, got {type(height).__name__}")
    if height < 1:
        raise ValueError(f"Height must be at least 1, got {height}")

    pattern_lines: List[str] = []
    # Calculate leading spaces and odd-numbered block counts (2 * level + 1)
    for level in range(height):
        spaces = " " * (height - 1 - level)
        blocks = "0" * (2 * level + 1)
        pattern_lines.append(f"{spaces}{blocks}")

    return pattern_lines


def print_patterns() -> None:
    """Print standard ASCII pattern variations to stdout."""
    print("=== Simple Decreasing Space Pattern ===")
    for line in generate_decreasing_space_pattern(11):
        print(line)

    print("\n=== Single-Sided Pyramid Pattern ===")
    for line in generate_single_sided_pyramid(11):
        print(line)

    print("\n=== Symmetric 3D Pyramid Pattern ===")
    for line in generate_ascii_pyramid(11):
        print(line)


if __name__ == "__main__":
    print_patterns()
