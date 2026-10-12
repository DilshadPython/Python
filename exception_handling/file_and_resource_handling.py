"""
Python Exception Handling: File I/O & Resource Management

This module demonstrates safe File I/O exception handling for `FileNotFoundError`,
`PermissionError`, and configuration file processing, comparing `try-finally`
versus Python context managers (`with` statement).

Key Concepts:
- `FileNotFoundError`: Trapped when attempting to open a non-existent file path.
- `PermissionError`: Trapped when file access permissions are denied.
- `with open(...) as f:` Context manager automatically closes file handles even if errors occur.
"""
import os
from typing import Optional


def read_config_file_try_finally(filepath: str) -> Optional[str]:
    """
    Reads a file using manual try-except-else-finally resource management.

    Args:
        filepath (str): Path to configuration file.

    Returns:
        Optional[str]: File content string, or None if reading failed.
    """
    file_handle = None
    try:
        file_handle = open(filepath, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Configuration file '{filepath}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filepath}'.")
        return None
    else:
        content = file_handle.read()
        return content
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"Cleanup: Explicitly closed file handle for '{filepath}'.")


def read_config_file_context_manager(filepath: str) -> Optional[str]:
    """
    Reads a file using Python's idiomatic `with` context manager.

    Args:
        filepath (str): Path to configuration file.

    Returns:
        Optional[str]: File content string, or None if reading failed.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error (Context Manager): File '{filepath}' not found.")
        return None
    except PermissionError:
        print(f"Error (Context Manager): Permission denied for '{filepath}'.")
        return None


def main() -> None:
    """Demonstrates File I/O exception handling."""
    print("=" * 60)
    print("7. File I/O & Resource Cleanup Demonstrations")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    valid_file = os.path.join(base_dir, "config_file.txt")
    invalid_file = os.path.join(base_dir, "missing_config.txt")

    # Ensure sample config file exists
    if not os.path.exists(valid_file):
        with open(valid_file, "w", encoding="utf-8") as f:
            f.write("port=8080\nhost=localhost\ndebug=true\n")

    # 1. Manual try-finally file reading
    print("\n--- 1. Manual `try-except-else-finally` File Reading ---")
    content = read_config_file_try_finally(valid_file)
    print(f"  Valid file content:\n{content}")

    _ = read_config_file_try_finally(invalid_file)

    # 2. Context Manager `with` file reading
    print("\n--- 2. Idiomatic `with` Context Manager File Reading ---")
    cm_content = read_config_file_context_manager(valid_file)
    print(f"  Context manager file content snippet: {cm_content.strip() if cm_content else None}")

    _ = read_config_file_context_manager(invalid_file)


if __name__ == "__main__":
    main()
