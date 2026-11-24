"""Legacy Re-Format Script (Refactored).

This module updates the original `re_format.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular functions and regex formatting, see `name_formatter.py`.
"""

from name_formatter import format_name_regex_groups


def demonstrate_regex_group_format(name: str) -> str:
    """Format name using regex capturing groups.

    Args:
        name: Raw name string.

    Returns:
        Formatted name string.
    """
    return format_name_regex_groups(name)


if __name__ == "__main__":
    print("=== Legacy Re-Format (Refactored) ===")
    sample = "Claudia, Ms"
    formatted = demonstrate_regex_group_format(sample)
    print(f"Original: '{sample}' -> Formatted: '{formatted}'")