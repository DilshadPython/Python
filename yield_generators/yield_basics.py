# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and memory measurement (sys.getsizeof).
# - import types: Standard library module for generator object type verification (types.GeneratorType).
# - from typing import Any, Dict, Generator, List, Optional, Tuple, Union: PEP 484 type hint annotations.
# =========================================================================
import sys
import types
from typing import Any, Dict, Generator, List, Optional, Tuple, Union


# ─── 1. Basic Generator Function ──────────────────────────────────────────────
def count_up_generator(limit: int) -> Generator[int, None, str]:
    """
    Simple generator function demonstrating state suspension and lazy iteration with 'yield'.
    
    Args:
        limit (int): The maximum integer (inclusive) to count up to.
        
    Yields:
        int: The next incremental integer.
        
    Returns:
        str: A final summary string when StopIteration is raised (Python 3.3+ PEP 380).
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer")

    current = 1
    while current <= limit:
        yield current
        current += 1
    return f"Completed counting up to {limit}"


# ─── 2. Fibonacci Sequence Generator ─────────────────────────────────────────
def fibonacci_generator(count: int) -> Generator[int, None, None]:
    """
    Generates the Fibonacci sequence up to 'count' numbers without storing all values in memory.
    
    Args:
        count (int): The total number of Fibonacci elements to generate.
        
    Yields:
        int: The next Fibonacci number in the sequence.
    """
    if not isinstance(count, int):
        raise TypeError("Count must be an integer")
    if count < 0:
        raise ValueError("Count must be a non-negative integer")

    a, b = 0, 1
    generated = 0
    while generated < count:
        yield a
        a, b = b, a + b
        generated += 1


# ─── 3. Interactive / Bidirectional Generator ────────────────────────────────
def interactive_accumulator_generator(initial_total: float = 0.0) -> Generator[float, float, str]:
    """
    Demonstrates bidirectional generator communication using .send(), .throw(), and .close().
    
    Args:
        initial_total (float): The starting value for accumulation.
        
    Yields:
        float: The current accumulated total after receiving a sent value.
        
    Returns:
        str: A final summary message upon normal completion.
    """
    if not isinstance(initial_total, (int, float)):
        raise TypeError("Initial total must be a numeric value")

    total = float(initial_total)
    while True:
        try:
            # Yield current total and wait for value sent via generator.send(val)
            val = yield total
            if val is None:
                continue
            if not isinstance(val, (int, float)):
                raise ValueError("Sent value must be a numeric integer or float")
            total += float(val)
        except GeneratorExit:
            # Clean exit triggered by generator.close()
            return f"Accumulator closed cleanly at total: {total}"


# ─── 4. Delegating Generator using 'yield from' (PEP 380) ───────────────────
def delegating_generator(*iterables: Any) -> Generator[Any, None, List[Any]]:
    """
    Demonstrates generator delegation using the 'yield from' expression introduced in Python 3.3.
    
    Args:
        *iterables: One or more iterable objects (lists, tuples, generators).
        
    Yields:
        Any: Items yielded sequentially from each sub-iterable.
        
    Returns:
        List[Any]: A metadata summary list of processed iterable lengths.
    """
    summary_lengths: List[int] = []
    for it in iterables:
        # 'yield from' delegates iteration directly to the sub-iterable
        items = list(it)
        summary_lengths.append(len(items))
        yield from items
    return summary_lengths


# ─── 5. Streaming Data Pipeline Generator ──────────────────────────────────
def pipeline_filter_generator(data_stream: List[int], threshold: int = 10) -> Generator[int, None, None]:
    """
    Demonstrates chaining generators to build a memory-efficient data processing pipeline.
    
    Args:
        data_stream (List[int]): Input stream of raw integers.
        threshold (int): Minimum value threshold for filtering.
        
    Yields:
        int: Doubled value of numbers exceeding the threshold.
    """
    if not isinstance(data_stream, list):
        raise TypeError("data_stream must be a list of integers")

    # Step 1: Generator expression filtering values above threshold
    filtered_gen = (item for item in data_stream if item > threshold)

    # Step 2: Transform filtered items lazily
    for item in filtered_gen:
        yield item * 2


# ─── DEMONSTRATION FUNCTIONS ──────────────────────────────────────────────────

def demonstrate_yield_basics(limit: int = 5) -> Dict[str, Any]:
    """
    Demonstrates basic generator creation, state suspension, lazy iteration, and return value capture.
    """
    gen = count_up_generator(limit)
    is_gen_instance = isinstance(gen, types.GeneratorType)
    
    yielded_values: List[int] = []
    return_value: Optional[str] = None
    
    while True:
        try:
            val = next(gen)
            yielded_values.append(val)
        except StopIteration as stop_err:
            return_value = stop_err.value
            break

    return {
        "limit": limit,
        "is_generator_instance": is_gen_instance,
        "yielded_values": yielded_values,
        "return_value_pep_380": return_value,
        "memory_efficiency": "Values produced on demand, 1 element at a time.",
    }


def demonstrate_bidirectional_generator() -> Dict[str, Any]:
    """
    Demonstrates bidirectional generator communication using .send(), .throw(), and .close().
    """
    acc = interactive_accumulator_generator(10.0)
    initial_yield = next(acc)  # Prime the generator to the first yield (10.0)
    
    sent_1 = acc.send(5.5)     # Total becomes 15.5
    sent_2 = acc.send(20.0)    # Total becomes 35.5
    
    caught_exception: Optional[str] = None
    try:
        acc.send("invalid_input_string")
    except ValueError as ve:
        caught_exception = str(ve)

    acc.close()

    return {
        "initial_primed_value": initial_yield,
        "after_send_5_5": sent_1,
        "after_send_20_0": sent_2,
        "caught_exception_on_bad_send": caught_exception,
        "generator_closed_status": "Successfully closed via acc.close()",
    }


def demonstrate_yield_from_delegation() -> Dict[str, Any]:
    """
    Demonstrates 'yield from' sub-generator delegation (PEP 380).
    """
    list_a = [1, 2, 3]
    gen_b = count_up_generator(3)
    tuple_c = (10, 20)

    delegator = delegating_generator(list_a, gen_b, tuple_c)
    yielded_elements: List[Any] = []
    
    while True:
        try:
            val = next(delegator)
            yielded_elements.append(val)
        except StopIteration as stop_err:
            summary = stop_err.value
            break

    return {
        "source_inputs": [list_a, "[count_up_generator(3)]", tuple_c],
        "flattened_yielded_elements": yielded_elements,
        "sub_iterable_lengths_returned": summary,
    }


def demonstrate_generator_vs_list_memory(n_items: int = 100000) -> Dict[str, Any]:
    """
    Demonstrates the memory performance footprint of a Generator vs an in-memory List.
    """
    if not isinstance(n_items, int) or n_items <= 0:
        raise TypeError("n_items must be a positive integer")

    # In-memory list creation O(N) memory
    list_data = [x * 2 for x in range(n_items)]
    list_size_bytes = sys.getsizeof(list_data)

    # Lazy generator expression O(1) memory
    gen_data = (x * 2 for x in range(n_items))
    gen_size_bytes = sys.getsizeof(gen_data)

    ratio = round(list_size_bytes / gen_size_bytes, 2) if gen_size_bytes > 0 else 0.0

    return {
        "element_count": n_items,
        "list_memory_bytes": list_size_bytes,
        "generator_memory_bytes": gen_size_bytes,
        "memory_saving_ratio": f"Generator is ~{ratio}x lighter in RAM",
        "complexity": {
            "list": "O(N) space complexity",
            "generator": "O(1) constant space complexity",
        },
    }


def demonstrate_range_generator_evolution() -> Dict[str, Any]:
    """
    Demonstrates range sequence object vs custom yield generator, including dir() inspection.
    """
    r = range(1, 10, 2)
    range_dir_public = [attr for attr in dir(r) if not attr.startswith("_")]
    range_dunders = [attr for attr in dir(r) if attr in ("__iter__", "__len__", "__getitem__", "__contains__")]

    gen = (x for x in range(1, 10, 2))
    gen_dir_dunders = [attr for attr in dir(gen) if attr in ("__iter__", "__next__", "gi_code", "gi_frame", "gi_running")]

    return {
        "range_object_representation": str(r),
        "range_public_attributes": sorted(range_dir_public),
        "range_key_dunders": range_dunders,
        "generator_key_attributes": gen_dir_dunders,
        "python_version_notes": {
            "python_2_7": "range() created an immediate list in memory O(N). xrange() was used for lazy sequence generation.",
            "python_3_0": "xrange() was removed; range() became a lazy immutable sequence object with O(1) memory footprint.",
            "python_3_3": "PEP 380 introduced 'yield from' for generator delegation and returning values from generators.",
            "python_3_8": "PEP 479 made StopIteration inside generators raise RuntimeError instead of exiting silently.",
            "python_3_13": "CPython 3.13 optimized generator stack frames and bytecode execution for faster yield/next switching.",
        },
    }


def demonstrate_generator_attributes_and_dir() -> Dict[str, Any]:
    """
    Demonstrates internal generator attributes via dir() inspection (gi_code, gi_frame, gi_running).
    """
    gen = count_up_generator(3)
    gen_dir_all = dir(gen)
    
    public_methods = [m for m in gen_dir_all if not m.startswith("_")]
    gi_attributes = [a for a in gen_dir_all if a.startswith("gi_")]

    return {
        "generator_public_methods": public_methods,
        "generator_internal_gi_attributes": gi_attributes,
        "gi_running_initial": gen.gi_running,
        "gi_code_name": gen.gi_code.co_name,
    }
