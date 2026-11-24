# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for CPython memory footprint inspection (sys.getsizeof).
# - import itertools: Standard library module providing memory-efficient iterator building blocks (chain, islice, cycle, accumulate).
# - from typing import Any, Dict, List, Tuple, Union, Iterator, Iterable: PEP 484 type annotations for static typing compliance.
# =========================================================================
import itertools
import sys
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple, Union


# =========================================================================
# TITLE 1: ITERABLE PROTOCOL & CUSTOM ITERATORS MECHANICS
# =========================================================================


class SquareIterator:
    """
    Custom stateful iterator demonstrating the Python Iterator Protocol.

    Implements:
    - __iter__(): Returns self as the iterator instance.
    - __next__(): Computes next squared integer or raises StopIteration when limit is reached.
    """

    def __init__(self, limit: int) -> None:
        if not isinstance(limit, int) or limit < 0:
            raise TypeError("Limit must be a non-negative integer.")
        self.limit: int = limit
        self.current: int = 0

    def __iter__(self) -> "SquareIterator":
        """Returns the iterator object itself."""
        return self

    def __next__(self) -> int:
        """Returns next squared integer or raises StopIteration."""
        if self.current >= self.limit:
            raise StopIteration
        result: int = self.current**2
        self.current += 1
        return result


class FibonacciIterator:
    """
    Custom stateful iterator producing Fibonacci sequence numbers up to a specified count.
    """

    def __init__(self, count: int) -> None:
        if not isinstance(count, int) or count < 0:
            raise TypeError("Count must be a non-negative integer.")
        self.count: int = count
        self.produced: int = 0
        self.a: int = 0
        self.b: int = 1

    def __iter__(self) -> "FibonacciIterator":
        return self

    def __next__(self) -> int:
        if self.produced >= self.count:
            raise StopIteration
        curr = self.a
        self.a, self.b = self.b, self.a + self.b
        self.produced += 1
        return curr


def demonstrate_iterable_protocol_and_manual_next() -> Dict[str, Any]:
    """
    Title 1 Example: Demonstrates iterable vs iterator distinction,
    manual next() extraction, StopIteration exception catching, and custom iterators.
    """
    sample_list: List[int] = [10, 20, 30]
    list_iter: Iterator[int] = iter(sample_list)

    # 1. Manual extraction using built-in next()
    elem1: int = next(list_iter)
    elem2: int = next(list_iter)
    elem3: int = next(list_iter)

    # 2. Verify StopIteration exception on exhaustion
    is_exhausted: bool = False
    try:
        next(list_iter)
    except StopIteration:
        is_exhausted = True

    # 3. Custom Iterator Protocol executions
    sq_iter = SquareIterator(limit=5)
    squared_results: List[int] = list(sq_iter)

    fib_iter = FibonacciIterator(count=7)
    fibonacci_results: List[int] = list(fib_iter)

    return {
        "manual_extraction": [elem1, elem2, elem3],
        "is_exhausted": is_exhausted,
        "custom_square_sequence": squared_results,
        "custom_fibonacci_sequence": fibonacci_results,
    }


# =========================================================================
# TITLE 2: BUILT-IN LAZY ITERATORS, FUNCTIONAL TOOLS & ITERTOOLS
# =========================================================================


def demonstrate_builtin_lazy_iterators() -> Dict[str, Any]:
    """
    Title 2 Example A: Demonstrates lazy functional built-in iterators
    (map, filter, zip, enumerate, reversed).
    """
    numbers: List[int] = [1, 2, 3, 4, 5, 6]

    mapped_obj: Iterator[int] = map(lambda x: x * 2, numbers)
    filtered_obj: Iterator[int] = filter(lambda x: x % 2 == 0, numbers)
    zipped_obj: Iterator[Tuple[int, str]] = zip(numbers, ["a", "b", "c", "d", "e", "f"])
    enumerated_obj: Iterator[Tuple[int, int]] = enumerate(numbers, start=100)
    reversed_obj: Iterator[int] = reversed(numbers)

    return {
        "map_results": list(mapped_obj),
        "filter_results": list(filtered_obj),
        "zip_results": list(zipped_obj),
        "enumerate_results": list(enumerated_obj),
        "reversed_results": list(reversed_obj),
    }


def demonstrate_generator_vs_list_memory_benchmark() -> Dict[str, Any]:
    """
    Title 2 Example B: Benchmarks generator expression O(1) constant RAM vs
    list comprehension O(N) linear RAM.
    """
    limit: int = 100000

    # Generator Expression (Lazy O(1) memory)
    gen_expr: Iterator[int] = (x**2 for x in range(limit))
    # List Comprehension (Eager O(N) memory)
    list_comp: List[int] = [x**2 for x in range(limit)]

    gen_size_bytes: int = sys.getsizeof(gen_expr)
    list_size_bytes: int = sys.getsizeof(list_comp)

    return {
        "limit_elements": limit,
        "generator_memory_bytes": gen_size_bytes,
        "list_memory_bytes": list_size_bytes,
        "is_generator_memory_efficient": gen_size_bytes < list_size_bytes,
    }


def demonstrate_itertools_building_blocks() -> Dict[str, Any]:
    """
    Title 2 Example C: Demonstrates standard library itertools building blocks
    (chain, islice, cycle, accumulate).
    """
    chained: List[int] = list(itertools.chain([1, 2], [3, 4], [5, 6]))
    sliced: List[int] = list(itertools.islice(range(100), 10, 15))
    cycled_sample: List[int] = list(itertools.islice(itertools.cycle([1, 2, 3]), 8))
    accumulated: List[int] = list(itertools.accumulate([1, 2, 3, 4, 5]))

    return {
        "itertools_chain": chained,
        "itertools_islice": sliced,
        "itertools_cycle_sample": cycled_sample,
        "itertools_accumulate": accumulated,
    }


# =========================================================================
# TITLE 3: RANGE SEQUENCE ITERATION, INTROSPECTION & VERSION EVOLUTION
# =========================================================================


def inspect_range_sequence_and_containment() -> Dict[str, Any]:
    """
    Title 3 Example A: Demonstrates range parameters (start, stop, step),
    O(1) constant memory benchmarks, and O(1) mathematical containment testing.
    """
    rng = range(2, 20, 3)  # Sequence: [2, 5, 8, 11, 14, 17]

    # Bounds and properties
    rng_start: int = rng.start
    rng_stop: int = rng.stop
    rng_step: int = rng.step
    rng_len: int = len(rng)

    # Sequence methods: index() & count()
    idx_8: int = rng.index(8) if 8 in rng else -1
    count_8: int = rng.count(8)

    # O(1) Memory benchmarks
    range_1k = range(1000)
    range_1m = range(1000000)
    range_1k_bytes: int = sys.getsizeof(range_1k)
    range_1m_bytes: int = sys.getsizeof(range_1m)

    # O(1) Containment testing
    is_14_in_range: bool = 14 in rng
    is_15_in_range: bool = 15 in rng

    return {
        "range_bounds": {
            "start": rng_start,
            "stop": rng_stop,
            "step": rng_step,
            "length": rng_len,
        },
        "sequence_methods": {"index_of_8": idx_8, "count_of_8": count_8},
        "containment_test": {
            "is_14_in_range": is_14_in_range,
            "is_15_in_range": is_15_in_range,
        },
        "memory_benchmark": {
            "range_1k_bytes": range_1k_bytes,
            "range_1m_bytes": range_1m_bytes,
            "is_constant_memory": range_1k_bytes == range_1m_bytes,
        },
    }


def inspect_range_and_iterator_dir_methods() -> Dict[str, Any]:
    """
    Title 3 Example B: Demonstrates introspection via dir(range) and dir(iter(range))
    listing all public attributes, sequence methods, and iterator dunders.
    """
    r = range(1, 10, 2)
    r_iter = iter(r)

    # Public sequence methods from dir(range)
    public_range_attrs: List[str] = sorted(
        [m for m in dir(range) if not m.startswith("_")]
    )
    # Iterator dunder methods from dir(iter(range))
    iter_dunders: List[str] = [m for m in dir(r_iter) if m in ("__iter__", "__next__")]

    return {
        "dir_range_public_methods": public_range_attrs,
        "iter_dunder_methods": iter_dunders,
        "range_attributes_values": {"start": r.start, "stop": r.stop, "step": r.step},
        "range_methods_exec": {"count_of_5": r.count(5), "index_of_5": r.index(5)},
    }


def demonstrate_python_version_evolution_matrix() -> Dict[str, Any]:
    """
    Title 3 Example C: Explains and demonstrates behavior changes across Python versions:
    - Python 2.7: xrange() vs range(), dict.iteritems(), iterator.next()
    - Python 3.3: range unified as immutable sequence, .index()/.count(), lazy map/filter/zip
    - Python 3.13: CPython 3.13 FOR_ITER bytecode specialization & zero-cost exception handling.
    """
    # 1. Range sequence representation
    modern_range = range(10)
    range_type: str = type(modern_range).__name__

    # 2. Dynamic dict view iteration
    sample_dict: Dict[str, int] = {"a": 1, "b": 2}
    items_view_type: str = type(sample_dict.items()).__name__

    # 3. Standard built-in next() function
    demo_iter = iter([100, 200])
    first_val: int = next(demo_iter)

    return {
        "range_type_name": range_type,
        "dict_items_type_name": items_view_type,
        "next_extracted_value": first_val,
        "version_comparison_notes": {
            "python_2_7": "range() returned list (O(N) RAM); xrange() returned iterator. Direct iterator.next() method. Dict used dict.iteritems().",
            "python_3_0_to_3_3": "xrange() removed; range unified as immutable O(1) RAM sequence. Standard next(it) function. map/filter/zip became lazy iterators.",
            "python_3_13": "CPython 3.13 adaptive FOR_ITER bytecode instruction specialization delivers 10-15% speedups for loops.",
        },
    }


def demonstrate_all_iterator_topics() -> Dict[str, Any]:
    """
    Master runner aggregating Title 1, Title 2, and Title 3 iterator functionality.
    """
    return {
        "title_1_iterable_protocol": demonstrate_iterable_protocol_and_manual_next(),
        "title_2_lazy_iterators": demonstrate_builtin_lazy_iterators(),
        "title_2_memory_benchmark": demonstrate_generator_vs_list_memory_benchmark(),
        "title_2_itertools": demonstrate_itertools_building_blocks(),
        "title_3_range_containment": inspect_range_sequence_and_containment(),
        "title_3_dir_introspection": inspect_range_and_iterator_dir_methods(),
        "title_3_version_evolution": demonstrate_python_version_evolution_matrix(),
    }
