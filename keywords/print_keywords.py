"""
Formatted Python Keywords Printer Module.

This module provides utility functions for iterating and displaying Python keywords
in formatted list or grid structures.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI argument processing.
# - `from python_keywords import get_all_python_keywords`: Keyword retrieval helper.
# =========================================================================
import sys

# Support both package and local directory import paths
try:
    from keywords.python_keywords import get_all_python_keywords
except ImportError:
    from python_keywords import get_all_python_keywords


def print_keywords_line_by_line() -> None:
    """Print each Python reserved keyword on its own line."""
    keywords = get_all_python_keywords()
    for key in keywords:
        print(key)


def print_keywords_grid(columns: int = 4) -> None:
    """Print Python reserved keywords in formatted column alignment.

    Args:
        columns (int): Number of columns per grid row. Defaults to 4.
    """
    keywords = get_all_python_keywords()
    print(f"--- Python Reserved Keywords Grid ({len(keywords)} Keywords) ---")

    for i in range(0, len(keywords), columns):
        row_items = keywords[i : i + columns]
        formatted_row = "  ".join(f"{kw:<12}" for kw in row_items)
        print(formatted_row)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for keyword printer."""
    print("=== Formatted Python Reserved Keywords Grid ===")
    print_keywords_grid(columns=5)
    return 0


if __name__ == "__main__":
    sys.exit(main())
