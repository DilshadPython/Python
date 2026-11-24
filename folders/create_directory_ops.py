"""Directory Creation Operations Module.

Provides functions for creating single and nested directories safely using
both the legacy `os` module and modern `pathlib.Path` objects.
"""

import os
from pathlib import Path
from typing import Union


def create_single_directory(folder_name: str) -> Path:
    """Create a single directory using `os.mkdir`.

    Args:
        folder_name: Name or path of the directory to create.

    Returns:
        Path object pointing to the created directory.
    """
    path = Path(folder_name)
    if not path.exists():
        os.mkdir(path)
        print(f"[os.mkdir] Directory created: '{path}'")
    else:
        print(f"[os.mkdir] Directory already exists: '{path}'")
    return path


def create_nested_directories(folder_path: str) -> Path:
    """Create multi-level nested directories using `os.makedirs`.

    Args:
        folder_path: Path structure of directories to create.

    Returns:
        Path object pointing to the target directory.
    """
    path = Path(folder_path)
    os.makedirs(path, exist_ok=True)
    print(f"[os.makedirs] Nested directory created/verified: '{path}'")
    return path


def create_directory_with_pathlib(folder_path: Union[str, Path]) -> Path:
    """Create single or nested directories using `pathlib.Path.mkdir`.

    Args:
        folder_path: String or Path target for directory creation.

    Returns:
        Path object of the created directory.
    """
    path = Path(folder_path)
    path.mkdir(parents=True, exist_ok=True)
    print(f"[pathlib.Path.mkdir] Path created/verified: '{path}'")
    return path


def main() -> None:
    """Demonstrate directory creation operations."""
    print("--- Directory Creation Operations ---")
    
    # 1. Single directory creation
    single_dir = create_single_directory("demo_single_folder")
    
    # 2. Nested directory creation with os.makedirs
    nested_dir = create_nested_directories("demo_parent/level1/level2")
    
    # 3. Pathlib directory creation
    pathlib_dir = create_directory_with_pathlib("demo_pathlib/subfolder")
    
    # Cleanup demonstration folders
    import shutil
    for target in [single_dir, Path("demo_parent"), Path("demo_pathlib")]:
        if target.exists():
            shutil.rmtree(target if target.is_dir() else target.parent)
            print(f"Cleaned up demo directory: '{target}'")


if __name__ == "__main__":
    main()
