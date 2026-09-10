"""
Backward-compatible wrapper script for pathlib demonstration.

This module delegates to `pathlib_tutorial.py`, replacing raw print statements with
structured `pathlib.Path` helper functions.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for execution status.
# - `from pathlib_tutorial import get_current_directory_info, decompose_path`:
#   Structured functions inspecting paths using pathlib.Path.
# =========================================================================
import sys

try:
    from python_library.pathlib_tutorial import (
        get_current_directory_info,
        decompose_path,
    )
except ImportError:
    from pathlib_tutorial import (
        get_current_directory_info,
        decompose_path,
    )


def run_path_demo() -> None:
    """Run directory inspection demonstration."""
    info = get_current_directory_info()
    print(info["current_working_directory"], "\n ==>> This is the current dir")
    print("=" * 45)

    sample_file = "required.txt"
    details = decompose_path(sample_file)
    print(f"Path '{sample_file}' exists: {details['exists']}")


if __name__ == "__main__":
    run_path_demo()