"""
Demonstrates building a custom file writer context manager class wrapping open() and close().
"""
# "import module" loads the os standard library module for filesystem operations.
import os
# "from module import name" imports specific type annotation helpers directly into local scope.
from typing import Any, Optional, Type



class MessageWriter:
    """Custom file writer context manager opening file on __enter__ and closing on __exit__."""

    def __init__(self, filepath: str, mode: str = 'w') -> None:
        self.filepath = filepath
        self.mode = mode
        self.file_handle: Any = None

    def __enter__(self) -> Any:
        """Open destination file stream and return file object target."""
        self.file_handle = open(self.filepath, self.mode, encoding='utf-8')
        return self.file_handle

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any]
    ) -> None:
        """Safely close open file handle during context exit."""
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()


def write_message_with_writer(filepath: str, content: str) -> bool:
    """Write text content to file using MessageWriter context manager."""
    with MessageWriter(filepath, 'w') as f:
        f.write(content)
    return os.path.exists(filepath)


if __name__ == '__main__':
    out_file = os.path.join(os.path.dirname(__file__), 'with_sample.txt')
    success = write_message_with_writer(out_file, '# with EXPRESSION as TARGET: SUITE\n')
    print(f"Message written successfully: {success}")
