"""Grade Bar Chart Generation via File Reading and Loop Step Filtering.

Reads numerical grades from 'grade.txt' and constructs a visual ASCII hash ('#') bar
chart representation for each grade where every 5 units add one hash mark.

Import Notes:
    - 'import os': Standard library OS module used for safe path construction and verification.
    - 'from typing import List, Tuple': Standard library typing imports for structured hints.
"""

import os
from typing import List, Tuple


def generate_grade_bar(grade: int, divisor: int = 5) -> Tuple[str, int]:
    """Generate a hash mark '#' bar string for a given numeric grade.

    Args:
        grade: The numeric grade value.
        divisor: Interval value for adding a hash symbol (default: 5).

    Returns:
        Tuple containing the hash bar string and the final iteration count.
    """
    bar = ""
    last_idx = 0
    for i in range(1, grade + 1):
        last_idx = i
        if i % divisor == 0:
            bar += "#"
    return bar, last_idx


def process_grade_bars(file_path: str) -> List[Tuple[int, str, int]]:
    """Read grades from a text file and return generated bar chart data.

    Args:
        file_path: Path to the grade text file.

    Returns:
        List of tuples: (grade_val, bar_str, final_iteration_index).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Grade file not found at: {file_path}")

    results: List[Tuple[int, str, int]] = []
    with open(file_path, "r", encoding="utf-8") as file_handle:
        for line in file_handle:
            clean_line = line.strip()
            if clean_line and clean_line.isdigit():
                grade_val = int(clean_line)
                bar, last_i = generate_grade_bar(grade_val, 5)
                results.append((grade_val, bar, last_i))
                print(f"Grade: {grade_val:3d} | Bar: {bar:<20s} | Last i: {last_i}")

    return results


def demo_for_bar() -> List[Tuple[int, str, int]]:
    """Execute grade bar chart generation demonstration on 'grade.txt'."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_file = os.path.join(script_dir, "grade.txt")
    print(f"--- Grade Bar Chart Processing ('{os.path.basename(target_file)}') ---")
    return process_grade_bars(target_file)


if __name__ == "__main__":
    demo_for_bar()
