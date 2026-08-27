import sys
from typing import TextIO

def format_simple_message(message: str) -> str:
    """Formats a basic string message with strict type validation."""
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    return str(message)

def format_multi_line(*lines: str) -> str:
    """Combines multiple arguments into a space-separated string line."""
    return " ".join(str(line) for line in lines)

def print_to_stream(stream: TextIO, message: str, end: str = "\n") -> None:
    """Outputs text to a custom stream (e.g. sys.stdout, sys.stderr, or io.StringIO)."""
    stream.write(message + end)
    stream.flush()