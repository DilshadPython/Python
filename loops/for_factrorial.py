"""Factorial Calculation (Spelling Correction: 'for_factrorial.py' -> 'for_factorial.py').

This module provides backwards compatibility for 'for_factrorial.py', delegating
factorial computation to the corrected 'for_factorial.py' module.

Import Notes:
    - 'from typing import Optional': Standard library typing import for static type annotations.
    - 'from for_factorial import calculate_factorial, demo_for_factorial': Imports factorial
      calculation functions from the corrected module.
"""

from typing import Optional
from for_factorial import calculate_factorial, demo_for_factorial


def run_legacy_factorial_demo(num: Optional[int] = 5) -> int:
    """Run factorial demo using corrected factorial calculation module."""
    return demo_for_factorial(num)


if __name__ == "__main__":
    demo_for_factorial()
