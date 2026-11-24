"""
Beginner Level Object-Oriented Path Manipulation Module (`beginner_pathlib.py`).

This module provides clear, well-commented examples of basic `pathlib.Path` operations
designed for beginner developers (`Path()`, `/` operator, `.exists()`, `.read_text()`, `.write_text()`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI execution exit status.
# - `from pathlib import Path`: Object-oriented filesystem path abstraction (PEP 428).
# - `from typing import Dict`: PEP 484 type hint generics.
# =========================================================================
import sys
from pathlib import Path
from typing import Dict


def create_and_join_path(base_directory: str, filename: str) -> Path:
    """Demonstrate object-oriented path joining using the slash (`/`) operator.

    Args:
        base_directory (str): Parent directory path string.
        filename (str): Target filename string.

    Returns:
        Path: Combined Path instance.
    """
    base = Path(base_directory)
    full_path = base / filename
    return full_path


def check_path_status(target_path: Path) -> Dict[str, bool]:
    """Check existence and type properties of a target path.

    Args:
        target_path (Path): Path instance to inspect.

    Returns:
        Dict[str, bool]: Inspection dictionary containing 'exists', 'is_file', 'is_dir'.
    """
    return {
        "exists": target_path.exists(),
        "is_file": target_path.is_file(),
        "is_dir": target_path.is_dir(),
    }


def read_and_write_file(target_file: Path, content: str) -> str:
    """Write text string to target file and read back using pathlib methods.

    Args:
        target_file (Path): Path instance of target text file.
        content (str): Text content to write.

    Returns:
        str: Text content read back from file.
    """
    # Create parent directories if missing
    target_file.parent.mkdir(parents=True, exist_ok=True)

    # Write text content with UTF-8 encoding
    target_file.write_text(content, encoding="utf-8")

    # Read text content back
    return target_file.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner pathlib demonstration."""
    print("=== Beginner Level Pathlib Operations ===")

    joined_path = create_and_join_path("data", "sample.txt")
    print(f"Joined Path (/): {joined_path}")

    status = check_path_status(joined_path)
    print(f"Path Status: {status}")

    demo_file = Path("demo_output.txt")
    read_back = read_and_write_file(demo_file, "Hello, Pathlib!")
    print(f"Read Back Content: '{read_back}'")

    # Cleanup demo file
    if demo_file.exists():
        demo_file.unlink()

    return 0


if __name__ == "__main__":
    sys.exit(main())
