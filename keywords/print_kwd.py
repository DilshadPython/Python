"""
Backward-compatible wrapper script for keyword iteration.

This module delegates to `print_keywords.py`, printing keywords line by line.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from print_keywords import print_keywords_line_by_line`: Line-by-line printing function.
# =========================================================================
try:
    from keywords.print_keywords import print_keywords_line_by_line
except ImportError:
    from print_keywords import print_keywords_line_by_line


if __name__ == "__main__":
    print_keywords_line_by_line()
