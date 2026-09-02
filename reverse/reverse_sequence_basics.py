# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and RAM memory measurement (sys.getsizeof).
# - from typing import Any, Dict, List, Tuple, Union: PEP 484 type annotations.
# =========================================================================
import sys
from typing import Any, Dict, List, Tuple, Union


# ─── SUBFOLDER 1: 01-FUNDAMENTALS ─────────────────────────────────────────────

def demonstrate_01_fundamentals_basics(
    sample_list: List[int] = None,
    sample_tuple: Tuple[str, ...] = None,
    sample_str: str = "Python"
) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> reverse_sequence_basics.py]
    Demonstrates fundamental sequence reversal using built-in reversed() iterator and
    in-place list.reverse() method.

    Args:
        sample_list (List[int], optional): Integer list to reverse. Defaults to [10, 20, 30, 40].
        sample_tuple (Tuple[str, ...], optional): String tuple. Defaults to ("alpha", "beta", "gamma").
        sample_str (str, optional): String. Defaults to "Python".

    Returns:
        Dict[str, Any]: Reversed collections and in-place mutation results.
    """
    if sample_list is None:
        sample_list = [10, 20, 30, 40]
    if sample_tuple is None:
        sample_tuple = ("alpha", "beta", "gamma")

    # 1. Reverse list, tuple, and string using reversed()
    reversed_list = list(reversed(sample_list))
    reversed_tuple = tuple(reversed(sample_tuple))
    reversed_str = "".join(reversed(sample_str))

    # 2. In-place mutation using list.reverse()
    working_list = list(sample_list)
    return_val = working_list.reverse()

    return {
        "original_list": sample_list,
        "reversed_list": reversed_list,
        "original_tuple": sample_tuple,
        "reversed_tuple": reversed_tuple,
        "original_str": sample_str,
        "reversed_str": reversed_str,
        "inplace_mutated_list": working_list,
        "inplace_return_val": return_val,
    }


def demonstrate_01_fundamentals_slicing(
    sample_list: List[int] = None,
    sample_str: str = "Developer"
) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> reverse_slicing_conversions.py]
    Demonstrates sequence slicing [::-1] and TypeError handling for un-reversible objects.

    Args:
        sample_list (List[int], optional): Input list. Defaults to [100, 200, 300, 400].
        sample_str (str, optional): Input string. Defaults to "Developer".

    Returns:
        Dict[str, Any]: Sliced reversed sequences and exception flags.
    """
    if sample_list is None:
        sample_list = [100, 200, 300, 400]

    # Full sequence reversal via slice
    sliced_list = sample_list[::-1]
    sliced_str = sample_str[::-1]

    # Type error verification
    set_type_error = False
    try:
        reversed({1, 2, 3})
    except TypeError:
        set_type_error = True

    return {
        "sliced_list": sliced_list,
        "sliced_str": sliced_str,
        "set_type_error_caught": set_type_error,
    }


# ─── SUBFOLDER 2: 02-ADVANCED-MATH-AND-OPERATORS ──────────────────────────────

class CustomCountdown:
    """Custom reversible class implementing __reversed__() protocol hook."""
    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self):
        return iter(range(1, self.count + 1))

    def __reversed__(self):
        for i in range(self.count, 0, -1):
            yield i * 10


def demonstrate_02_advanced_custom_reverse() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> custom_reversible_class.py]
    Demonstrates custom class reversal via __reversed__() hook vs fallback sequence protocol.

    Returns:
        Dict[str, Any]: Custom reversal results.
    """
    obj = CustomCountdown(4)
    forward_items = list(obj)
    reversed_items = list(reversed(obj))

    return {
        "forward_items": forward_items,
        "custom_reversed_items": reversed_items,
    }


def demonstrate_02_advanced_dict_and_matrix_reversing(
    sample_dict: Dict[str, int] = None,
    matrix: List[List[int]] = None
) -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> matrix_and_dict_reverse.py]
    Demonstrates dictionary reversing (keys, values, items) and 2D matrix transformations.

    Args:
        sample_dict (Dict[str, int], optional): Dict to reverse. Defaults to {"a": 1, "b": 2, "c": 3}.
        matrix (List[List[int]], optional): 2D grid matrix. Defaults to [[1, 2], [3, 4]].

    Returns:
        Dict[str, Any]: Reversed dictionary views and 2D matrix transformations.
    """
    if sample_dict is None:
        sample_dict = {"a": 1, "b": 2, "c": 3}
    if matrix is None:
        matrix = [[1, 2], [3, 4]]

    reversed_keys = list(reversed(sample_dict))
    reversed_values = list(reversed(sample_dict.values()))
    reversed_items = list(reversed(sample_dict.items()))

    row_reversed_matrix = matrix[::-1]
    col_reversed_matrix = [row[::-1] for row in matrix]
    rotated_180_matrix = [row[::-1] for row in matrix[::-1]]

    return {
        "reversed_keys": reversed_keys,
        "reversed_values": reversed_values,
        "reversed_items": reversed_items,
        "row_reversed_matrix": row_reversed_matrix,
        "col_reversed_matrix": col_reversed_matrix,
        "rotated_180_matrix": rotated_180_matrix,
    }


# ─── SUBFOLDER 3: 03-RANGE-EVOLUTION-AND-PERFORMANCE ──────────────────────────

def demonstrate_03_range_evolution_and_performance() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> range_reverse_evolution.py]
    Demonstrates reversing range sequences, O(1) RAM benchmarks, dir() introspection,
    and CPython version evolution matrix (Python 2.7 to 3.13).

    Returns:
        Dict[str, Any]: Performance benchmarks and CPython evolution notes.
    """
    # Negative step vs reversed(range)
    neg_step = list(range(10, 0, -2))
    rev_range = list(reversed(range(2, 11, 2)))

    # Memory benchmarks
    lazy_range_iter = reversed(range(1, 1_000_000))
    materialized_slice = list(range(1, 1_000))[::-1]

    lazy_mem = sys.getsizeof(lazy_range_iter)
    slice_mem = sys.getsizeof(materialized_slice)

    # Introspection via dir()
    public_attrs = sorted([attr for attr in dir(lazy_range_iter) if not attr.startswith("_")])
    dunder_methods = sorted([attr for attr in dir(lazy_range_iter) if attr in ("__iter__", "__next__")])

    return {
        "negative_step_range": neg_step,
        "reversed_range_list": rev_range,
        "are_equal": neg_step == rev_range,
        "lazy_range_iter_bytes": lazy_mem,
        "materialized_slice_bytes": slice_mem,
        "is_constant_memory": lazy_mem < slice_mem,
        "public_attrs": public_attrs,
        "dunder_methods": dunder_methods,
        "cpython_evolution": {
            "python_2_7": "range() allocated O(N) list RAM; xrange() was lazy generator; dict views lacked reversed().",
            "python_3_3": "range unified into O(1) immutable sequence; reversed(range(...)) optimized range_iterator.",
            "python_3_8": "reversed() added to dict keys, values, and items views maintaining insertion order.",
            "python_3_13": "CPython adaptive interpreter FOR_ITER bytecode specialization, free-threaded execution, zero-copy reversal.",
        },
    }


def run_all_reverse_module_demos() -> Dict[str, Any]:
    """
    Executes all subfolder module demonstrations in sequence.
    """
    return {
        "01_fundamentals": {
            "basics": demonstrate_01_fundamentals_basics(),
            "slicing": demonstrate_01_fundamentals_slicing(),
        },
        "02_advanced_math": {
            "custom_class": demonstrate_02_advanced_custom_reverse(),
            "dict_and_matrix": demonstrate_02_advanced_dict_and_matrix_reversing(),
        },
        "03_range_and_performance": demonstrate_03_range_evolution_and_performance(),
    }


if __name__ == "__main__":
    import pprint
    pprint.pprint(run_all_reverse_module_demos())
