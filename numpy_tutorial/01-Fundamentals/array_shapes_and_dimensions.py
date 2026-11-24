"""
NumPy Array Shapes and Dimensions Module.

This module demonstrates:
- Multi-dimensional array structures (1D vectors, 2D matrices, 3D tensors).
- Introspection attributes: .ndim, .shape, .size, .dtype, .itemsize.
- Reshaping matrices and arrays using np.reshape().
"""

# Import numpy for numerical array manipulation
import numpy as np


def create_3d_tensor() -> np.ndarray:
    """Create and return a 3D NumPy array (tensor).

    Returns:
        np.ndarray: A 3D array with shape (2, 2, 3).
    """
    # 3D array constructed from nested list structure
    data_3d = [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]]
    ]
    tensor: np.ndarray = np.array(data_3d, dtype=np.int32)
    return tensor


def inspect_array_metadata(arr: np.ndarray) -> dict[str, object]:
    """Inspect and extract array metadata attributes.

    Args:
        arr (np.ndarray): Target NumPy array.

    Returns:
        dict[str, object]: Dictionary containing metadata (ndim, shape, size, dtype, itemsize).
    """
    return {
        "ndim": arr.ndim,
        "shape": arr.shape,
        "size": arr.size,
        "dtype": str(arr.dtype),
        "itemsize": arr.itemsize,
        "nbytes": arr.nbytes
    }


def reshape_array(arr: np.ndarray, new_shape: tuple[int, ...]) -> np.ndarray:
    """Reshape an array into a new target dimensional layout.

    Args:
        arr (np.ndarray): Original array.
        new_shape (tuple[int, ...]): Target shape.

    Returns:
        np.ndarray: Reshaped NumPy array view or copy.
    """
    return arr.reshape(new_shape)


if __name__ == "__main__":
    tensor = create_3d_tensor()
    metadata = inspect_array_metadata(tensor)

    print("--- 3D Tensor ---")
    print(tensor)
    print("\n--- Tensor Introspection Metadata ---")
    for key, value in metadata.items():
        print(f"{key:10s}: {value}")

    flat_vector = np.arange(24)
    reshaped_matrix = reshape_array(flat_vector, (4, 6))
    print("\n--- Reshaped Matrix (4, 6) ---")
    print(reshaped_matrix)
