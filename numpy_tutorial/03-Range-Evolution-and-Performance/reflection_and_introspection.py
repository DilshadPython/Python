"""
Runtime Introspection and Reflection Matrix Module for range and ndarray.

This module demonstrates:
- Reflection and attribute extraction using dir(range) and dir(np.ndarray).
- Accessing lazy range attributes (.start, .stop, .step) and methods (.count(), .index()).
- Inspecting and calling ndarray methods (.ndim, .shape, .dtype, .sum(), .mean(), .std(), .max(), .min(), .flatten(), .tolist()).
"""

# Import numpy for array introspection and vector aggregation methods
import numpy as np


def introspect_range_attributes() -> dict[str, object]:
    """Inspect and demonstrate all public attributes and methods of Python range.

    Returns:
        dict[str, object]: Dictionary of attributes, methods, and results.
    """
    r = range(10, 100, 5)

    # Filter public attributes (non-dunder)
    public_attrs = [attr for attr in dir(r) if not attr.startswith("__")]

    return {
        "public_attributes": public_attrs,
        "start": r.start,
        "stop": r.stop,
        "step": r.step,
        "count_of_25": r.count(25),
        "index_of_30": r.index(30),
    }


def introspect_ndarray_attributes(arr: np.ndarray) -> dict[str, object]:
    """Inspect public attributes, statistics, and transformation methods of ndarray.

    Args:
        arr (np.ndarray): Target NumPy array.

    Returns:
        dict[str, object]: Dictionary containing metadata, statistics, and exported data.
    """
    # Key non-dunder attributes
    public_attrs = [attr for attr in dir(arr) if not attr.startswith("__")][:15]

    return {
        "sample_public_attributes": public_attrs,
        "ndim": arr.ndim,
        "shape": arr.shape,
        "dtype": str(arr.dtype),
        "size": arr.size,
        "nbytes": arr.nbytes,
        "sum": float(arr.sum()),
        "mean": float(arr.mean()),
        "std": float(arr.std()),
        "max": float(arr.max()),
        "min": float(arr.min()),
        "flattened_list": arr.flatten().tolist(),
    }


if __name__ == "__main__":
    range_info = introspect_range_attributes()
    print("--- Reflection: dir(range) Public Attributes ---")
    print(range_info["public_attributes"])
    print(f"Start: {range_info['start']}, Stop: {range_info['stop']}, Step: {range_info['step']}")
    print(f"r.count(25): {range_info['count_of_25']}, r.index(30): {range_info['index_of_30']}")

    sample_mat = np.array([[10, 20, 30], [40, 50, 60]])
    ndarray_info = introspect_ndarray_attributes(sample_mat)

    print("\n--- Reflection: dir(np.ndarray) Introspection ---")
    print("Shape:", ndarray_info["shape"], "| Dtype:", ndarray_info["dtype"])
    print(f"Sum: {ndarray_info['sum']} | Mean: {ndarray_info['mean']} | Std: {ndarray_info['std']:.2f}")
    print(f"Max: {ndarray_info['max']} | Min: {ndarray_info['min']}")
    print("Exported List:", ndarray_info["flattened_list"])
