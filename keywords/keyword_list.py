"""
Backward-compatible wrapper script for keyword inspection.

This module delegates to `python_keywords.py`, outputting the list of Python keywords.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for process exit status.
# - `from python_keywords import get_all_python_keywords`: Keyword retrieval helper.
# =========================================================================
import sys

try:
    from keywords.python_keywords import get_all_python_keywords
except ImportError:
    from python_keywords import get_all_python_keywords


def run_legacy_demo() -> None:
    """Run legacy keyword list demonstration."""
    print("List of python keywords")
    print(get_all_python_keywords())


if __name__ == "__main__":
    run_legacy_demo()
