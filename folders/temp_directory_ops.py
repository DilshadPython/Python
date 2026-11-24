"""Temporary Directory Operations Module.

Provides utilities for creating self-cleaning temporary directories using
`tempfile.TemporaryDirectory` context manager and explicit `tempfile.mkdtemp`.
"""

import shutil
import tempfile
from pathlib import Path
from typing import Generator


def create_temp_directory_context(prefix: str = "demo_tmp_") -> None:
    """Demonstrate auto-cleanup temporary directory via context manager.

    Args:
        prefix: Prefix for the temporary directory name.
    """
    with tempfile.TemporaryDirectory(prefix=prefix) as temp_dir:
        temp_path = Path(temp_dir)
        print(f"[tempfile.TemporaryDirectory] Created temporary directory: '{temp_path}'")
        
        # Write a sample file
        sample_file = temp_path / "data.txt"
        sample_file.write_text("Temporary file contents.")
        print(f"  - Created file: '{sample_file}' (Exists: {sample_file.exists()})")
        
    print(f"  - Outside context block (Directory exists: {temp_path.exists()})")


def create_temp_directory_explicit(prefix: str = "demo_tmp_") -> Path:
    """Create a temporary directory requiring explicit cleanup using `tempfile.mkdtemp`.

    Args:
        prefix: Prefix for the temporary directory name.

    Returns:
        Path object pointing to created temporary directory.
    """
    temp_dir_str = tempfile.mkdtemp(prefix=prefix)
    temp_path = Path(temp_dir_str)
    print(f"[tempfile.mkdtemp] Created explicit temporary directory: '{temp_path}'")
    return temp_path


def main() -> None:
    """Demonstrate temporary directory operations."""
    print("--- Temporary Directory Operations ---")
    
    # 1. Context manager approach (recommended)
    print("\n1. Managed Context Temporary Directory:")
    create_temp_directory_context(prefix="context_demo_")
    
    # 2. Explicit creation and cleanup
    print("\n2. Explicit Temporary Directory Creation & Cleanup:")
    tmp_path = create_temp_directory_explicit(prefix="explicit_demo_")
    (tmp_path / "log.txt").write_text("Log payload")
    print(f"  - Temporary file exists: {(tmp_path / 'log.txt').exists()}")
    
    # Manual cleanup
    shutil.rmtree(tmp_path)
    print(f"  - Cleaned up directory (Exists: {tmp_path.exists()})")


if __name__ == "__main__":
    main()
