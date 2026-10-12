"""
Intermediate Level Python Unpacking Demonstration Module.

This module provides functional unpacking patterns designed for intermediate developers
(extended iterable unpacking `head, *middle, tail = seq`, `*args` and `**kwargs` parameter delegation, `{**d1, **d2}`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Any, Dict, List, Tuple`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Any, Dict, List, Tuple


def demonstrate_extended_iterable_unpacking(items: List[int]) -> Tuple[int, List[int], int]:
    """Demonstrate Extended Iterable Unpacking (PEP 3132) to capture head, middle list, and tail.

    Args:
        items (List[int]): List of integers containing at least 2 elements.

    Returns:
        Tuple[int, List[int], int]: Unpacked (first_element, middle_elements_list, last_element).
    """
    head, *middle, tail = items
    return head, middle, tail


def demonstrate_varargs_kwargs_delegation(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Capture variable positional arguments (*args) and keyword arguments (**kwargs).

    Args:
        *args: Variable length positional arguments tuple.
        **kwargs: Variable length keyword arguments dictionary.

    Returns:
        Dict[str, Any]: Structured argument dictionary.
    """
    return {
        "positional_count": len(args),
        "positional_args": list(args),
        "keyword_keys": list(kwargs.keys()),
        "keyword_kwargs": kwargs,
    }


def demonstrate_dictionary_merge_unpacking(base: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Merge dictionaries using dictionary unpacking operator `{**base, **overrides}`.

    Args:
        base (Dict[str, Any]): Base configuration dictionary.
        overrides (Dict[str, Any]): User override dictionary.

    Returns:
        Dict[str, Any]: Combined merged dictionary.
    """
    return {**base, **overrides}


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate unpacking demonstration."""
    print("=== Intermediate Level Python Unpacking Demonstration ===")

    seq = [1, 2, 3, 4, 5]
    first, mid, last = demonstrate_extended_iterable_unpacking(seq)
    print(f"Extended Unpacking: Head={first}, Middle={mid}, Tail={last}")

    captured = demonstrate_varargs_kwargs_delegation(10, 20, "hello", mode="active", level=5)
    print(f"Varargs & Kwargs Unpacking: {captured}")

    merged = demonstrate_dictionary_merge_unpacking({"a": 1, "b": 2}, {"b": 99, "c": 3})
    print(f"Dictionary Merge Unpacking: {merged}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
