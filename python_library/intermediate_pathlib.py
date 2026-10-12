"""
Intermediate Level Object-Oriented Path Manipulation Module (`intermediate_pathlib.py`).

This module provides functional filesystem patterns designed for intermediate developers
(`rglob()` recursive traversal, `.with_suffix()`, `.with_name()`, `.stat()` metadata inspection).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System execution utilities.
# - `from pathlib import Path`: Object-oriented filesystem path abstraction (PEP 428).
# - `from typing import Any, Dict, List`: PEP 484 type hint generics.
# =========================================================================
import sys
from pathlib import Path
from typing import Any, Dict, List


def find_files_recursively(directory_path: Path, pattern: str = "*.py") -> List[Path]:
    """Recursively search for matching file paths using `Path.rglob()`.

    Args:
        directory_path (Path): Directory root path to search.
        pattern (str): Glob matching pattern (defaults to "*.py").

    Returns:
        List[Path]: List of matching Path instances.
    """
    if not directory_path.exists():
        return []
    return list(directory_path.rglob(pattern))


def transform_file_extension(original_path: Path, new_suffix: str) -> Path:
    """Transform file path extension using `Path.with_suffix()`.

    Args:
        original_path (Path): Input file path (e.g., Path("report.txt")).
        new_suffix (str): Target extension (e.g., ".pdf").

    Returns:
        Path: New Path instance with modified extension.
    """
    return original_path.with_suffix(new_suffix)


def get_file_metadata(file_path: Path) -> Dict[str, Any]:
    """Retrieve detailed filesystem metadata stats using `Path.stat()`.

    Args:
        file_path (Path): File path to inspect.

    Returns:
        Dict[str, Any]: Stat dictionary containing size in bytes, mtime, and permissions.
    """
    if not file_path.exists():
        return {"error": f"File '{file_path}' does not exist"}

    stat_result = file_path.stat()
    return {
        "path": str(file_path),
        "size_bytes": stat_result.st_size,
        "modified_timestamp": stat_result.st_mtime,
        "mode_octal": oct(stat_result.st_mode),
        "is_executable": stat_result.st_mode & 0o111 != 0,
    }


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate pathlib demonstration."""
    print("=== Intermediate Level Pathlib Operations ===")

    current_dir = Path(".")
    py_files = find_files_recursively(current_dir, "*.py")
    print(f"Found {len(py_files)} Python files recursively.")

    sample = Path("document.docx")
    pdf_path = transform_file_extension(sample, ".pdf")
    print(f"Transformed Path (.with_suffix): '{sample}' -> '{pdf_path}'")

    meta = get_file_metadata(Path(__file__))
    print(f"Current File Metadata (.stat): {meta}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
