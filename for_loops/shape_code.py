"""Complex Pyramid Pattern Generation with Multiple Nested Loops.

Demonstrates constructing structured numeric inverted/hourglass shapes using multiple
sequential and nested loop blocks with custom spacing and decremental ranges.

Import Notes:
    - 'from typing import List': Standard library typing import for list type hints.
"""

from typing import List


def generate_numeric_pyramid_shape(total_rows: int = 8) -> List[str]:
    """Generate complex numeric pyramid rows using nested loop blocks.

    Args:
        total_rows: Total height/rows for shape generation (default: 8).

    Returns:
        List of generated line strings representing the pattern rows.
    """
    pattern_lines: List[str] = []

    for x in range(0, total_rows):
        line_parts: List[str] = []

        # 1. Decremental left numbers
        for y in range(total_rows - 1, x, -1):
            line_parts.append(f"{y} ")

        # 2. Middle padding spaces
        for _ in range(x):
            line_parts.append("  ")

        # 3. Incremental right numbers
        for j in range(x + 1, total_rows):
            line_parts.append(f"{j} ")

        line_str = "".join(line_parts)
        pattern_lines.append(line_str)
        print(line_str)
        print()

    return pattern_lines


def demo_shape_code() -> List[str]:
    """Run numeric pyramid pattern demonstration."""
    print("--- Complex Numeric Pyramid Pattern ---")
    return generate_numeric_pyramid_shape(8)


if __name__ == "__main__":
    demo_shape_code()
