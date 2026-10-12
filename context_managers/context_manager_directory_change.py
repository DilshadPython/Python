"""
Directory Changing Context Manager Demonstration Module.

This module demonstrates using a context manager to temporarily change working directories,
guaranteeing restoration of the original directory upon exit.
"""
# "import os" imports standard operating system interface routines.
import os
# "from contextlib import contextmanager" imports context manager decorator.
from contextlib import contextmanager
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import Generator" imports generator type hint annotation.
from typing import Generator


@contextmanager
def change_directory(target_path: Path) -> Generator[Path, None, None]:
    """
    Context manager that temporarily changes working directory to target_path,
    restoring original directory upon context exit.

    Args:
        target_path (Path): Path to target directory.
    """
    original_directory = os.getcwd()
    target_path.mkdir(parents=True, exist_ok=True)
    os.chdir(target_path)
    try:
        yield target_path
    finally:
        os.chdir(original_directory)


if __name__ == "__main__":
    print("=== Directory Change Context Manager Demonstration ===")
    base_dir = Path(__file__).parent
    dir_first = base_dir / "dir_first"
    dir_second = base_dir / "dir_second"

    print(f"Starting directory: {os.getcwd()}")

    with change_directory(dir_first):
        print(f"Inside dir_first context : {os.getcwd()}")

    with change_directory(dir_second):
        print(f"Inside dir_second context: {os.getcwd()}")

    print(f"Restored directory       : {os.getcwd()}")
