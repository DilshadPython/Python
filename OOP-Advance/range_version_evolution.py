"""Python Range Behavioral Evolution, Inspection, and Performance Module.

This module explains and demonstrates how `range` has evolved across Python versions:
- Python 2.7: `range()` returned a memory-allocated `list`. `xrange()` was a lazy generator object.
- Python 3.3+: `range` replaced `xrange()` as an immutable sequence type with O(1) membership testing (`in`).
- Python 3.13: Highly optimized C-level sequence implementation supporting slicing, negative steps, large integer bounds, and full container protocols.

It also demonstrates introspection of `range` using `dir()`.
"""

import sys
from typing import List, Tuple, Any


def inspect_range_attributes() -> List[str]:
    """Inspect all public and internal attributes/methods available on range objects using dir().

    Returns:
        List of attribute names.
    """
    r = range(0, 10, 2)
    return dir(r)


def demonstrate_range_features() -> Tuple[int, int, int, bool]:
    """Demonstrate range immutability, O(1) membership testing, slicing, and attributes.

    Returns:
        Tuple containing start, stop, step, and containment boolean result.
    """
    r = range(10, 100, 5)

    start_val = r.start
    stop_val = r.stop
    step_val = r.step
    contains_50 = 50 in r

    return start_val, stop_val, step_val, contains_50


def compare_range_memory_efficiency(n: int = 1_000_000) -> Tuple[int, int]:
    """Compare memory consumption of range generator object vs explicit list conversion.

    Args:
        n: Upper limit for range sequence.

    Returns:
        Tuple containing (bytes used by range, bytes used by list).
    """
    r = range(n)
    lst = list(r)
    return sys.getsizeof(r), sys.getsizeof(lst)


if __name__ == "__main__":
    print("=== Python Range Evolution & Introspection ===")

    print("\n--- 1. Range Attribute & Method Introspection using dir() ---")
    public_range_attrs = [attr for attr in inspect_range_attributes() if not attr.startswith("__")]
    dunder_range_attrs = [attr for attr in inspect_range_attributes() if attr.startswith("__")]
    print("Public Range Methods/Attributes:", public_range_attrs)
    print("Sample Dunder Methods:", dunder_range_attrs[:8])

    print("\n--- 2. Range Attributes & Sequence Operations ---")
    start, stop, step, contains_50 = demonstrate_range_features()
    print(f"range(10, 100, 5) -> start: {start}, stop: {stop}, step: {step}")
    print("Is 50 in range(10, 100, 5)?:", contains_50)

    print("\n--- 3. Memory Efficiency Comparison (range vs list) ---")
    range_bytes, list_bytes = compare_range_memory_efficiency(1_000_000)
    print(f"Memory for range(1,000,000): {range_bytes} bytes")
    print(f"Memory for list(1,000,000):  {list_bytes} bytes")
    print(f"Memory Savings Factor: {list_bytes / range_bytes:.1f}x smaller")
