"""Directory Scanning and Traversal Operations Module.

Provides functions to list, inspect, walk, and glob directory contents using
`os.listdir`, `os.scandir`, `os.walk`, and `pathlib.Path.glob`.
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Union


def list_directory_contents(target_path: Union[str, Path] = ".") -> List[str]:
    """Retrieve entry names in a directory using `os.listdir`.

    Args:
        target_path: Path of the target directory to scan.

    Returns:
        List of filenames and subdirectory names.
    """
    path = Path(target_path)
    if not path.is_dir():
        raise NotADirectoryError(f"Target path '{target_path}' is not a directory.")
    return os.listdir(path)


def scan_directory_entries(
    target_path: Union[str, Path] = "."
) -> List[Dict[str, Union[str, int, bool]]]:
    """Retrieve detailed entry metadata efficiently using `os.scandir`.

    Args:
        target_path: Directory path to inspect.

    Returns:
        List of dictionaries containing entry metadata.
    """
    path = Path(target_path)
    entries_metadata = []
    
    with os.scandir(path) as entries:
        for entry in entries:
            entries_metadata.append({
                "name": entry.name,
                "path": entry.path,
                "is_dir": entry.is_dir(),
                "is_file": entry.is_file(),
                "size_bytes": entry.stat().st_size if entry.is_file() else 0,
            })
            
    return entries_metadata


def walk_directory_tree(
    target_path: Union[str, Path] = "."
) -> List[Tuple[str, List[str], List[str]]]:
    """Recursively walk directory trees using `os.walk`.

    Args:
        target_path: Directory root to walk.

    Returns:
        List of tuples (root, dirs, files) representing directory tree structure.
    """
    path = Path(target_path)
    results = []
    for root, dirs, files in os.walk(path):
        results.append((root, dirs, files))
    return results


def glob_directory_files(
    target_path: Union[str, Path] = ".",
    pattern: str = "*",
    recursive: bool = False,
) -> List[Path]:
    """Find matching files using `pathlib.Path.glob` or `rglob`.

    Args:
        target_path: Base directory search path.
        pattern: Match pattern (e.g., "*.py", "*_ops.py").
        recursive: Whether to search recursively in subdirectories.

    Returns:
        List of matching Path objects.
    """
    path = Path(target_path)
    if recursive:
        return list(path.rglob(pattern))
    return list(path.glob(pattern))


def main() -> None:
    """Demonstrate directory scanning operations."""
    print("--- Directory Scanning Operations ---")
    current_dir = Path(".")
    
    # 1. os.listdir
    contents = list_directory_contents(current_dir)
    print(f"\n[os.listdir] Entries in current directory ({len(contents)} items):")
    print(contents[:5])
    
    # 2. os.scandir
    detailed_entries = scan_directory_entries(current_dir)
    print(f"\n[os.scandir] Sample entry metadata:")
    if detailed_entries:
        print(detailed_entries[0])
        
    # 3. os.walk
    tree = walk_directory_tree(current_dir)
    print(f"\n[os.walk] Walked {len(tree)} directory level(s).")
    
    # 4. pathlib glob
    python_files = glob_directory_files(current_dir, pattern="*.py", recursive=False)
    print(f"\n[Path.glob] Python files found ({len(python_files)}):")
    for file in python_files:
        print(f"  - {file.name}")


if __name__ == "__main__":
    main()
