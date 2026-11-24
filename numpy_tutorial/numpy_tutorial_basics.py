"""
Master Executable Guide for NumPy Core Tutorial.

This standalone script combines and executes all core NumPy features across the 3-step curriculum:
1. Array Creation & Shapes (1D, 2D, 3D, dtype, eye, ones, empty)
2. Advanced Slicing, Ufuncs, Transposition & Matrix Multiplication (@)
3. Range vs arange Comparison, Performance Benchmarks & Reflection (dir(range) / dir(np.ndarray))
"""

# Import sys for system memory reflection
import sys

# Import numpy for high-performance array operations
import numpy as np


def run_fundamentals_demo() -> None:
    """Run Step 1: Fundamentals Demonstration."""
    print("=" * 60)
    print(" STEP 1: NUMPY FUNDAMENTALS & ARRAY CREATION")
    print("=" * 60)

    # 1D & 2D Arrays
    arr_1d = np.array([10, 20, 30, 40, 50], dtype=np.int64)
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
    identity = np.eye(4)

    print(f"1D Vector: {arr_1d} | Shape: {arr_1d.shape} | Dtype: {arr_1d.dtype}")
    print(f"2D Matrix:\n{arr_2d}")
    print(f"4x4 Identity Matrix:\n{identity}\n")


def run_advanced_operations_demo() -> None:
    """Run Step 2: Advanced Math & Matrix Operations Demonstration."""
    print("=" * 60)
    print(" STEP 2: ADVANCED MATH, UFUNCS & MATRIX OPERATIONS")
    print("=" * 60)

    # Matrix transposition & @ operator
    mat_a = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)
    mat_b = mat_a.T                             # (2, 3)
    mat_prod = mat_b @ mat_a                    # (2, 2)

    print(f"Original Matrix A (3,2):\n{mat_a}")
    print(f"Transposed Matrix B (2,3):\n{mat_b}")
    print(f"Matrix Product (B @ A) (2,2):\n{mat_prod}")

    # Universal Functions (ufuncs)
    x = np.array([0.0, np.pi / 2, np.pi])
    print(f"Sin Ufunc: {np.sin(x).round(4)}")
    print(f"Sqrt Ufunc: {np.sqrt(np.array([4, 16, 25]))}\n")


def run_range_performance_demo() -> None:
    """Run Step 3: Range Evolution, Introspection & Reflection Demonstration."""
    print("=" * 60)
    print(" STEP 3: RANGE EVOLUTION & RUNTIME INTROSPECTION")
    print("=" * 60)

    # Range vs arange
    py_rng = range(0, 100_000, 5)
    np_arr = np.arange(0, 100_000, 5, dtype=np.int64)

    print(f"Python range RAM footprint: {sys.getsizeof(py_rng)} bytes (O(1) Lazy Object)")
    print(f"NumPy arange RAM footprint: {sys.getsizeof(np_arr):,} bytes (O(N) Contiguous Memory)")

    # Reflection: dir(range) and dir(ndarray)
    print("\nPublic range attributes:", [a for a in dir(py_rng) if not a.startswith("__")])
    print(f"range start={py_rng.start}, stop={py_rng.stop}, step={py_rng.step}")
    print(f"np.ndarray shape={np_arr.shape}, ndim={np_arr.ndim}, size={np_arr.size:,}")
    print("=" * 60)


if __name__ == "__main__":
    run_fundamentals_demo()
    run_advanced_operations_demo()
    run_range_performance_demo()
