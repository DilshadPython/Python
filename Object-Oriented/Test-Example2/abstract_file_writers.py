"""Abstract File Writers Module.

This module demonstrates polymorphic file writing using ABC (`abc.ABC`)
with `DelimFile` and `LogFile` implementations.
"""

import abc
import datetime
from typing import List, Union


class WriteFile(abc.ABC):
    """Abstract base class for file writers."""

    def __init__(self, filename: str) -> None:
        """Initialize WriteFile with output path."""
        self.filename: str = filename

    def append_line(self, line: str) -> None:
        """Append line to target file safely.

        Args:
            line: Line of text to write.
        """
        with open(self.filename, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")

    @abc.abstractmethod
    def write(self, data: Union[List[str], str]) -> None:
        """Abstract write method."""
        pass


class DelimFile(WriteFile):
    """Delimited file writer joining lists by delimiter."""

    def __init__(self, filename: str, delimiter: str = ",") -> None:
        """Initialize DelimFile."""
        super().__init__(filename)
        self.delimiter: str = delimiter

    def write(self, data: Union[List[str], str]) -> None:
        """Join elements by delimiter and append line.

        Args:
            data: List of elements or string.
        """
        if isinstance(data, list):
            line = self.delimiter.join(data)
        else:
            line = str(data)
        self.append_line(line)


class LogFile(WriteFile):
    """Log file writer prepending timestamp to log entries."""

    def write(self, data: Union[List[str], str]) -> None:
        """Prepend timestamp to log message and append line.

        Args:
            data: Log message string.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.append_line(f"{timestamp}    {data}")


if __name__ == "__main__":
    print("=== Abstract File Writers Demonstration ===")
    log = LogFile("demo_log.txt")
    delim = DelimFile("demo_delim.csv", ",")

    log.write("System initialised.")
    delim.write(["col1", "col2", "col3"])
    print("Abstract file writers executed successfully.")
