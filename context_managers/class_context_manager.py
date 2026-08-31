"""
Class-Based Context Manager Demonstration Module.

This module demonstrates building a custom context manager class implementing
__enter__() setup and __exit__() teardown for safe file handling.
"""
# "from pathlib import Path" imports object-oriented filesystem path utilities.
from pathlib import Path
# "from typing import Any, Optional, Type, TextIO" imports type hint annotations.
from typing import Any, Optional, Type, TextIO


class OpenTextFile:
    """
    Custom class-based context manager for opening and automatically closing files.
    """

    def __init__(self, filename: str, mode: str = "r") -> None:
        """
        Initialize file path and opening mode.

        Args:
            filename (str): Name or path of file.
            mode (str): File access mode ('r', 'w', 'a', etc.). Defaults to 'r'.
        """
        self.filepath = Path(filename)
        self.mode = mode
        self.file_handle: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        """
        Open the file resource and return the stream object.

        Returns:
            TextIO: Opened text file stream object.
        """
        self.file_handle = open(self.filepath, self.mode, encoding="utf-8")
        return self.file_handle

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        traceback: Optional[Any],
    ) -> None:
        """
        Guarantee file closure when exiting the with-statement block.
        """
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()


if __name__ == "__main__":
    print("=== Class-Based Context Manager Demonstration ===")
    demo_path = Path(__file__).parent / "myfile.txt"

    with OpenTextFile(str(demo_path), "w") as file_stream:
        file_stream.write("Add some message to the file\n")

    print(f"Is file stream closed after context exit? {file_stream.closed}")
