"""
File Reading Context Manager Demonstration Module.

This module demonstrates automatic file resource cleanup using the 'with' statement
versus legacy manual open() and close() file handling patterns.
"""
# "import os" imports standard operating system interface routines.
import os
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import List" imports list type annotation helper.
from typing import List


def read_lines_with_context(filepath: str) -> List[str]:
    """
    Read lines from file safely utilizing 'with' context manager.

    Args:
        filepath (str): Path to text file.

    Returns:
        List[str]: List of stripped text lines.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    cleaned_lines: List[str] = []
    with open(path, "r", encoding="utf-8") as file_handle:
        for line in file_handle:
            cleaned_lines.append(line.rstrip("\n"))

    return cleaned_lines


def read_lines_legacy_close(filepath: str) -> List[str]:
    """
    Read lines from file using legacy manual open() and close() within try-finally.

    Args:
        filepath (str): Path to text file.

    Returns:
        List[str]: List of stripped text lines.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    cleaned_lines: List[str] = []
    file_handle = open(path, "r", encoding="utf-8")
    try:
        for line in file_handle:
            cleaned_lines.append(line.rstrip("\n"))
    finally:
        file_handle.close()

    return cleaned_lines


if __name__ == "__main__":
    print("=== File Reading Context Manager Demonstration ===")
    sample_file = str(Path(__file__).parent / "with_sample.txt")
    lines = read_lines_with_context(sample_file)
    print("Lines read safely via context manager:", lines)
