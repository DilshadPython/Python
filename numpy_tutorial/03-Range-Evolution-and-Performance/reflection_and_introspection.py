"""
Runtime Introspection and Reflection Matrix Module for range and ndarray.

This module demonstrates:
- Reflection and attribute extraction using dir(range) and dir(np.ndarray).
- Accessing lazy range attributes (.start, .stop, .step) and methods (.count(), .index()).
- Inspecting and calling running ndarray attributes:
  (.ndim, .shape, .size, .dtype, .itemsize, .nbytes, .T, .real, .imag)
- Inspecting and calling running ndarray methods:
  (.reshape(), .transpose(), .flatten(), .ravel(), .astype(), .copy(),
   .tolist(), .sum(), .mean(), .std(), .var(), .min(), .max(),
   .argmin(), .argmax(), .clip(), .squeeze(), .swapaxes(), .repeat())
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
    public_attrs = [attr for attr in dir(arr) if not attr.startswith("__")]

    # Demonstrate running methods and attributes on copy
    working_arr = arr.copy()
    floated_arr = working_arr.astype(np.float64)
    clipped_arr = working_arr.clip(min=15, max=45)
    repeated_arr = working_arr.repeat(2, axis=0)

    return {
        "public_attributes_count": len(public_attrs),
        "sample_public_attributes": public_attrs[:15],
        "ndim": arr.ndim,
        "shape": arr.shape,
        "dtype": str(arr.dtype),
        "size": arr.size,
        "itemsize": arr.itemsize,
        "nbytes": arr.nbytes,
        "transposed_shape": arr.T.shape,
        "real_part": arr.real.tolist(),
        "imag_part": arr.imag.tolist(),
        "sum": float(arr.sum()),
        "mean": float(arr.mean()),
        "std": float(arr.std()),
        "var": float(arr.var()),
        "max": float(arr.max()),
        "min": float(arr.min()),
        "argmax": int(arr.argmax()),
        "argmin": int(arr.argmin()),
        "flattened_list": arr.flatten().tolist(),
        "raveled_shape": arr.ravel().shape,
        "clipped_sample": clipped_arr.tolist(),
        "repeated_shape": repeated_arr.shape,
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
    print(f"Argmax: {ndarray_info['argmax']} | Argmin: {ndarray_info['argmin']}")
    print("Exported List:", ndarray_info["flattened_list"])
