"""
Dir-First Resource Context Manager Demonstration Module.

This module provides custom context manager implementations operating specifically
within the dir-first isolated subfolder, managing file streams and working directory safety.
"""

# "import os" imports standard operating system routines for directory manipulation.
import os
# "from contextlib import contextmanager" imports decorator converting generator functions into context managers.
from contextlib import contextmanager
# "from pathlib import Path" imports object-oriented filesystem path utilities.
from pathlib import Path
# "from typing import Any, Generator, List, Optional, TextIO, Type" imports static type hint annotations.
from typing import Any, Generator, List, Optional, TextIO, Type


class DirFirstResourceHandler:
    """
    Class-based context manager for managing files within the dir-first directory.
    
    Guarantees automatic file handle closing upon exit, even if exceptions occur.
    """

    def __init__(self, filename: str, mode: str = "r") -> None:
        """
        Initialize DirFirstResourceHandler with target filename and file mode.

        Args:
            filename (str): Name of the file inside dir-first.
            mode (str): File mode ('r', 'w', 'a', etc.). Defaults to 'r'.
        """
        self.dir_path = Path(__file__).resolve().parent
        self.filepath = self.dir_path / filename
        self.mode = mode
        self.file_handle: Optional[TextIO] = None

    def __enter__(self) -> Optional[TextIO]:
        """
        Open the target file within dir-first directory and return file stream object.

        Returns:
            Optional[TextIO]: Opened text file stream handle, or None if missing in read mode.
        """
        try:
            self.file_handle = open(self.filepath, self.mode, encoding="utf-8")
            return self.file_handle
        except FileNotFoundError as err:
            print(f"[DirFirst] Handled missing file in __enter__: {err}")
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
            exc_type (Optional[Type[BaseException]]): Caught exception class.
            exc_val (Optional[BaseException]): Caught exception instance.
            exc_tb (Optional[Any]): Exception traceback.

        Returns:
            bool: True if exception handled/suppressed, False otherwise.
        """
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()
        if exc_type is FileNotFoundError:
            print(f"[DirFirst] Suppressed missing file exception: {exc_val}")
            return True
        return False


@contextmanager
def managed_dir_first_file(
    filename: str, mode: str = "r"
) -> Generator[Optional[TextIO], None, None]:
    """
    Generator context manager managing text files in dir-first subfolder.

    Args:
        filename (str): File name in dir-first subfolder.
        mode (str): File opening mode.

    Yields:
        Generator[Optional[TextIO], None, None]: Opened text file stream handle or None.
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


def read_dir_first_lines(filename: str) -> List[str]:
    """
    Read stripped lines from a file located in dir-first subfolder safely using context manager.

    Args:
        filename (str): File name in dir-first subfolder.

    Returns:
        List[str]: List of stripped text lines.
    """
    lines: List[str] = []
    with DirFirstResourceHandler(filename, "r") as stream:
        if stream:
            for line in stream:
                lines.append(line.rstrip("\n"))
    return lines


if __name__ == "__main__":
    print("=== Dir-First Resource Context Manager Demonstration ===")
    sample_lines = read_dir_first_lines("test_a.txt")
    print(f"Read {len(sample_lines)} lines from test_a.txt:")
    for line in sample_lines:
        print(f"  - {line}")
