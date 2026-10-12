# import sys: Imports Python's built-in System-specific parameters & functions module.
# Used for stream redirection (e.g. sys.stdout for console output, sys.stderr for errors).
import sys

# from typing import TextIO: Imports type hint interface for Text I/O streams (file objects, sys.stdout, io.StringIO).
from typing import TextIO


def format_simple_message(message: str) -> str:
    """Formats a basic string message with strict type validation."""
    # Example Call: format_simple_message("Hello Python")
    # Explanation: Returns the string parameter directly if it's a valid string.
    # Output Produced: "Hello Python"
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    return str(message)


def format_multi_line(*lines: str) -> str:
    """Combines multiple arguments into a space-separated string line."""
    # Example Call: format_multi_line("Cloud", "Flask", "Python")
    # Explanation: Takes variable argument tuple *lines ("Cloud", "Flask", "Python") and joins them with " ".
    # Output Produced: "Cloud Flask Python"
    return " ".join(str(line) for line in lines)


def print_to_stream(stream: TextIO, message: str, end: str = "\n") -> None:
    """Outputs text to a custom stream (e.g. sys.stdout, sys.stderr, or io.StringIO)."""
    # Example Call: print_to_stream(buffer, "Stream Output Success")
    # Explanation: Writes the message string plus newline to the provided stream buffer, then flushes.
    # Output Produced: "Stream Output Success"
    stream.write(message + end)
    stream.flush()
