"""
Object-Oriented Filesystem Path Operations Module (`pathlib.Path`).

This module demonstrates modern object-oriented path manipulation using Python's standard
`pathlib` library (PEP 428), replacing legacy string-based `os.path` operations.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import os`: Operating system interface for environment context.
# - `from pathlib import Path`: Object-oriented filesystem path abstraction (PEP 428).
# - `import sys`: System utilities for CLI argument processing and exit status.
# - `from typing import Dict, List, Optional, Union`: PEP 484 type hint generics.
# =========================================================================
import os
from pathlib import Path
import sys
from typing import Dict, List, Optional, Union


def get_current_directory_info() -> Dict[str, str]:
    """Retrieve details about current working directory and user home directory.

    Returns:
        Dict[str, str]: Dictionary containing cwd and home path strings.
    """
    cwd_path = Path.cwd()
    home_path = Path.home()

    return {
        "current_working_directory": str(cwd_path),
        "user_home_directory": str(home_path),
    }


def decompose_path(target_path: Union[str, Path]) -> Dict[str, Union[str, bool]]:
    """Decompose a file or directory path into structural components.

    Args:
        target_path (Union[str, Path]): Target path string or Path instance.

    Returns:
        Dict[str, Union[str, bool]]: Dictionary containing stem, suffix, name, parent, is_file, and exists.
    """
    path_obj = Path(target_path)

    return {
        "raw_path": str(path_obj),
        "name": path_obj.name,
        "stem": path_obj.stem,
        "suffix": path_obj.suffix,
        "parent": str(path_obj.parent),
        "is_absolute": path_obj.is_absolute(),
        "exists": path_obj.exists(),
        "is_file": path_obj.is_file(),
        "is_dir": path_obj.is_dir(),
    }


def list_directory_contents(
    directory_path: Union[str, Path] = ".",
    pattern: str = "*",
) -> List[Dict[str, Union[str, bool]]]:
    """Iterate and list contents of a target directory using glob pattern matching.

    Args:
        directory_path (Union[str, Path]): Directory to iterate. Defaults to current directory ".".
        pattern (str): Glob matching pattern. Defaults to "*".

    Returns:
        List[Dict[str, Union[str, bool]]]: List of path component dictionaries.

    Raises:
        NotADirectoryError: If directory_path exists but is not a directory.
        FileNotFoundError: If directory_path does not exist.
    """
    path_obj = Path(directory_path)

    if not path_obj.exists():
        raise FileNotFoundError(f"Directory path '{directory_path}' does not exist")
    if not path_obj.is_dir():
        raise NotADirectoryError(f"Path '{directory_path}' is not a directory")

    items: List[Dict[str, Union[str, bool]]] = []
    for item in path_obj.glob(pattern):
        items.append(decompose_path(item))

    return items


def write_and_read_text_file(
    file_path: Union[str, Path],
    content: str,
) -> Dict[str, Union[str, int]]:
    """Write text content to a file using Path.write_text and read back using Path.read_text.

    Args:
        file_path (Union[str, Path]): Target file path.
        content (str): Text content string to write.

    Returns:
        Dict[str, Union[str, int]]: Dictionary containing bytes_written, file_path, and read_content.
    """
    path_obj = Path(file_path)
    
    # Ensure parent directory exists before writing
    path_obj.parent.mkdir(parents=True, exist_ok=True)

    bytes_written = path_obj.write_text(content, encoding="utf-8")
    read_content = path_obj.read_text(encoding="utf-8")

    return {
        "file_path": str(path_obj.resolve()),
        "bytes_written": bytes_written,
        "read_content": read_content,
    }


def main(argv: list[str] | None = None) -> int:
    """CLI entry point demonstrating pathlib operations."""
    print("=== Object-Oriented Filesystem Path Operations (`pathlib.Path`) ===")

    info = get_current_directory_info()
    print(f"Current Directory: {info['current_working_directory']}")
    print(f"User Home Directory: {info['user_home_directory']}")

    sample_file = Path("required.txt")
    print(f"\nDecomposing '{sample_file}':")
    details = decompose_path(sample_file)
    for k, v in details.items():
        print(f"  {k}: {v}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
