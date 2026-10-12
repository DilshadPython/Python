"""
Generator & Contextlib Utilities Module.

This module demonstrates generator-based context managers using @contextmanager, ExitStack for multi-resource
management, and contextlib.suppress for safe error handling during file building operations.
"""
# "import os" imports standard operating system interface routines.
import os
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from contextlib import ExitStack, contextmanager, suppress" imports contextlib utility tools.
from contextlib import ExitStack, contextmanager, suppress
# "from typing import Dict, Generator, List" imports type hint annotations.
from typing import Dict, Generator, List


@contextmanager
def temporary_file_builder(
    filepath: str, initial_content: str = ""
) -> Generator[str, None, None]:
    """
    Generator-based context manager that creates a temporary file, yields its path,
    and guarantees file cleanup upon context exit.

    Args:
        filepath (str): Path to temporary file.
        initial_content (str): Text content to write on creation.
    """
    path = Path(filepath)
    with open(path, "w", encoding="utf-8") as file_handle:
        if initial_content:
            file_handle.write(initial_content)

    try:
        yield str(path)
    finally:
        # Guarantee cleanup of temporary file after context exit
        with suppress(FileNotFoundError):
            if path.exists():
                path.unlink()


def build_multiple_files(file_map: Dict[str, str], target_dir: str) -> List[str]:
    """
    Safely write multiple files within a single context using ExitStack to manage resources.

    Args:
        file_map (Dict[str, str]): Map of filenames to contents.
        target_dir (str): Destination directory path.

    Returns:
        List[str]: List of created file paths.
    """
    created_paths: List[str] = []
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)

    with ExitStack() as stack:
        for filename, content in file_map.items():
            full_path = target_path / filename
            file_handle = stack.enter_context(open(full_path, "w", encoding="utf-8"))
            file_handle.write(content)
            created_paths.append(str(full_path))

    return created_paths


def remove_file_safely(filepath: str) -> bool:
    """
    Remove a file using contextlib.suppress to ignore FileNotFoundError.

    Args:
        filepath (str): Target file path.

    Returns:
        bool: True if file was removed, False if file did not exist.
    """
    path = Path(filepath)
    if not path.exists():
        return False

    with suppress(FileNotFoundError):
        path.unlink()
        return True
    return False


if __name__ == "__main__":
    print("=== Contextlib Generator & ExitStack Demonstration ===")
    sample_path = "temp_demo_build.txt"
    with temporary_file_builder(
        sample_path, "Contextlib generator demonstration\n"
    ) as pth:
        print(f"File created at: {pth}, exists: {Path(pth).exists()}")

    print(f"File exists after context exit: {Path(sample_path).exists()}")
