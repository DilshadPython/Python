"""
Directory File Iterator Demonstration Module.

This module demonstrates modern, cross-platform directory iteration using os.scandir()
and pathlib.Path generators/iterators.

Historical Note:
Legacy scripts used `os.popen('dir *.py')` which depended on Windows shell syntax.
Modern Python 3 code uses `os.scandir()` or `Path.glob()`, which return OS-native iterators
that are memory-efficient, cross-platform (Linux/macOS/Windows), and PEP 8 compliant.
"""
# "import os" imports standard operating system interface routines.
import os
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import List" imports type hint annotations.
from typing import List


def iterate_python_files_in_dir(directory_path: Path) -> List[str]:
    """
    Safely iterate over Python files using pathlib.Path iterator interface.

    Args:
        directory_path (Path): Path to search.

    Returns:
        List[str]: Names of Python files found.
    """
    if not directory_path.exists() or not directory_path.is_dir():
        return []

    # Path.glob returns an iterator (generator object) yielding Path instances lazily
    file_iterator = directory_path.glob("*.py")
    return [file_path.name for file_path in file_iterator]


def iterate_scandir_entries(directory_path: Path) -> List[str]:
    """
    Demonstrate os.scandir() directory iterator (PEP 471, Python 3.5+).

    os.scandir() yields DirEntry objects with cached stat attributes, making directory
    traversal up to 2-20x faster than os.listdir().

    Args:
        directory_path (Path): Directory path.

    Returns:
        List[str]: List of entry names.
    """
    if not directory_path.exists():
        return []

    entries: List[str] = []
    with os.scandir(directory_path) as scanner:
        # scanner is an iterator yielding DirEntry objects
        for entry in scanner:
            if entry.name.endswith(".py"):
                entries.append(entry.name)

    return entries


if __name__ == "__main__":
    print("=== Directory Iterator Demonstration ===")
    current_dir = Path(__file__).parent
    py_files = iterate_python_files_in_dir(current_dir)
    print(f"Python files via Path.glob iterator  : {py_files}")

    scandir_files = iterate_scandir_entries(current_dir)
    print(f"Python files via os.scandir iterator : {scandir_files}")
