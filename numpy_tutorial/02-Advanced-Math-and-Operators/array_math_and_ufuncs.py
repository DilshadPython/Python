"""
NumPy Array Math, Universal Functions (ufuncs), and Matrix Multiplication Module.

This module demonstrates:
- Unary universal functions (np.sqrt, np.exp).
- Binary universal functions (np.add, np.maximum, np.minimum).
- Matrix transposition (.T attribute).
- Matrix dot product (np.dot) and matrix multiplication operator (@).
"""

# Import numpy for vector math and linear algebra operations
import numpy as np


def apply_unary_ufuncs(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Compute square root and exponential of array elements.

    Args:
        arr (np.ndarray): Input numeric array.

    Returns:
        tuple[np.ndarray, np.ndarray]: Square roots and exponential values.
    """
    sqrt_res: np.ndarray = np.sqrt(arr)
    exp_res: np.ndarray = np.exp(arr)
    return sqrt_res, exp_res


def apply_binary_ufuncs(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Perform element-wise binary addition, maximum, and minimum calculations.

    Args:
        x (np.ndarray): First input array.
        y (np.ndarray): Second input array.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Sum, maximums, minimums.
    """
    sum_res: np.ndarray = np.add(x, y)
    max_res: np.ndarray = np.maximum(x, y)
    min_res: np.ndarray = np.minimum(x, y)
    return sum_res, max_res, min_res


def compute_matrix_transposition_and_dot(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Perform matrix transposition, dot product, and matrix multiplication (@).

    Args:
        matrix (np.ndarray): 2D matrix of shape (M, N).

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Transposed matrix, np.dot product, matrix @ product.
    """
    transposed: np.ndarray = matrix.T
    dot_product: np.ndarray = np.dot(transposed, matrix)
    matmul_operator: np.ndarray = transposed @ matrix
    return transposed, dot_product, matmul_operator


if __name__ == "__main__":
    nums = np.arange(1, 10, dtype=np.float64)
    sqrt_vals, exp_vals = apply_unary_ufuncs(nums)

    print("--- Unary Ufuncs ---")
    print("Square Root:", sqrt_vals[:3])
    print("Exponent:   ", exp_vals[:3])

    vec_a = np.array([1.5, 3.2, 5.8])
    vec_b = np.array([2.1, 2.9, 6.0])
    sum_v, max_v, min_v = apply_binary_ufuncs(vec_a, vec_b)
    print("\n--- Binary Ufuncs ---")
    print("Sum:    ", sum_v)
    print("Maximum:", max_v)
    print("Minimum:", min_v)

    mat = np.arange(12).reshape((3, 4))
    trans, dot_prod, mat_mul = compute_matrix_transposition_and_dot(mat)
    print("\n--- Matrix Transposition (3,4) -> (4,3) ---")
    print(trans)
    print("--- Dot Product (4,3) @ (3,4) -> (4,4) ---")
    print(dot_prod)
    print("--- Matrix @ Equality Check ---", np.array_equal(dot_prod, mat_mul))
