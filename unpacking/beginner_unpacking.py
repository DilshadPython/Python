"""
Beginner Level Python Unpacking Demonstration Module.

This module provides clear, well-commented examples of basic sequence unpacking,
tuple assignment, and wildcard item discarding (`_`) designed for beginner developers.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI execution exit codes.
# - `from typing import Tuple`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Tuple


def demonstrate_tuple_assignment(full_name: str) -> Tuple[str, str]:
    """Unpack a two-word string split result into separate first and last name variables.

    Args:
        full_name (str): Space-delimited string (e.g. "Dilshad Abdulla").

    Returns:
        Tuple[str, str]: Unpacked (first_name, last_name) tuple.
    """
    first_name, last_name = full_name.split(" ", 1)
    return first_name, last_name


def demonstrate_wildcard_discard(full_name: str) -> str:
    """Unpack a string while using the underscore (`_`) wildcard placeholder to ignore last name.

    Args:
        full_name (str): Space-delimited string (e.g. "Dilshad Abdulla").

    Returns:
        str: Extracted first name string.
    """
    first_name, _ = full_name.split(" ", 1)
    return first_name


def demonstrate_basic_list_unpacking(numbers: list[int]) -> Tuple[int, int, int]:
    """Unpack a 3-element integer list into three distinct variables.

    Args:
        numbers (list[int]): List of 3 integers.

    Returns:
        Tuple[int, int, int]: Unpacked variable values.
    """
    first, second, third = numbers
    return first, second, third


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner unpacking demonstration."""
    print("=== Beginner Level Python Unpacking Demonstration ===")

    fname, lname = demonstrate_tuple_assignment("Dilshad Abdulla")
    print(f"Tuple Assignment: First='{fname}', Last='{lname}'")

    fname_only = demonstrate_wildcard_discard("Dilshad Abdulla")
    print(f"Wildcard Discard (_): First='{fname_only}'")

    a, b, c = demonstrate_basic_list_unpacking([10, 20, 30])
    print(f"List Unpacking: a={a}, b={b}, c={c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
