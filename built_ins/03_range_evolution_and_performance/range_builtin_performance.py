"""
Built-in Range Sequence Performance, Introspection, and Version Evolution Module.

This module demonstrates using Python `range()` built-in sequence generators,
benchmarks memory efficiency ($O(1)$ RAM footprint for range sequence objects),
inspects `dir(range)` public members, and documents built-in function evolutions
from Python 2.7 to 3.13.

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13 standards.
"""

import sys
from typing import Any, Dict, Generator, List, Tuple


def generate_builtin_step_sequence(start: int, stop: int, step: int = 1) -> range:
    """
    Constructs an O(1) memory sequence range representing built-in stepping sequences.

    Args:
        start (int): Start boundary index.
        stop (int): Stop boundary index.
        step (int): Stepping increment.

    Returns:
        range: Range sequence object.
    """
    return range(start, stop, step)


def inspect_range_attributes(r: range) -> Dict[str, Any]:
    """
    Performs runtime introspection on a range sequence instance using dir().

    Args:
        r (range): Target range sequence instance.

    Returns:
        Dict[str, Any]: Public attributes and method availability.
    """
    return {
        "start": r.start,
        "stop": r.stop,
        "step": r.step,
        "has_count": hasattr(r, "count"),
        "has_index": hasattr(r, "index"),
        "public_members": [attr for attr in dir(r) if not attr.startswith("__")],
    }


def compare_range_vs_list_memory(total_elements: int = 100_000) -> Tuple[int, int]:
    """
    Compares memory footprint between built-in range sequence O(1) and materialized list O(N).

    Args:
        total_elements (int): Total element count.

    Returns:
        Tuple[int, int]: Bytes consumed by range object vs materialized list.
    """
    r_seq = range(0, total_elements, 1)
    l_seq = list(r_seq)

    return sys.getsizeof(r_seq), sys.getsizeof(l_seq)


def get_builtin_version_evolution_matrix() -> Dict[str, str]:
    """
    Returns historical evolution notes for Python built-in functions and range objects.

    Returns:
        Dict[str, str]: Historical version milestone notes.
    """
    return {
        "Python 2.7 (Built-in Legacy)": "xrange() existed for lazy sequence iteration; range() eagerly built lists in RAM; print was a statement; raw_input() was used for text input.",
        "Python 3.0-3.3": "range() replaced xrange() as an immutable O(1) sequence generator; print() became a built-in function; zip(), map(), and filter() returned lazy iterators.",
        "Python 3.8": "Added position-only parameter syntax (/) in built-in function signatures; math.prod() added.",
        "Python 3.10": "zip(strict=True) introduced to enforce equal length iteration; match/case pattern matching on built-in types.",
        "Python 3.11": "Specialized CPython bytecode instructions for built-in functions (abs, len, min, max) yielding 10-60% speedups.",
        "Python 3.13": "GIL-free CPython (PEP 703) enables true multi-core parallel execution of built-in function operations.",
    }


if __name__ == "__main__":
    r_obj = generate_builtin_step_sequence(0, 1000, 50)
    info = inspect_range_attributes(r_obj)

    print("Built-in range Introspection Matrix:")
    print(f"  start={info['start']}, stop={info['stop']}, step={info['step']}")
    print(f"  Public members: {info['public_members']}")

    r_bytes, l_bytes = compare_range_vs_list_memory(100_000)
    print(f"\nMemory Footprint (100,000 elements): range={r_bytes} bytes [O(1)], list={l_bytes} bytes [O(N)]")

    print("\n--- Built-in Function Version Evolution Matrix ---")
    for ver, note in get_builtin_version_evolution_matrix().items():
        print(f"  {ver}: {note}")
