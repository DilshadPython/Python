"""
Sequence Reflection Demonstration Module (`reflection.py`).

Demonstrates recursive sequence reflection (reversal) for numbers, words, and custom lists.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from typing import Any, Sequence`: PEP 484 type hint generics.
# =========================================================================
from typing import Any, Sequence


def reflect(seq: Sequence[Any]) -> Sequence[Any]:
    """Recursively reverse (reflect) a sequence preserving its constructor type.

    Args:
        seq (Sequence[Any]): Target list, tuple, or string sequence.

    Returns:
        Sequence[Any]: Reversed sequence preserving original type.
    """
    ftype = type(seq)
    emptyseq = ftype()

    if seq == emptyseq:
        return emptyseq

    restrev = reflect(seq[1:])
    first = seq[0:1]

    result = restrev + first  # type: ignore
    return result


def main() -> None:
    """Run reflection sequence reversal demonstration."""
    print("Reversed List:", reflect([2, 4, 5, 6, 8, 9]))
    print("Reversed String:", reflect("Hello world"))


if __name__ == "__main__":
    main()
