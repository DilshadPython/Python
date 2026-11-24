"""
Range Version Evolution & Sequence Performance Notes Module.

This module documents and demonstrates the evolution of the range object from Python 2.7 to Python 3.13:
- Python 2.7: range() returned a dynamic list in memory; xrange() provided sequence iteration.
- Python 3.0+: range() replaced xrange(), operating as an immutable sequence with O(1) memory footprint.
- Range Inspection: Demonstrates attributes (start, stop, step) and introspection via dir(range).
"""
# "import module" loads sys module from standard library into local namespace.
import sys
# "from typing import ..." imports Tuple and List annotations into local scope.
from typing import List, Tuple


def inspect_range_attributes() -> List[str]:
    """
    Inspect attributes and methods available on the range object using dir().

    Returns:
        List[str]: List of range attribute names excluding internal dunders.
    """
    r = range(1, 10)
    return [attr for attr in dir(r) if not attr.startswith("__")]


def demonstrate_range_features() -> Tuple[int, int, int, bool]:
    """
    Demonstrate range start, stop, step attributes and O(1) membership testing.

    Returns:
        Tuple[int, int, int, bool]: (start, stop, step, contains_50)
    """
    r = range(10, 100, 5)
    return r.start, r.stop, r.step, (50 in r)


def compare_range_memory_efficiency(count: int = 1_000_000) -> Tuple[int, int]:
    """
    Compare RAM memory consumption between range object and materialized list.

    Args:
        count (int): Upper bound number of elements.

    Returns:
        Tuple[int, int]: Byte sizes of (range_bytes, list_bytes).
    """
    r = range(count)
    lst = list(r[:1000])  # Sample list to avoid excessive memory allocation
    return sys.getsizeof(r), sys.getsizeof(lst)
