"""xrange Compatibility and Historical Overview Module.

In Python 2.7, xrange() was a generator-like sequence type used to avoid creating
full lists in memory. In Python 3.0, xrange() was removed and renamed to range(),
making range() an immutable, O(1) memory sequence object.

This module re-exports the comparative functionality from range_vs_xrange.py.
"""

from range_vs_xrange import (
    compare_range_memory_and_type,
    demonstrate_range_attributes,
    demonstrate_range_sequence_methods,
    introspect_range_attributes_and_methods,
    print_range_xrange_comparisons,
)

__all__ = [
    "compare_range_memory_and_type",
    "demonstrate_range_attributes",
    "demonstrate_range_sequence_methods",
    "introspect_range_attributes_and_methods",
    "print_range_xrange_comparisons",
]

if __name__ == "__main__":
    print("[xrange.py] Deprecation Notice: Python 2 xrange() was replaced by Python 3 range().")
    print_range_xrange_comparisons()
