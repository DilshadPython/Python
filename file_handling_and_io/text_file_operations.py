"""
File Handling & I/O: Text File Operations

This module demonstrates text file operations in Python:
- Opening modes: `'r'` (read), `'w'` (write/overwrite), `'a'` (append), `'x'` (exclusive creation), `'r+'` (read/write).
- File object methods: `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, `seek()`, `tell()`, `flush()`.
- Line-by-line streaming iteration using `for line in file_handle:`.
"""
import os
from typing import List


def write_lines_to_file(filepath: str, lines: List[str]) -> int:
    """
    Writes a list of text strings to a file in write ('w') mode.

    Args:
        filepath (str): Target file path.
        lines (List[str]): List of strings to write.

    Returns:
        int: Number of characters written.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        content = "\n".join(lines) + "\n"
        chars_written = f.write(content)
        f.flush()  # Flushes internal buffer to disk
        return chars_written


def append_line_to_file(filepath: str, line: str) -> None:
    """
    Appends a single line to a file in append ('a') mode.

    Args:
        filepath (str): Target file path.
        line (str): Line content to append.
    """
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(line.strip() + "\n")


def read_file_all(filepath: str) -> str:
    """
    Reads the entire file content into a single string using `read()`.

    Args:
        filepath (str): File path to read.

    Returns:
        str: Complete text file content.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def read_file_lines(filepath: str) -> List[str]:
    """
    Reads all lines into a list of strings using `readlines()`.

    Args:
        filepath (str): File path to read.

    Returns:
        List[str]: Stripped list of line strings.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def stream_file_lines(filepath: str) -> List[str]:
    """
    Streams lines one-by-one using for-in loop (memory efficient for large files).

    Args:
        filepath (str): File path to stream.

    Returns:
        List[str]: Processed lines.
    """
    processed: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            processed.append(line.strip().upper())
    return processed


def demonstrate_seek_and_tell(filepath: str) -> List[str]:
    """
    Demonstrates inspecting file pointer offset using `tell()` and resetting position using `seek()`.

    Args:
        filepath (str): Target file path.

    Returns:
        List[str]: Log lines documenting pointer positions.
    """
    logs: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        logs.append(f"Initial file pointer offset (`tell()`): {f.tell()}")
        first_line = f.readline()
        logs.append(f"After reading first line ({first_line.strip()!r}), `tell()` offset: {f.tell()}")
        f.seek(0)  # Reset pointer back to file beginning
        logs.append(f"After `seek(0)`, `tell()` offset: {f.tell()}")
    return logs


def main() -> None:
    """Demonstrates text file operations."""
    print("=" * 60)
    print("1. Text File Operations (`r`, `w`, `a`, `seek`, `tell`)")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_file = os.path.join(base_dir, "cities.txt")

    initial_cities = ["Tokyo", "London", "New York", "Paris", "Berlin"]

    # 1. Write lines
    chars = write_lines_to_file(sample_file, initial_cities)
    print(f"\n1. Wrote {len(initial_cities)} cities ({chars} chars) to {sample_file}")

    # 2. Append line
    append_line_to_file(sample_file, "Sydney")
    print("2. Appended 'Sydney' to cities.txt")

    # 3. Read all lines
    lines = read_file_lines(sample_file)
    print(f"\n3. Current file lines (`readlines()`): {lines}")

    # 4. Seek and Tell demonstration
    seek_logs = demonstrate_seek_and_tell(sample_file)
    print("\n4. Pointer Inspection (`tell()` and `seek()`):")
    for log in seek_logs:
        print(f"   {log}")


if __name__ == "__main__":
    main()
