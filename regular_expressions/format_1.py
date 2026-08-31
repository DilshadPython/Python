"""Legacy Walrus Regex Name Format Script (Refactored).

This module updates the original `format_1.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular functions and regex formatting, see `name_formatter.py`.
"""

from name_formatter import format_name_regex_walrus


def demonstrate_walrus_format(name: str) -> str:
    """Format name using walrus operator (:=) regex search.

    Args:
        name: Raw name string.

    Returns:
        Formatted name string.
    """
    return format_name_regex_walrus(name)


if __name__ == "__main__":
    print("=== Legacy Walrus Regex Name Format (Refactored) ===")
    sample = "Trump, Mrs Donald"
    formatted = demonstrate_walrus_format(sample)
    print(f"Original: '{sample}' -> Formatted: '{formatted}'")