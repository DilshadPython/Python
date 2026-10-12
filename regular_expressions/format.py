"""Legacy Name Format Script (Refactored).

This module updates the original `format.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular functions and regex formatting, see `name_formatter.py`.
"""

from name_formatter import format_name_split


def demonstrate_format(name: str) -> str:
    """Format name from 'Last, First' to 'First Last'.

    Args:
        name: Raw name string.

    Returns:
        Formatted name string.
    """
    return format_name_split(name)


if __name__ == "__main__":
    print("=== Legacy Name Format (Refactored) ===")
    sample = "Smith, John"
    formatted = demonstrate_format(sample)
    print(f"Original: '{sample}' -> Formatted: '{formatted}'")
