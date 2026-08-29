"""Generating ASCII Triangle Shapes with Nested 'for' Loops.

Demonstrates using nested 'for' loops to render incremental and decremental
hash mark ('#') right-triangle shapes.

Import Notes:
    - 'from typing import List': Standard library typing import for string list annotations.
"""

from typing import List


def generate_ascending_hash_triangle(max_rows: int = 5) -> List[str]:
    """Generate ascending right-triangle hash rows.

    Args:
        max_rows: Number of rows in triangle (default: 5 for demo clarity).

    Returns:
        List of formatted row strings.
    """
    rows: List[str] = []
    print(f"--- Ascending Hash Triangle ({max_rows} rows) ---")
    for x in range(1, max_rows + 1):
        row_str = " ".join("#" for _ in range(x))
        rows.append(row_str)
        print(row_str)
    return rows


def generate_descending_hash_triangle(start_rows: int = 5) -> List[str]:
    """Generate descending right-triangle hash rows.

    Args:
        start_rows: Starting row width (default: 5).

    Returns:
        List of formatted row strings.
    """
    rows: List[str] = []
    print(f"\n--- Descending Hash Triangle ({start_rows} rows) ---")
    for a in range(start_rows, 0, -1):
        row_str = " ".join("#" for _ in range(a))
        rows.append(row_str)
        print(row_str)
    return rows


def demo_print_shape_forloop() -> None:
    """Run shape printing demonstration."""
    generate_ascending_hash_triangle(5)
    print("=========")
    generate_descending_hash_triangle(5)


if __name__ == "__main__":
    demo_print_shape_forloop()
