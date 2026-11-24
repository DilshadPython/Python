"""Directory Management Operations Module.

Provides functions for renaming, moving, and calculating cumulative folder sizes
using `os`, `shutil`, and `pathlib.Path`.
"""

import os
import shutil
from pathlib import Path
from typing import Union


def rename_directory(
    source_path: Union[str, Path],
    destination_path: Union[str, Path],
) -> Path:
    """Rename a directory using `pathlib.Path.rename` or `os.rename`.

    Args:
        source_path: Existing directory path.
        destination_path: New directory path.

    Returns:
        Path object pointing to the renamed directory.
    """
    src = Path(source_path)
    dest = Path(destination_path)
    
    if not src.exists():
        raise FileNotFoundError(f"Source directory '{source_path}' does not exist.")
        
    src.rename(dest)
    print(f"[Path.rename] Renamed '{src}' to '{dest}'")
    return dest


def move_directory(
    source_path: Union[str, Path],
    destination_path: Union[str, Path],
) -> Path:
    """Move a directory to another location using `shutil.move`.

    Args:
        source_path: Path of the directory to move.
        destination_path: Destination directory path.

    Returns:
        Path object pointing to the moved directory.
    """
    src = Path(source_path)
    dest = Path(destination_path)
    
    if not src.exists():
        raise FileNotFoundError(f"Source directory '{source_path}' does not exist.")
        
    result_path = shutil.move(str(src), str(dest))
    print(f"[shutil.move] Moved '{src}' to '{result_path}'")
    return Path(result_path)


def get_directory_size(target_path: Union[str, Path]) -> int:
    """Calculate total size of all files in a directory recursively.

    Args:
        target_path: Directory path to analyze.

    Returns:
        Total size in bytes.
    """
    path = Path(target_path)
    if not path.is_dir():
        raise NotADirectoryError(f"Target path '{target_path}' is not a directory.")
        
    total_size = 0
    for root, _, files in os.walk(path):
        for file in files:
            file_path = Path(root) / file
            if file_path.is_file():
                total_size += file_path.stat().st_size
                
    return total_size


def main() -> None:
    """Demonstrate directory management operations."""
    print("--- Directory Management Operations ---")
    
    # Create temporary folders for demonstration
    demo_source = Path("temp_manage_src")
    demo_renamed = Path("temp_manage_renamed")
    demo_target_dir = Path("temp_manage_target")
    
    demo_source.mkdir(exist_ok=True)
    (demo_source / "test_file.txt").write_text("Hello Directory Management!")
    
    # 1. Directory size calculation
    size = get_directory_size(demo_source)
    print(f"\n[get_directory_size] Folder '{demo_source}' size: {size} bytes")
    
    # 2. Rename directory
    renamed_path = rename_directory(demo_source, demo_renamed)
    
    # 3. Move directory
    demo_target_dir.mkdir(exist_ok=True)
    moved_path = move_directory(renamed_path, demo_target_dir)
    
    # Cleanup
    if demo_target_dir.exists():
        shutil.rmtree(demo_target_dir)
        print(f"\nCleaned up test environment.")


if __name__ == "__main__":
    main()
