"""
Custom File Writer Context Manager Module.

This module demonstrates building a custom file writer context manager class
wrapping open() and close() file operations.
"""
# "import os" imports standard operating system interface routines.
import os
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import Any, Optional, Type, TextIO" imports type annotation helpers.
from typing import Any, Optional, Type, TextIO


class MessageWriter:
    """
    Custom file writer context manager opening file on __enter__ and closing on __exit__.
    """

    def __init__(self, filepath: str, mode: str = "w") -> None:
        """
        Initialize MessageWriter with file path and opening mode.

        Args:
            filepath (str): Path to output file.
            mode (str): File access mode ('w', 'a', etc.). Defaults to 'w'.
        """
        self.filepath = Path(filepath)
        self.mode = mode
        self.file_handle: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        """
        Open destination file stream and return file object target.

        Returns:
            TextIO: Opened text file stream object.
        """
        self.file_handle = open(self.filepath, self.mode, encoding="utf-8")
        return self.file_handle

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> None:
        """
        Safely close open file handle during context exit.
        """
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()


def write_message_with_writer(filepath: str, content: str) -> bool:
    """
    Write text content to file using MessageWriter context manager.

    Args:
        filepath (str): Target output file path.
        content (str): Text content to write.

    Returns:
        bool: True if file exists after writing.
    """
    with MessageWriter(filepath, "w") as writer_stream:
        writer_stream.write(content)
    return Path(filepath).exists()


if __name__ == "__main__":
    print("=== Custom MessageWriter Context Manager Demonstration ===")
    out_file = str(Path(__file__).parent / "with_sample.txt")
    success = write_message_with_writer(
        out_file, "# with EXPRESSION as TARGET: SUITE\n"
    )
    print(f"Message written successfully: {success}")
