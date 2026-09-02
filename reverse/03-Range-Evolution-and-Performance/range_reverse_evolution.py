# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and RAM memory measurement (sys.getsizeof).
# - from typing import Any, Dict, List, Tuple: PEP 484 type annotations.
# =========================================================================
import sys
from typing import Any, Dict, List, Tuple


def demonstrate_range_reversing_mechanics() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> range_reverse_evolution.py]
    Demonstrates reversing range sequences using range(start, stop, negative_step)
    versus calling built-in reversed(range(...)).

    Returns:
        Dict[str, Any]: Generated countdown sequences and equality validation.
    """
    # 1. Countdown via negative step range(start, stop, step)
    negative_step_range = list(range(10, 0, -2))  # [10, 8, 6, 4, 2]

    # 2. Reversing a positive step range via reversed()
    forward_range = range(2, 11, 2)               # [2, 4, 6, 8, 10]
    reversed_range_iter = reversed(forward_range) # Lazy range_iterator object
    reversed_range_list = list(reversed_range_iter) # [10, 8, 6, 4, 2]

    # Sequence comparison: negative step range vs reversed(range)
    are_sequences_equal = negative_step_range == reversed_range_list

    return {
        "negative_step_range": negative_step_range,
        "forward_range_bounds": {"start": forward_range.start, "stop": forward_range.stop, "step": forward_range.step},
        "reversed_range_list": reversed_range_list,
        "are_sequences_equal": are_sequences_equal,
    }


def demonstrate_memory_and_dir_introspection() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> range_reverse_evolution.py]
    Demonstrates O(1) constant memory overhead of reversed(range(...)) vs O(N) list slicing,
    and inspects attributes of reversed iterator and range objects via dir().

    Returns:
        Dict[str, Any]: Memory benchmarks, dir() introspection, and version evolution notes.
    """
    # 1. Memory Benchmark: O(1) lazy reverse iterator vs O(N) materialized list slice
    large_range = range(1, 1_000_001)
    lazy_reversed_iter = reversed(large_range)
    
    # Materialized list slice allocates linear RAM
    small_list = list(range(1, 1_000))
    materialized_slice = small_list[::-1]

    lazy_iter_memory = sys.getsizeof(lazy_reversed_iter)
    range_memory = sys.getsizeof(large_range)
    list_slice_memory = sys.getsizeof(materialized_slice)

    # 2. Introspection matrix via dir()
    sample_list = [1, 2, 3]
    list_rev_iter = reversed(sample_list)

    public_dir_reversed = [attr for attr in dir(list_rev_iter) if not attr.startswith("_")]
    dunder_dir_reversed = [attr for attr in dir(list_rev_iter) if attr in ("__iter__", "__next__", "__length_hint__")]

    return {
        "lazy_reversed_iter_bytes": lazy_iter_memory,
        "range_object_bytes": range_memory,
        "materialized_list_slice_bytes": list_slice_memory,
        "is_lazy_memory_constant": lazy_iter_memory < 100 and range_memory < 100,
        "public_methods_dir_reversed": sorted(public_dir_reversed),
        "dunder_methods_dir_reversed": sorted(dunder_dir_reversed),
        "cpython_evolution": {
            "python_2_7": (
                "In Python 2.7, range() created an eager list consuming O(N) memory. "
                "xrange() was a custom sequence type. reversed(xrange(...)) worked, "
                "dict views (.keys(), .values()) were un-ordered lists without reversed() support."
            ),
            "python_3_3": (
                "Python 3 unified range into an immutable O(1) sequence with .start, .stop, .step, "
                ".index(), and .count(). reversed(range(...)) returned a specialized range_iterator."
            ),
            "python_3_8": (
                "Python 3.8 enabled built-in reversed() support on dict objects, dict_keys, "
                "dict_values, and dict_items views, reflecting insertion order."
            ),
            "python_3_13": (
                "CPython 3.13 introduces adaptive bytecode specialization for FOR_ITER, "
                "optimizing reverse iterator loop dispatch, free-threaded GIL-free execution, "
                "and zero-copy sequence slicing."
            ),
        },
    }


if __name__ == "__main__":
    print(demonstrate_range_reversing_mechanics())
    print(demonstrate_memory_and_dir_introspection())
