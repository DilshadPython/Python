"""Object Composition Demonstration Module.

This module demonstrates Object Composition ("Has-A" relationships) in Python.
Instead of using inheritance ("Is-A"), a class delegates behavior to an injected object component
(such as an `io.StringIO` instance or a file stream writer).
"""

import io
from typing import Protocol, Any


class WriterProtocol(Protocol):
    """Protocol defining the interface required for writer components."""

    def write(self, s: str) -> int:
        """Write string content to destination."""
        ...


class TextComposer:
    """Class showcasing object composition by delegating writing to an injected writer component."""

    def __init__(self, writer: Any) -> None:
        """Initialize TextComposer with a writer component.

        Args:
            writer: Object implementing a write(str) method.
        """
        self.writer: Any = writer

    def write_message(self, message: str = "This is the message we write.") -> None:
        """Delegate message writing to the injected writer object.

        Args:
            message: String message to write.
        """
        self.writer.write(message)


if __name__ == "__main__":
    print("=== Object Composition Demonstration ===")

    # 1. Composing with io.StringIO in-memory stream
    string_stream = io.StringIO()
    composer = TextComposer(string_stream)
    composer.write_message("Hello from Object Composition!")
    print("In-Memory Stream Output:", string_stream.getvalue())

    # 2. Composing with file stream
    file_path = "composition_test.txt"
    with open(file_path, "w", encoding="utf-8") as file_handle:
        file_composer = TextComposer(file_handle)
        file_composer.write_message("Persisted message via file writer composition.")

    with open(file_path, "r", encoding="utf-8") as file_handle:
        print("File Stream Output:", file_handle.read())
