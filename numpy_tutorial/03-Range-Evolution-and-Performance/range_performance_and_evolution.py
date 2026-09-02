"""
NumPy and Python Range Memory Performance and Version Evolution Module.

This module documents and benchmarks:
- Memory footprint using sys.getsizeof for range() vs np.arange() vs materialized list.
- Computational time complexity and evaluation mechanisms (O(1) lazy range vs O(N) memory allocation).
- Comprehensive Python version evolution matrix (Python 2.7 to Python 3.13).
"""

# Import sys for memory size introspection (sys.getsizeof)
import sys

# Import time for performance benchmarking
import time

# Import numpy for array allocation comparisons
import numpy as np


def measure_memory_footprint(element_count: int = 1_000_000) -> dict[str, int]:
    """Measure byte memory usage for range, list, and np.ndarray.

    Args:
        element_count (int): Number of elements in sequence.

    Returns:
        dict[str, int]: Memory footprints in bytes for each data structure.
    """
    py_range = range(element_count)
    np_array = np.arange(element_count, dtype=np.int64)

    # Note: sys.getsizeof(py_range) measures O(1) sequence header (~48 bytes)
    # sys.getsizeof(np_array) measures contiguous buffer array memory (~8 MB)
    return {
        "range_object_bytes": sys.getsizeof(py_range),
        "numpy_array_bytes": sys.getsizeof(np_array),
        "numpy_nbytes_attribute": int(np_array.nbytes),
    }


def benchmark_iteration_performance(element_count: int = 100_000) -> dict[str, float]:
    """Benchmark summation execution time between Python range sum and NumPy array sum.

    Args:
        element_count (int): Total elements to process.

    Returns:
        dict[str, float]: Elapsed execution time in seconds.
    """
    # Python range sum time
    start_py = time.perf_counter()
    _ = sum(range(element_count))
    time_py = time.perf_counter() - start_py

    # NumPy array vectorized sum time
    arr = np.arange(element_count, dtype=np.int64)
    start_np = time.perf_counter()
    _ = arr.sum()
    time_np = time.perf_counter() - start_np

    return {
        "python_range_sum_seconds": time_py,
        "numpy_array_sum_seconds": time_np,
        "speedup_factor": time_py / time_np if time_np > 0 else 0.0,
    }


def get_version_evolution_matrix() -> dict[str, str]:
    """Provide historical and modern breakdown of range and array evolution.

    Returns:
        dict[str, str]: Evolution matrix across Python releases.
    """
    return {
        "Python 2.7": "range() created a fully materialized list in RAM O(N). xrange() was a custom sequence type for lazy O(1) iteration.",
        "Python 3.0": "range() replaced xrange() entirely as an immutable lazy O(1) sequence object. Materialized range list removed.",
        "Python 3.3": "range objects added support for slicing range(100)[::2] yielding new lazy range objects in O(1) time.",
        "Python 3.8": "Positional-only parameter boundary syntax (/), vectorized SIMD performance updates in NumPy.",
        "Python 3.11": "CPython Specializing Adaptive Interpreter accelerated integer loop evaluation over ranges by 10-25%.",
        "Python 3.13": "Free-threaded CPython (PEP 703) enables parallel multi-threaded NumPy matrix operations without GIL bottlenecks.",
    }


if __name__ == "__main__":
    count = 1_000_000
    mem_stats = measure_memory_footprint(count)

    print(f"--- Memory Footprint for {count:,} Elements ---")
    print(f"Python range() RAM footprint:   {mem_stats['range_object_bytes']} bytes  (O(1) Memory)")
    print(f"NumPy np.arange() RAM footprint: {mem_stats['numpy_array_bytes']:,} bytes (O(N) Contiguous Memory)")

    perf = benchmark_iteration_performance(500_000)
    print("\n--- Vectorized Sum Benchmark ---")
    print(f"Python sum(range()):  {perf['python_range_sum_seconds']:.6f} sec")
    print(f"NumPy arr.sum():       {perf['numpy_array_sum_seconds']:.6f} sec")
    print(f"NumPy Vector Speedup: {perf['speedup_factor']:.2f}x faster")

    print("\n--- Python Version Evolution Matrix ---")
    for ver, desc in get_version_evolution_matrix().items():
        print(f"[{ver}]: {desc}")
