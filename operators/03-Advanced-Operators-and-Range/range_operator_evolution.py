"""
Python Operators: Range Sequence Evolution & Introspection Module.

This module documents and demonstrates:
- Range Sequence Operators: Containment (in, not in), Slicing (range[a:b:c]), Equality (==)
- Version Evolution: Python 2.7 range() list vs xrange() generator ➔ Python 3.0+ immutable range sequence
- Performance Notes: O(1) memory evaluation via sys.getsizeof() and O(1) containment testing
- Introspection Matrix: Attribute and method discovery using dir(range)
"""
# "import module" loads sys module into local namespace.
import sys
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Tuple


def inspect_range_attributes() -> List[str]:
    """
    Inspect all public attributes and methods available on the range object using dir().

    Returns:
        List[str]: List of range sequence attribute names excluding internal dunders.
    """
    r = range(1, 10)
    return [attr for attr in dir(r) if not attr.startswith("__")]


def demonstrate_range_operator_features() -> Tuple[int, int, int, bool, int, int]:
    """
    Demonstrate range sequence start, stop, step attributes, containment testing, indexing, and count.

    Returns:
        Tuple: (start, stop, step, contains_45, indexed_item, count_of_30).
    """
    r = range(10, 100, 5)

    contains_45 = 45 in r
    indexed_item = r[4]     # 10 + 4*5 = 30
    count_of_30 = r.count(30)

    return r.start, r.stop, r.step, contains_45, indexed_item, count_of_30


def compare_range_memory_efficiency(element_count: int = 1_000_000) -> Tuple[int, int]:
    """
    Compare RAM memory consumption between immutable range object and materialized list.

    Args:
        element_count (int): Upper bound sequence length.

    Returns:
        Tuple[int, int]: Byte sizes of (range_bytes, list_sample_bytes).
    """
    r = range(element_count)
    lst_sample = list(r[:1000])  # Sample list to avoid excessive memory allocation

    return sys.getsizeof(r), sys.getsizeof(lst_sample)
