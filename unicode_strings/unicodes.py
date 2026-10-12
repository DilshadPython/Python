"""
Backward-compatible wrapper script for Unicode character metadata lookup.

This file delegates to `unicode_names.py`, replacing single-letter variable names
(a, b, c...) with informative, structured unicode inspection functions.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: Standard system interaction module.
# - `from unicode_names import inspect_symbol_suite`: Centralized unicode metadata lookup function.
# =========================================================================
import sys

try:
    from unicode_strings.unicode_names import inspect_symbol_suite
except ImportError:
    from unicode_names import inspect_symbol_suite


def run_unicode_demo() -> None:
    """Run unicode symbol inspection and print formatted outputs."""
    symbols = ["&", "£", "$", "@", "~", "^", "|", "%", "€"]
    results = inspect_symbol_suite(symbols)

    for item in results:
        print(f"{item['symbol']} : {item['name']}")


if __name__ == "__main__":
    run_unicode_demo()