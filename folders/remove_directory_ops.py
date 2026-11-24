"""Directory Removal Operations Module.

Provides functions for deleting empty directories and recursively removing directory trees
using `os.rmdir`, `pathlib.Path.rmdir`, and `shutil.rmtree`.
"""

import os
import shutil
from pathlib import Path
from typing import Union


def remove_empty_directory(target_path: Union[str, Path]) -> bool:
    """Remove an empty directory safely using `pathlib.Path.rmdir` or `os.rmdir`.

    Args:
        target_path: Path of the empty directory to remove.

    Returns:
        True if successfully removed.

    Raises:
        OSError: If directory is not empty or does not exist.
    """
    path = Path(target_path)
    if not path.exists():
        raise FileNotFoundError(f"Directory '{target_path}' does not exist.")
        
    path.rmdir()
    print(f"[Path.rmdir] Removed empty directory: '{path}'")
    return True


def remove_directory_tree(target_path: Union[str, Path]) -> bool:
    """Recursively delete a directory tree and all contents using `shutil.rmtree`.

    Args:
        target_path: Path of the directory tree to remove.

    Returns:
        True if successfully removed.
    """
    path = Path(target_path)
    if not path.exists():
        print(f"[shutil.rmtree] Path '{target_path}' does not exist.")
        return False
        
    shutil.rmtree(path)
    print(f"[shutil.rmtree] Recursively removed directory tree: '{path}'")
    return True


def main() -> None:
    """Demonstrate directory removal operations."""
    print("--- Directory Removal Operations ---")
    
    # 1. Create and remove an empty directory
    empty_dir = Path("demo_empty_folder")
    empty_dir.mkdir(exist_ok=True)
    remove_empty_directory(empty_dir)
    
    # 2. Create and recursively remove a non-empty directory tree
    nested_dir = Path("demo_remove_tree/level1/level2")
    nested_dir.mkdir(parents=True, exist_ok=True)
    (nested_dir / "sample.txt").write_text("Test content for deletion")
    
    remove_directory_tree("demo_remove_tree")


if __name__ == "__main__":
    main()
