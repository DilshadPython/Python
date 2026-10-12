"""
Dir-Second Multi-Resource Context Manager Demonstration Module.

This module provides custom context manager implementations operating specifically
within the dir-second subfolder, emphasizing multi-resource context management,
ExitStack automation, and file stream safety.
"""

# "import os" imports standard operating system interface utilities.
import os
# "from contextlib import ExitStack, contextmanager" imports multi-context manager management tools.
from contextlib import ExitStack, contextmanager
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import Any, Generator, List, Optional, TextIO, Type" imports static type hint annotations.
from typing import Any, Generator, List, Optional, TextIO, Type


class DirSecondResourceHandler:
    """
    Class-based context manager for managing resource streams within the dir-second subfolder.

    Guarantees automatic file handle cleanup upon exiting the block, even when errors occur.
    """

    def __init__(self, filename: str, mode: str = "r") -> None:
        """
        Initialize DirSecondResourceHandler with target filename and file mode.

        Args:
            filename (str): Name of the file inside dir-second directory.
            mode (str): File mode ('r', 'w', 'a', etc.). Defaults to 'r'.
        """
        self.dir_path = Path(__file__).resolve().parent
        self.filepath = self.dir_path / filename
        self.mode = mode
        self.file_handle: Optional[TextIO] = None

    def __enter__(self) -> Optional[TextIO]:
        """
        Open the target file in dir-second directory and return file stream object.

        Returns:
            Optional[TextIO]: Opened text stream handle, or None if missing file.
        """
        try:
            self.file_handle = open(self.filepath, self.mode, encoding="utf-8")
            return self.file_handle
        except FileNotFoundError as err:
            print(f"[DirSecond] Handled missing file in __enter__: {err}")
            self.file_handle = None
            return None

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> bool:
        """
        Safely close file handle on context exit.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception type if raised inside block.
            exc_val (Optional[BaseException]): Exception value if raised inside block.
            exc_tb (Optional[Any]): Exception traceback object.

        Returns:
            bool: True if exception handled/suppressed, False otherwise.
        """
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()
        if exc_type is FileNotFoundError:
            print(f"[DirSecond] Suppressed missing file exception: {exc_val}")
            return True
        return False


@contextmanager
def managed_dir_second_file(
    filename: str, mode: str = "r"
) -> Generator[Optional[TextIO], None, None]:
    """
    Generator context manager managing text file streams in dir-second subfolder.

    Args:
        filename (str): Target file name within dir-second subfolder.
        mode (str): File opening mode.

    Yields:
        Generator[Optional[TextIO], None, None]: Text IO stream handle or None.
    """
    dir_path = Path(__file__).resolve().parent
    filepath = dir_path / filename
    stream: Optional[TextIO] = None
    try:
        if filepath.exists() or "w" in mode or "a" in mode:
            stream = open(filepath, mode, encoding="utf-8")
        yield stream
    finally:
        if stream and not stream.closed:
            stream.close()


def read_multiple_dir_second_files(filenames: List[str]) -> List[List[str]]:
    """
    Read multiple files concurrently in dir-second subfolder using ExitStack.

    Args:
        filenames (List[str]): List of target filenames in dir-second.

    Returns:
        List[List[str]]: List of line lists for each file opened.
    """
    dir_path = Path(__file__).resolve().parent
    results: List[List[str]] = []

    with ExitStack() as stack:
        handles = []
        for name in filenames:
            fpath = dir_path / name
            if fpath.exists():
                h = stack.enter_context(open(fpath, "r", encoding="utf-8"))
                handles.append(h)
            else:
                handles.append(None)

        for h in handles:
            if h is not None:
                results.append([line.rstrip("\n") for line in h])
            else:
                results.append([])

    return results


if __name__ == "__main__":
    print("=== Dir-Second Multi-Resource Context Manager Demonstration ===")
    logs = read_multiple_dir_second_files(["test_b.txt", "test_c.txt"])
    for idx, fname in enumerate(["test_b.txt", "test_c.txt"]):
        print(f"--- Content of {fname} ---")
        for line in logs[idx]:
            print(f"  {line}")
