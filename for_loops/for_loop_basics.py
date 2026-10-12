"""Python For Loops, Iteration Control & Iterator Mechanics (For Loop Module).

Import Notes & Architecture:
    - 'import sys': System parameter inspection, interpreter settings, and memory footprint analysis (sys.getsizeof).
    - 'import itertools': High-performance iterator tools (chain, cycle, islice, count, repeat, zip_longest).
    - 'import time': Execution timing benchmarks for loop performance comparisons.
    - 'from typing import Dict, List, Any, Union, Tuple, Optional, Iterable, Iterator': PEP 484 static type hint annotations.
"""

import sys
import itertools
import time
from typing import Dict, List, Any, Union, Tuple, Optional, Iterable, Iterator

Number = Union[int, float]


def starter_loop_examples() -> Dict[str, Any]:
    """Starter examples demonstrating Python loop structures (for, range, break, continue, else).

    Loops iterate over sequences or repeat block execution until a condition evaluates to False.
    """
    # 1. Standard 'for' loop over a list
    fruits = ["apple", "banana", "cherry"]
    collected_fruits: List[str] = []
    for fruit in fruits:
        collected_fruits.append(fruit.upper())

    # 2. 'for' loop using range(start, stop, step)
    range_numbers: List[int] = []
    for i in range(1, 10, 2):  # Odd numbers from 1 to 9
        range_numbers.append(i)

    # 3. 'for' loop counter accumulator
    counter = 0
    accumulated_sum = 0
    for step in range(1, 6):
        counter = step
        accumulated_sum += step

    # 4. Loop control keywords: 'continue' (skip step) and 'break' (exit loop early)
    filtered_sequence: List[int] = []
    for num in range(1, 20):
        if num % 2 == 0:
            continue  # Skip even numbers
        if num > 7:
            break  # Exit loop when number exceeds 7
        filtered_sequence.append(num)

    # 5. 'for-else' block execution (else clause executes ONLY if loop completes without hitting break)
    loop_completed_normally = False
    for item in [1, 2, 3]:
        if item == 99:  # Condition never met
            break
    else:
        loop_completed_normally = True

    return {
        "collected_fruits": collected_fruits,
        "range_numbers": range_numbers,
        "accumulated_counter": counter,
        "accumulated_sum": accumulated_sum,
        "filtered_sequence": filtered_sequence,
        "loop_completed_normally": loop_completed_normally,
    }


def enumerate_and_zip_iteration(
    names: List[str], scores: List[int]
) -> Dict[str, Any]:
    """Demonstrates index tracking via enumerate() and sequence pairing via zip() / zip_longest()."""
    if not isinstance(names, list) or not isinstance(scores, list):
        raise TypeError("Input arguments 'names' and 'scores' must be valid Python lists")

    # 1. enumerate(iterable, start=1): Attaches counter indices to sequence elements
    indexed_students: List[str] = []
    for rank, name in enumerate(names, start=1):
        indexed_students.append(f"#{rank} {name}")

    # 2. zip(*iterables): Aggregates elements from two or more iterables in parallel
    paired_results: List[Tuple[str, int]] = []
    for name, score in zip(names, scores):
        paired_results.append((name, score))

    # 3. itertools.zip_longest: Pairs elements up to longest input, padding missing values with fillvalue
    extra_scores = [98, 95, 88, 92]
    padded_pairs: List[Tuple[str, int]] = []
    for name, score in itertools.zip_longest(names, extra_scores, fillvalue="Anonymous"):
        padded_pairs.append((name, score))

    return {
        "indexed_students": indexed_students,
        "paired_results": paired_results,
        "padded_pairs": padded_pairs,
    }


def nested_loops_and_control_flow(
    matrix: List[List[int]], search_target: int
) -> Dict[str, Any]:
    """Demonstrates 2D matrix nested iteration, row flattening, and early multi-level break logic."""
    if not isinstance(matrix, list):
        raise TypeError("Input 'matrix' must be a valid 2D list")

    flattened_matrix: List[int] = []
    target_found = False
    target_coordinates: Optional[Tuple[int, int]] = None

    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            flattened_matrix.append(val)
            if val == search_target:
                target_found = True
                target_coordinates = (row_idx, col_idx)
                break  # Breaks inner loop
        if target_found:
            break  # Breaks outer loop

    return {
        "flattened_matrix": flattened_matrix,
        "target_found": target_found,
        "target_coordinates": target_coordinates,
    }


def execute_all_dir_loop_methods() -> Dict[str, Any]:
    """Demonstrates built-in methods and dunder attributes available on range, enumerate, and iterator objects."""
    sample_range = range(1, 10, 2)
    range_dir = [attr for attr in dir(sample_range) if not attr.startswith("__")]

    # Introspect range attributes
    r_start = sample_range.start
    r_stop = sample_range.stop
    r_step = sample_range.step
    r_count = sample_range.count(5)
    r_index = sample_range.index(5)

    # Iterator dunder protocol: __iter__ and __next__
    sample_list = [10, 20, 30]
    list_iterator = iter(sample_list)

    enum_obj = enumerate(sample_list)
    zip_obj = zip(sample_list, sample_list)

    return {
        "range_public_methods": range_dir,
        "range_start": r_start,
        "range_stop": r_stop,
        "range_step": r_step,
        "range_count_five": r_count,
        "range_index_five": r_index,
        "enum_has_next": hasattr(enum_obj, "__next__"),
        "zip_has_next": hasattr(zip_obj, "__next__"),
        "iterator_first_value": next(list_iterator),
        "iterator_second_value": next(list_iterator),
    }


def itertools_advanced_loops(items: List[str]) -> Dict[str, Any]:
    """Demonstrates high-performance iterator tools from the standard library 'itertools' module."""
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a valid list")

    # 1. itertools.chain: Combines multiple iterables into a single sequential stream
    chained_iter = list(itertools.chain(items, ["extra_1", "extra_2"]))

    # 2. itertools.islice: Slices an iterator lazily without loading full sequence into memory
    sliced_iter = list(itertools.islice(range(100), 5, 10))

    # 3. itertools.accumulate: Yields running accumulated totals
    accumulated_sum = list(itertools.accumulate([1, 2, 3, 4, 5]))

    # 4. itertools.cycle: Cycles indefinitely through an iterable (bounded using islice)
    cycled_colors = list(itertools.islice(itertools.cycle(["red", "green", "blue"]), 7))

    return {
        "chained_iter": chained_iter,
        "sliced_iter": sliced_iter,
        "accumulated_sum": accumulated_sum,
        "cycled_colors": cycled_colors,
    }


def dictionary_and_generator_iteration(
    mapping: Dict[str, Any]
) -> Dict[str, Any]:
    """Demonstrates dictionary key/value view iteration, generator expressions, and memory profiling."""
    if not isinstance(mapping, dict):
        raise TypeError("Input 'mapping' must be a valid dictionary")

    # 1. Dictionary iteration over items(), keys(), values()
    formatted_pairs: List[str] = []
    for key, val in mapping.items():
        formatted_pairs.append(f"{key}={val}")

    # 2. Generator expression vs eager list memory benchmarking
    eager_list = [x ** 2 for x in range(10000)]
    lazy_generator = (x ** 2 for x in range(10000))

    list_memory = sys.getsizeof(eager_list)
    gen_memory = sys.getsizeof(lazy_generator)

    return {
        "formatted_pairs": formatted_pairs,
        "dict_keys": list(mapping.keys()),
        "dict_values": [str(v) for v in mapping.values()],
        "generator_sum": sum(lazy_generator),
        "list_memory_bytes": list_memory,
        "gen_memory_bytes": gen_memory,
    }


def cross_version_loop_analysis() -> Dict[str, Any]:
    """Provides cross-version performance and structural comparison for Python loop constructs."""
    # Python 3.3 range object is an O(1) memory sequence
    range_obj = range(1000000)
    range_memory = sys.getsizeof(range_obj)

    return {
        "python_version": sys.version,
        "range_memory_bytes": range_memory,
        "is_lazy_range_sequence": isinstance(range_obj, Iterable),
        "bytecode_optimizations": "CPython 3.13 specialized FOR_ITER instruction opcodes enabled",
    }
