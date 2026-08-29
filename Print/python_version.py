"""
Python Version & Print Definition Evolution (Python 2.7 to Python 3.13).

This module inspects the running interpreter version and defines the exact
evolution and formal signatures of `print` from Python 2.7 through Python 3.13,
grouping identical versions together and separating only where changes occurred.
"""

import sys
import inspect


# =====================================================================
# Grouped Print Definitions (Python 2.7 to Python 3.13)
# =====================================================================

PRINT_VERSION_DEFINITIONS = {
    # -----------------------------------------------------------------
    # Group 1: Python 2.7 (and Python 2.x Legacy)
    # -----------------------------------------------------------------
    "Python 2.7": {
        "type": "Statement / Keyword (Grammar construct)",
        "signature": "print [>> file,] [expression (',' expression)* [',']]",
        "future_import_signature": "print(*objects, sep=' ', end='\\n', file=sys.stdout)",
        "changes": [
            "print was a language statement, NOT a built-in function.",
            "Trailing comma suppressed newline: print 'Hello',",
            "Stream redirection used chevron syntax: print >> sys.stderr, 'Error'",
            "from __future__ import print_function enabled function syntax (PEP 3105)."
        ],
        "notice": (
            "Notice for Python 2.7:\n"
            "1. In Python 2.7, 'print' is a statement. Parentheses wrap expressions as tuples:\n"
            "   print('A', 'B') -> outputs ('A', 'B') instead of A B.\n"
            "2. No 'sep', 'end', or 'flush' keyword arguments exist without future import.\n"
            "3. Cannot be passed as a first-class function (e.g. map(print, items) is a SyntaxError)."
        )
    },

    # -----------------------------------------------------------------
    # Group 2: Python 3.0 – Python 3.2 (Identical Definition)
    # -----------------------------------------------------------------
    "Python 3.0 - 3.2": {
        "type": "Built-in Function (PEP 3105)",
        "signature": "print(*objects, sep=' ', end='\\n', file=sys.stdout)",
        "changes": [
            "Replaced the print statement with a standard built-in function.",
            "Added 'sep' parameter (default: single space ' ').",
            "Added 'end' parameter (default: newline '\\n').",
            "Added 'file' parameter (default: sys.stdout) replacing the old '>>' redirection.",
            "Became a first-class citizen (can be passed to higher-order functions like map/filter)."
        ],
        "notice": (
            "Notice for Python 3.0 - 3.2 (Grouped Identical):\n"
            "1. Python 3.0, 3.1, and 3.2 share the exact same print() signature.\n"
            "2. The 'flush' keyword argument did NOT exist in 3.0-3.2;\n"
            "   forcing stream output required an explicit sys.stdout.flush() call."
        )
    },

    # -----------------------------------------------------------------
    # Group 3: Python 3.3 – Python 3.13 (Identical Definition)
    # -----------------------------------------------------------------
    "Python 3.3 - 3.13": {
        "type": "Built-in Function with Stream Flush Control",
        "signature": "print(*objects, sep=' ', end='\\n', file=None, flush=False)",
        "changes": [
            "Added 'flush=False' keyword argument (Python 3.3+, PEP 3105).",
            "file=None explicitly defaults to sys.stdout at runtime.",
            "Signature remained 100% identical and stable across all versions 3.3 through 3.13.",
            "Enhanced formatting support via PEP 498 f-strings (Python 3.6+), debug '=' specifier (3.8+), and PEP 701 f-string parser (3.12+)."
        ],
        "notice": (
            "Notice for Python 3.3 - 3.13 (Grouped Identical):\n"
            "1. Python 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, and 3.13\n"
            "   all share the exact same built-in print definition:\n"
            "   print(*objects, sep=' ', end='\\n', file=None, flush=False)\n"
            "2. Setting flush=True forces the buffer to flush immediately without calling sys.stdout.flush().\n"
            "3. Formatting evolution across this span:\n"
            "   - Python 3.6+: f-strings (f'Value: {val}')\n"
            "   - Python 3.8+: Self-documenting f-strings (f'{val=}')\n"
            "   - Python 3.12+: PEP 701 quotes/nested expressions in f-strings\n"
            "   - Python 3.13+: Enhanced interactive REPL & colorized output."
        )
    }
}


def display_print_definitions() -> None:
    """Display the grouped print definitions and notices from Python 2.7 to 3.13."""
    print("=" * 70)
    print("  DEFINITION OF PRINT: PYTHON 2.7 TO PYTHON 3.13 (GROUPED EVOLUTION)")
    print("=" * 70)

    for group_name, info in PRINT_VERSION_DEFINITIONS.items():
        print(f"\n[{group_name}]")
        print(f"  Type:      {info['type']}")
        print(f"  Signature: {info['signature']}")
        print("  Key Changes:")
        for change in info["changes"]:
            print(f"    - {change}")
        print("\n  " + info["notice"].replace("\n", "\n  "))
        print("-" * 70)


def display_runtime_info() -> None:
    """Display the active runtime Python version and inspect current print()."""
    v = sys.version_info
    print("\n" + "=" * 70)
    print("  CURRENT INTERPRETER RUNTIME INFO")
    print("=" * 70)
    print(f"Active Python Version: {v.major}.{v.minor}.{v.micro} ({v.releaselevel.capitalize()})")
    print(f"Full System Version:   {sys.version}")

    # Inspect current built-in print docstring & signature
    print("\nCurrent Built-in print() Definition:")
    print(f"  Docstring Signature: {print.__doc__.splitlines()[0] if print.__doc__ else 'N/A'}")
    print(f"  Active Signature:    print(*objects, sep=' ', end='\\n', file=None, flush=False)")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    display_runtime_info()
    display_print_definitions()