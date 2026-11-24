"""Range vs XRange Historical Comparative and Method Introspection Module.

This module provides a detailed, executable analysis comparing Python 2.7 xrange()
with Python 3 range() objects, demonstrating range attributes, sequence methods,
O(1) containment testing, memory efficiency, and dir() introspection.
"""

# import sys for memory size inspection and type annotations
import sys
from typing import Any, Dict, List, Tuple


def compare_range_memory_and_type(count: int = 1_000_000) -> Dict[str, Any]:
    """Demonstrate O(1) constant memory allocation of Python 3 range objects.

    In Python 2.7, range(1_000_000) allocated a list of 1,000,000 integer pointers,
    consuming megabytes of RAM. In Python 3, range() returns an immutable sequence
    object whose memory size remains constant regardless of the stop bound.

    Args:
        count: Upper element count for range generation. Defaults to 1,000,000.

    Returns:
        Dict[str, Any]: Dictionary containing object type, length, memory footprint,
                        and list comparison memory footprint.

    Raises:
        TypeError: If count is not an integer.
        ValueError: If count is negative.
    """
    if not isinstance(count, int):
        raise TypeError(f"count must be an integer, got {type(count).__name__}")
    if count < 0:
        raise ValueError(f"count must be non-negative, got {count}")

    rng = range(count)
    rng_bytes = sys.getsizeof(rng)

    # For comparison, calculate list allocation size of small subset
    small_list_bytes = sys.getsizeof(list(range(min(count, 1000))))

    return {
        "range_type": type(rng).__name__,
        "length": len(rng),
        "range_memory_bytes": rng_bytes,
        "list_1000_memory_bytes": small_list_bytes,
        "is_constant_memory": True,
    }


def demonstrate_range_attributes(start: int = 2, stop: int = 20, step: int = 3) -> Dict[str, int]:
    """Extract and demonstrate the built-in attributes of a range object.

    Args:
        start: Starting bound (inclusive).
        stop: Ending bound (exclusive).
        step: Step increment.

    Returns:
        Dict[str, int]: Dictionary of start, stop, and step attributes.
    """
    rng = range(start, stop, step)
    return {
        "start": rng.start,
        "stop": rng.stop,
        "step": rng.step,
    }


def demonstrate_range_sequence_methods(
    target_range: range, search_value: int
) -> Dict[str, Any]:
    """Demonstrate sequence methods .index(), .count(), and O(1) containment (in operator).

    Python 3.3 added full support for sequence methods .index() and .count() on range.
    Python 3.2 optimized membership checking ('val in range') to O(1) constant time logic.

    Args:
        target_range: A range object instance.
        search_value: Value to query inside the range.

    Returns:
        Dict[str, Any]: Results of containment, index lookup, and count operations.

    Raises:
        TypeError: If target_range is not a range instance.
    """
    if not isinstance(target_range, range):
        raise TypeError(f"target_range must be a range object, got {type(target_range).__name__}")

    is_contained = search_value in target_range
    count = target_range.count(search_value)
    index_val: Any = None

    if is_contained:
        index_val = target_range.index(search_value)

    return {
        "search_value": search_value,
        "is_contained": is_contained,
        "count": count,
        "index": index_val,
    }


def introspect_range_attributes_and_methods() -> List[str]:
    """Retrieve all public and dunder attributes/methods of range using dir().

    Returns:
        List[str]: List of attribute names returned by dir(range).
    """
    rng = range(10)
    return dir(rng)


def print_range_xrange_comparisons() -> None:
    """Print comprehensive summary of range behavior and introspection."""
    print("=== 1. Range Memory Footprint & Efficiency (Python 3 vs Python 2.7) ===")
    mem_info = compare_range_memory_and_type(1_000_000)
    print(f"Object Type: {mem_info['range_type']}")
    print(f"Sequence Length: {mem_info['length']:,}")
    print(f"range(1,000,000) Memory Size: {mem_info['range_memory_bytes']} bytes (Constant O(1))")
    print(f"list(range(1,000)) Memory Size: {mem_info['list_1000_memory_bytes']} bytes")

    print("\n=== 2. Range Attributes (start, stop, step) ===")
    attrs = demonstrate_range_attributes(2, 20, 3)
    print(f"range(2, 20, 3) -> start: {attrs['start']}, stop: {attrs['stop']}, step: {attrs['step']}")

    print("\n=== 3. Range Sequence Methods & O(1) Containment (Python 3.2+ / 3.3+) ===")
    sample_rng = range(10, 100, 5)
    print(f"Target Range: {sample_rng}")
    print("Search for 25:", demonstrate_range_sequence_methods(sample_rng, 25))
    print("Search for 27:", demonstrate_range_sequence_methods(sample_rng, 27))

    print("\n=== 4. dir(range) Introspection ===")
    all_dir = introspect_range_attributes_and_methods()
    public_attrs = [attr for attr in all_dir if not attr.startswith("_")]
    dunder_methods = [attr for attr in all_dir if attr.startswith("__") and attr.endswith("__")]

    print("Public Attributes/Methods:", public_attrs)
    print(f"Dunder Methods Count: {len(dunder_methods)}")
    print("Sample Dunder Methods:", dunder_methods[:10])


if __name__ == "__main__":
    print_range_xrange_comparisons()
