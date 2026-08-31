"""
Demonstrates automatic file resource cleanup using 'with' vs legacy manual close().
"""
# "import module" loads the os standard library module for path verification.
import os
# "from module import name" imports the List type hint symbol directly into local scope.
from typing import List



def read_lines_with_context(filepath: str) -> List[str]:
    """Read lines from file safely utilizing 'with' context manager."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    cleaned_lines: List[str] = []
    with open(filepath, 'r', encoding='utf-8') as fh:
        for line in fh:
            cleaned_lines.append(line.rstrip('\n'))

    return cleaned_lines


def read_lines_legacy_close(filepath: str) -> List[str]:
    """Read lines from file using legacy manual open() and close()."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    cleaned_lines: List[str] = []
    fh = open(filepath, 'r', encoding='utf-8')
    try:
        for line in fh:
            cleaned_lines.append(line.rstrip('\n'))
    finally:
        fh.close()

    return cleaned_lines


if __name__ == '__main__':
    sample_file = os.path.join(os.path.dirname(__file__), 'with_sample.txt')
    lines = read_lines_with_context(sample_file)
    print("Lines read safely via context manager:", lines)
