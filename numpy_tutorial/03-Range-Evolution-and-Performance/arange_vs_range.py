"""
NumPy np.arange() vs Python range() Comparison Module.

This module demonstrates:
- Parameter signatures of range([start,] stop[, step]) vs np.arange([start,] stop[, step,], dtype=None).
- Support for floating-point start/stop/step in np.arange() versus integer-only range().
- Directional stepping (positive step, negative decreasing step).
"""

# Import numpy for array generation functions
import numpy as np


def generate_python_range(start: int, stop: int, step: int = 1) -> range:
    """Generate a standard Python built-in range object.

    Args:
        start (int): Inclusive start integer.
        stop (int): Exclusive stop integer.
        step (int, optional): Step size integer. Defaults to 1.

    Returns:
        range: Built-in Python range sequence.
    """
    return range(start, stop, step)


def generate_numpy_arange(
    start: float, stop: float, step: float = 1.0, dtype: type | None = None
) -> np.ndarray:
    """Generate a NumPy ndarray sequence using np.arange().

    Args:
        start (float): Start value (integer or float).
        stop (float): End value boundary (integer or float).
        step (float, optional): Step delta value (can be float). Defaults to 1.0.
        dtype (type | None, optional): Explicit data type. Defaults to None.

    Returns:
        np.ndarray: Generated NumPy array.
    """
    return np.arange(start, stop, step, dtype=dtype)


def demonstrate_floating_and_negative_steps() -> tuple[np.ndarray, np.ndarray]:
    """Demonstrate np.arange with float steps and negative steps.

    Returns:
        tuple[np.ndarray, np.ndarray]:
            - Float stepped array (e.g. 0.0 to 2.0 by 0.25).
            - Negative stepped decreasing array (e.g. 101 down to 35 by -5).
    """
    float_stepped: np.ndarray = np.arange(0.0, 2.0, 0.25)
    negative_stepped: np.ndarray = np.arange(101, 35, -5)
    return float_stepped, negative_stepped


if __name__ == "__main__":
    py_r = generate_python_range(7, 77, 3)
    np_r = generate_numpy_arange(7, 77, 3)

    print("--- Standard Python range(7, 77, 3) ---")
    print(py_r, "List:", list(py_r)[:5])

    print("\n--- NumPy np.arange(7, 77, 3) ---")
    print(np_r)

    flt_arr, neg_arr = demonstrate_floating_and_negative_steps()
    print("\n--- Floating Point Step (0.0 to 2.0 by 0.25) ---")
    print(flt_arr)

    print("\n--- Negative Decreasing Step (101 down to 35 by -5) ---")
    print(neg_arr)
