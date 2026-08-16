"""
Demonstration and definition of print() from Python 2.7 to Python 3.13.

This script isolates the version groups where print definition/signature
changed, while displaying all identical versions together with notices.
"""

import sys
import io


# =====================================================================
# 1. GROUP 1: Python 2.7 (Statement Syntax)
# =====================================================================
# Definition in Python 2.7:
#   print [>> file,] [expression (',' expression)* [',']]
#
# Notice:
#   - In Python 2.7, print was a keyword statement, not a function.
#   - A trailing comma suppressed the newline.
#   - Redirection used the >> chevron operator.
#   - Parentheses wrapped items as a tuple: print("a", "b") -> ('a', 'b')
#   - Forward compatibility: `from __future__ import print_function` (PEP 3105)
#     enabled the Python 3 style function in Python 2.7.


def demo_group_python_2_7() -> None:
    print("\n--- [Group 1: Python 2.7] ---")
    print("Definition / Signature: print [>> file,] [expression (',' expression)* [',']]")
    print("Notice:")
    print("  * Statement keyword in Python 2.7 (no function call required).")
    print("  * Trailing comma: print 'Hello', -> prints 'Hello ' without newline.")
    print("  * Redirection: print >> sys.stderr, 'Error message'")
    print("  * Parentheses create a tuple in Python 2.7:")
    print("    In Python 2.7: print('A', 'B') -> ('A', 'B')")
    print("    In Python 3+:  print('A', 'B') -> A B")


# =====================================================================
# 2. GROUP 2: Python 3.0 – 3.2 (Identical Built-in Function)
# =====================================================================
# Definition in Python 3.0, 3.1, 3.2:
#   print(*objects, sep=' ', end='\n', file=sys.stdout)
#
# Notice:
#   - Python 3.0, 3.1, and 3.2 share the EXACT same signature.
#   - PEP 3105 turned print into a built-in function.
#   - Added `sep=' '` parameter to customize separator between items.
#   - Added `end='\n'` parameter to customize end character.
#   - Added `file=sys.stdout` to redirect output to any file-like object (.write() method).
#   - The `flush` parameter did NOT exist yet in 3.0-3.2 (required sys.stdout.flush()).


def demo_group_python_3_0_to_3_2() -> None:
    print("\n--- [Group 2: Python 3.0 - 3.2 (Grouped Identical)] ---")
    print("Definition / Signature: print(*objects, sep=' ', end='\\n', file=sys.stdout)")
    print("Notice:")
    print("  * Versions 3.0, 3.1, and 3.2 share the exact same signature.")
    print("  * 'sep' parameter example:")
    print("    print('2026', '08', '16', sep='-') ->", end=" ")
    print("2026", "08", "16", sep="-")
    print("  * 'end' parameter example:")
    print("    print('Loading...', end='') -> keeps cursor on same line.")
    print("  * 'file' parameter example:")
    buffer = io.StringIO()
    print("Captured in buffer via file=buffer", file=buffer)
    print(f"    Captured content: {buffer.getvalue().strip()}")
    print("  * Note: 'flush' keyword was not yet supported in Python 3.0 - 3.2.")


# =====================================================================
# 3. GROUP 3: Python 3.3 – 3.13 (Identical Built-in Function)
# =====================================================================
# Definition in Python 3.3 through Python 3.13:
#   print(*objects, sep=' ', end='\n', file=None, flush=False)
#
# Notice:
#   - Python 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, and 3.13
#     all share the EXACT same built-in function signature and implementation.
#   - Added `flush=False` keyword argument in Python 3.3.
#     When flush=True, output stream is forcibly flushed immediately.
#   - `file=None` now defaults to sys.stdout at runtime (if sys.stdout is None, no-op).
#   - String formatting integration evolved across versions:
#     * Python 3.6+: PEP 498 f-strings -> print(f"Hello, {name}")
#     * Python 3.8+: Debug format specifier -> print(f"{x=}")
#     * Python 3.12+: PEP 701 nested quotes and escapes inside f-strings
#     * Python 3.13+: Enhanced interactive REPL & colorized tracebacks.


def demo_group_python_3_3_to_3_13() -> None:
    print("\n--- [Group 3: Python 3.3 - 3.13 (Grouped Identical)] ---")
    print("Definition / Signature: print(*objects, sep=' ', end='\\n', file=None, flush=False)")
    print("Notice:")
    print("  * Versions 3.3 through 3.13 all share the exact same signature.")
    print("  * 'flush=True' forces immediate stream flushing without sys.stdout.flush().")
    print("    print('Immediate update', flush=True)")
    print("  * Python 3.6+ f-string integration:")
    user = "Developer"
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"    f-string output: Welcome {user}! Running Python {version}")
    print(f"  * Python 3.8+ debug specifier: {version=}")


def run_all_version_demos() -> None:
    print("=" * 70)
    print("  PYTHON PRINT DEFINITIONS & EVOLUTION (PYTHON 2.7 -> PYTHON 3.13)")
    print("  (Changed versions separated; identical versions grouped together)")
    print("=" * 70)
    demo_group_python_2_7()
    demo_group_python_3_0_to_3_2()
    demo_group_python_3_3_to_3_13()
    print("\n" + "=" * 70)


if __name__ == "__main__":
    run_all_version_demos()
