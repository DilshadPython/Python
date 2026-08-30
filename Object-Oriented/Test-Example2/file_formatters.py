"""File Formatters and Composite Writer Module.

This module provides formatter components (`CSVFormatter`, `LogFormatter`) and a composite writer (`FileWriter`)
that formats data before persisting to disk.
"""

import datetime
from typing import List, Union, Type, Protocol


class FormatterProtocol(Protocol):
    """Protocol defining format method interface."""

    def format(self, data: Union[List[str], str]) -> str:
        """Format input data into string output."""
        ...


class CSVFormatter:
    """CSV Formatter quoting elements containing delimiters."""

    def __init__(self, delimiter: str = ",") -> None:
        """Initialize CSVFormatter with delimiter."""
        self.delimiter: str = delimiter

    def format(self, elements: List[str]) -> str:
        """Format list of strings into a delimiter-separated line.

        Args:
            elements: List of strings.

        Returns:
            Formatted CSV string.
        """
        formatted_elements = [
            f'"{item}"' if self.delimiter in item else item for item in elements
        ]
        return self.delimiter.join(formatted_elements)


class LogFormatter:
    """Log Formatter prepending timestamp to log messages."""

    def format(self, message: str) -> str:
        """Format string message with timestamp header.

        Args:
            message: Raw log message.

        Returns:
            Timestamped log string.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"{timestamp}   {message}"


class FileWriter:
    """Composite writer managing file stream lifetime and applying injected formatters."""

    def __init__(self, filename: str, formatter_cls: Type[Union[CSVFormatter, LogFormatter]]) -> None:
        """Initialize FileWriter.

        Args:
            filename: Target output file path.
            formatter_cls: Formatter class to instantiate.
        """
        self.filename: str = filename
        self.formatter = formatter_cls()
        self.file_handle = open(filename, "w", encoding="utf-8")

    def write(self, data: Union[List[str], str]) -> None:
        """Format data and write to file stream.

        Args:
            data: Raw input data.
        """
        formatted_text = self.formatter.format(data)  # type: ignore
        self.file_handle.write(formatted_text + "\n")

    def close(self) -> None:
        """Close file stream handle."""
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()


if __name__ == "__main__":
    print("=== File Formatters Demonstration ===")
    csv_writer = FileWriter("demo.csv", CSVFormatter)
    log_writer = FileWriter("demo.log", LogFormatter)

    csv_writer.write(["a", "b,2", "c"])
    log_writer.write("Demo log message")

    csv_writer.close()
    log_writer.close()
    print("Files successfully formatted and written.")
