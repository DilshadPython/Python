"""
Demonstrates generator-based context managers using contextlib, ExitStack for multi-resource
management, and contextlib.suppress for safe error handling during file building operations.
"""

# "import module" loads the os standard library module for filesystem operations.
import os
# "from module import name" imports specific context manager utilities and type annotations directly into local scope.
from contextlib import ExitStack, contextmanager, suppress
from typing import Dict, Generator, List



@contextmanager
def temporary_file_builder(filepath: str, initial_content: str = "") -> Generator[str, None, None]:
    """
    Generator-based context manager that creates a temporary file, yields its path,
    and guarantees file cleanup upon context exit.
    """
    with open(filepath, 'w', encoding='utf-8') as fh:
        if initial_content:
            fh.write(initial_content)

    try:
        yield filepath
    finally:
        # Guarantee cleanup of temporary file after context exit
        with suppress(FileNotFoundError):
            if os.path.exists(filepath):
                os.remove(filepath)


def build_multiple_files(file_map: Dict[str, str], target_dir: str) -> List[str]:
    """
    Safely write multiple files within a single context using ExitStack to manage resources.
    Returns list of created file paths.
    """
    created_paths: List[str] = []
    os.makedirs(target_dir, exist_ok=True)

    with ExitStack() as stack:
        for filename, content in file_map.items():
            full_path = os.path.join(target_dir, filename)
            fh = stack.enter_context(open(full_path, 'w', encoding='utf-8'))
            fh.write(content)
            created_paths.append(full_path)

    return created_paths


def remove_file_safely(filepath: str) -> bool:
    """Remove a file using contextlib.suppress to ignore FileNotFoundError."""
    with suppress(FileNotFoundError):
        os.remove(filepath)
        return True
    return False


if __name__ == '__main__':
    sample_path = 'temp_demo_build.txt'
    with temporary_file_builder(sample_path, "Contextlib generator demonstration\n") as path:
        print(f"File created at: {path}, exists: {os.path.exists(path)}")

    print(f"File exists after context exit: {os.path.exists(sample_path)}")
