"""
File Stream Iterator Demonstration Module.

This module demonstrates lazy line-by-line file streaming using Python's TextIOWrapper iterator interface.
"""
# "from pathlib import Path" imports object-oriented file paths.
from pathlib import Path
# "from typing import List" imports list type annotation.
from typing import List


def read_file_lines_with_iterator(file_path: Path, max_lines: int = 3) -> List[str]:
    """
    Read up to max_lines lines from a text file using explicit next() calls on file iterator.

    Args:
        file_path (Path): Path to text file.
        max_lines (int): Maximum lines to read. Defaults to 3.

    Returns:
        List[str]: Stripped line contents.
    """
    lines: List[str] = []
    if not file_path.exists():
        return lines

    with open(file_path, "r", encoding="utf-8") as file_handle:
        for _ in range(max_lines):
            try:
                line = next(file_handle)
                lines.append(line.rstrip("\n"))
            except StopIteration:
                break

    return lines


if __name__ == "__main__":
    print("=== File Stream Iterator Demonstration ===")
    sample_file = Path(__file__).parent / "grade.txt"
    if sample_file.exists():
        extracted = read_file_lines_with_iterator(sample_file, max_lines=3)
        print(f"Extracted lines from {sample_file.name}: {extracted}")
