"""
File Handling & I/O: Temporary Files & Pathlib Manipulations

This module demonstrates temporary file creation and modern object-oriented path
manipulations using Python standard library tools:
- `tempfile.NamedTemporaryFile`: Auto-cleaning temporary file creation.
- `pathlib.Path`: Object-oriented path resolution, file existence, and extension checks.
- `os.stat()`: Inspecting file size, creation timestamp, and modification metadata.
"""
import os
import tempfile
from pathlib import Path
from typing import Dict, Any


def create_temporary_file_demo(content: str) -> str:
    """
    Creates a temporary file, writes content, reads it back, and verifies auto-cleanup.

    Args:
        content (str): Text content to write into temporary file.

    Returns:
        str: Read back content.
    """
    read_back = ""
    # NamedTemporaryFile automatically deletes the file on context exit if delete=True
    with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=True) as temp_file:
        temp_file.write(content)
        temp_file.flush()
        temp_file.seek(0)
        read_back = temp_file.read()
        print(f"Temporary file path created: {temp_file.name}")
    return read_back


def inspect_file_metadata(filepath: str) -> Dict[str, Any]:
    """
    Extracts file metadata using `pathlib.Path` and `os.stat()`.

    Args:
        filepath (str): Target file path.

    Returns:
        Dict[str, Any]: File metadata dictionary (exists, size, stem, suffix).
    """
    path = Path(filepath)
    if not path.exists():
        return {"exists": False}

    stat_info = path.stat()
    return {
        "exists": True,
        "name": path.name,
        "stem": path.stem,
        "suffix": path.suffix,
        "size_bytes": stat_info.st_size,
        "absolute_path": str(path.resolve()),
    }


def main() -> None:
    """Demonstrates temporary files and pathlib path inspection."""
    print("=" * 60)
    print("5. Temporary Files & `pathlib.Path` Inspection")
    print("=" * 60)

    # 1. Temporary File Demonstration
    sample_text = "Temporary data buffer line 1\nTemporary data buffer line 2"
    result = create_temporary_file_demo(sample_text)
    print(f"   Read back from temporary file:\n{result}")

    # 2. Pathlib & Stat Metadata Inspection
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_target = os.path.join(base_dir, "cities.txt")
    meta = inspect_file_metadata(sample_target)

    print(f"\n2. Metadata for {sample_target}:")
    for key, val in meta.items():
        print(f"   {key:<15s}: {val}")


if __name__ == "__main__":
    main()
