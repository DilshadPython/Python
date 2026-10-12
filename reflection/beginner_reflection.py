"""
Beginner Level Sequence Reversal & Reflection Module (`beginner_reflection.py`).

This module provides clear, well-commented examples of fundamental sequence reversal methods
designed for beginner developers (recursive reversal, extended slicing `[::-1]`, built-in `reversed()`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Any, List, Sequence`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Any, List, Sequence


def reflect_recursive(seq: Sequence[Any]) -> Sequence[Any]:
    """Reverse a sequence using recursive base-case decomposition.

    Args:
        seq (Sequence[Any]): Input sequence (list, tuple, str).

    Returns:
        Sequence[Any]: Reversed sequence preserving original type.
    """
    seq_type = type(seq)
    empty_seq = seq_type()

    # Base case: empty sequence returns empty constructor instance
    if seq == empty_seq:
        return empty_seq

    # Recursive step: reverse rest of sequence and append first element
    return reflect_recursive(seq[1:]) + seq[0:1]  # type: ignore


def reflect_via_slicing(seq: Sequence[Any]) -> Sequence[Any]:
    """Reverse a sequence using Python extended step slicing syntax `[::-1]`.

    Args:
        seq (Sequence[Any]): Input sequence.

    Returns:
        Sequence[Any]: Reversed sequence.
    """
    return seq[::-1]


def reflect_via_reversed(seq: Sequence[Any]) -> List[Any]:
    """Reverse a sequence using built-in `reversed()` iterator.

    Args:
        seq (Sequence[Any]): Input sequence.

    Returns:
        List[Any]: Reversed items converted to list.
    """
    return list(reversed(seq))


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner reflection demonstration."""
    print("=== Beginner Level Sequence Reversal ===")

    numbers = [2, 4, 5, 6, 8, 9]
    greeting = "Hello world"

    print(f"Recursive List: {reflect_recursive(numbers)}")
    print(f"Recursive String: '{reflect_recursive(greeting)}'")
    print(f"Sliced List: {reflect_via_slicing(numbers)}")
    print(f"Reversed Iterator List: {reflect_via_reversed(numbers)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
