# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and RAM memory measurement (sys.getsizeof).
# - import time: Standard library module for execution time benchmarking.
# - from pathlib import Path: Safe file path manipulations for binary and CSV persistence.
# - from typing import Any, Dict, List, Optional, Tuple, Union: PEP 484 type annotations.
# - import numpy as np: High-performance scientific computing and N-dimensional array processing.
# =========================================================================
from pathlib import Path
import sys
import time
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np


# ─── SUBFOLDER 1: 01-FUNDAMENTALS ─────────────────────────────────────────────


def demonstrate_01_fundamentals_creation() -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> array_creation_and_dtypes.py]
    Demonstrates fundamental NumPy array creation routines from standard Python lists,
    tuples, and structural initializer functions (np.ones, np.empty, np.eye).

    Returns:
        Dict[str, Any]: Basic arrays, structural matrices, and data type metadata.
    """
    # 1. Create 1D array from integer list
    number_list: List[int] = [22, 17, 9, 18, 33, 81, 50]
    first_array: np.ndarray = np.array(number_list, dtype=np.int64)

    # 2. Create 2D matrix from list of lists
    second_list: List[int] = [21, 19, 4, 30, 66, 6, 17]
    combined_list: List[List[int]] = [number_list, second_list]
    two_dim_array: np.ndarray = np.array(combined_list, dtype=np.int64)

    # 3. Create 1D array from tuple sequence
    tuple_sequence: Tuple[int, ...] = (17, 9, 76, 1, 2, 3, 4, 17)
    tuple_array: np.ndarray = np.array(tuple_sequence)

    # 4. Structural matrices: ones, empty, and identity matrix
    ones_matrix: np.ndarray = np.ones((10, 10), dtype=np.float64)
    empty_matrix: np.ndarray = np.empty((8, 8), dtype=np.float64)
    identity_matrix: np.ndarray = np.eye(5, dtype=np.float64)

    return {
        "1d_array": first_array,
        "1d_shape": first_array.shape,
        "1d_dtype": str(first_array.dtype),
        "2d_array": two_dim_array,
        "2d_shape": two_dim_array.shape,
        "tuple_array": tuple_array,
        "ones_shape": ones_matrix.shape,
        "empty_shape": empty_matrix.shape,
        "identity_matrix": identity_matrix,
        "identity_trace": float(np.trace(identity_matrix)),
    }


def demonstrate_01_fundamentals_shapes_and_metadata() -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> array_shapes_and_dimensions.py]
    Demonstrates multi-dimensional array creation (3D tensor), metadata introspection
    (.ndim, .shape, .size, .dtype, .itemsize, .nbytes), and reshaping operations.

    Returns:
        Dict[str, Any]: Tensor structures, metadata dictionary, and reshaped matrices.
    """
    # 1. 3D array tensor constructed from nested lists
    data_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    tensor: np.ndarray = np.array(data_3d, dtype=np.int32)

    # 2. Metadata introspection
    metadata: Dict[str, Any] = {
        "ndim": tensor.ndim,
        "shape": tensor.shape,
        "size": tensor.size,
        "dtype": str(tensor.dtype),
        "itemsize": tensor.itemsize,
        "nbytes": tensor.nbytes,
    }

    # 3. Reshaping 1D vector into 2D matrix layout
    flat_vector: np.ndarray = np.arange(24)
    reshaped_matrix: np.ndarray = flat_vector.reshape((4, 6))

    return {
        "tensor_3d": tensor,
        "metadata": metadata,
        "flat_vector": flat_vector,
        "reshaped_matrix": reshaped_matrix,
        "reshaped_shape": reshaped_matrix.shape,
    }


# ─── SUBFOLDER 2: 02-ADVANCED-MATH-AND-OPERATORS ──────────────────────────────


def demonstrate_02_advanced_indexing_and_masking() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> indexing_slicing_and_masking.py]
    Demonstrates 2D matrix slicing (row/col extraction), in-place slice mutation,
    fancy integer indexing, and boolean condition masking.

    Returns:
        Dict[str, Any]: Slices, mutated copies, and boolean mask selections.
    """
    # 1. 2D Row and Column Extraction
    matrix = np.array(
        [
            ["a", "b", "c", "d", "e"],
            ["ab", "cd", "ef", "gh", "ij"],
            ["kl", "mn", "op", "qr", "st"],
        ]
    )
    third_column: np.ndarray = matrix[:, 2]  # ['c', 'ef', 'op']
    first_row: np.ndarray = matrix[0, :]  # ['a', 'b', 'c', 'd', 'e']
    partial_row: np.ndarray = matrix[2, :3]  # ['kl', 'mn', 'op']

    # 2. In-place slice mutation on copied array
    nums: np.ndarray = np.arange(20, 40)
    mutated: np.ndarray = nums.copy()
    mutated[6:11] = 70

    # 3. Fancy Indexing and Boolean Masking
    sample_arr: np.ndarray = np.array([10, 20, 30, 40, 50])
    indices = [0, 2, 4]
    fancy_selected: np.ndarray = sample_arr[indices]

    mean_val: float = float(np.mean(sample_arr))
    masked_selected: np.ndarray = sample_arr[sample_arr > mean_val]

    return {
        "third_column": third_column.tolist(),
        "first_row": first_row.tolist(),
        "partial_row": partial_row.tolist(),
        "original_nums": nums.tolist(),
        "mutated_slice": mutated[6:11].tolist(),
        "fancy_selected": fancy_selected.tolist(),
        "mean_threshold": mean_val,
        "masked_selected": masked_selected.tolist(),
    }


def demonstrate_02_advanced_math_and_ufuncs() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> array_math_and_ufuncs.py]
    Demonstrates unary ufuncs (np.sqrt, np.exp), binary ufuncs (np.add, np.maximum, np.minimum),
    matrix transposition (.T), dot product (np.dot), and matrix multiplication (@).

    Returns:
        Dict[str, Any]: Universal function outputs and matrix algebra results.
    """
    # 1. Unary Ufuncs
    nums = np.array([4.0, 9.0, 16.0], dtype=np.float64)
    sqrt_vals: np.ndarray = np.sqrt(nums)
    exp_vals: np.ndarray = np.exp(nums)

    # 2. Binary Ufuncs
    vec_a = np.array([1.5, 3.2, 5.8])
    vec_b = np.array([2.1, 2.9, 6.0])
    sum_res: np.ndarray = np.add(vec_a, vec_b)
    max_res: np.ndarray = np.maximum(vec_a, vec_b)
    min_res: np.ndarray = np.minimum(vec_a, vec_b)

    # 3. Matrix Transposition, Dot Product & @ Operator
    mat_a = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)
    mat_b = mat_a.T  # (2, 3)
    dot_product: np.ndarray = np.dot(mat_b, mat_a)
    matmul_operator: np.ndarray = mat_b @ mat_a

    return {
        "sqrt_vals": sqrt_vals.tolist(),
        "exp_vals": exp_vals.tolist(),
        "sum_res": sum_res.tolist(),
        "max_res": max_res.tolist(),
        "min_res": min_res.tolist(),
        "mat_a_shape": mat_a.shape,
        "mat_b_transposed_shape": mat_b.shape,
        "dot_product": dot_product.tolist(),
        "matmul_operator": matmul_operator.tolist(),
        "matrices_equal": bool(np.array_equal(dot_product, matmul_operator)),
    }


def demonstrate_02_broadcasting_and_axis_operations() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> broadcasting_and_axes.py]
    Demonstrates NumPy array broadcasting mechanics (adding 1D vector to 2D matrix),
    axis-specific aggregations (axis=0 columns vs axis=1 rows), and array stacking (vstack, hstack).

    Returns:
        Dict[str, Any]: Broadcasted results, axis sum/mean vectors, and stacked matrices.
    """
    # 1. Broadcasting 1D vector to 2D matrix
    matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Shape (3, 3)
    row_vector = np.array([10, 20, 30])  # Shape (3,)
    broadcast_add: np.ndarray = matrix_2d + row_vector  # Adds [10, 20, 30] to each row

    # 2. Axis-specific Reduction Operations
    col_sums: np.ndarray = matrix_2d.sum(axis=0)  # [12, 15, 18] (Column sum)
    row_means: np.ndarray = matrix_2d.mean(axis=1)  # [2.0, 5.0, 8.0] (Row mean)

    # 3. Concatenation and Stacking
    v_stacked: np.ndarray = np.vstack((matrix_2d, row_vector))  # Shape (4, 3)
    col_vector = np.array([[100], [200], [300]])  # Shape (3, 1)
    h_stacked: np.ndarray = np.hstack((matrix_2d, col_vector))  # Shape (3, 4)

    return {
        "matrix_2d": matrix_2d.tolist(),
        "row_vector": row_vector.tolist(),
        "broadcast_add": broadcast_add.tolist(),
        "col_sums_axis_0": col_sums.tolist(),
        "row_means_axis_1": row_means.tolist(),
        "v_stacked_shape": v_stacked.shape,
        "h_stacked_shape": h_stacked.shape,
    }


def demonstrate_02_linear_algebra_and_random_sampling() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> linalg_and_random.py]
    Demonstrates np.linalg subpackage (matrix determinant, inverse, eigenvalues, system solver Ax=b, L2 norm)
    and np.random generator routines.

    Returns:
        Dict[str, Any]: Determinants, inverses, linear equation solution x, and random samples.
    """
    # 1. Linear Algebra (np.linalg)
    A = np.array(
        [[2.0, 1.0], [1.0, 3.0]], dtype=np.float64
    )  # Symmetric positive-definite matrix
    b = np.array([8.0, 13.0], dtype=np.float64)  # Target vector

    det_A: float = float(np.linalg.det(A))
    inv_A: np.ndarray = np.linalg.inv(A)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    x_solution: np.ndarray = np.linalg.solve(A, b)  # Solves Ax = b (x = [2.0, 4.0])
    l2_norm: float = float(np.linalg.norm(b))

    # 2. Reproducible Random Sampling (np.random)
    rng = np.random.default_rng(seed=42)
    uniform_samples: np.ndarray = rng.uniform(0.0, 1.0, size=5)
    normal_samples: np.ndarray = rng.normal(loc=0.0, scale=1.0, size=(2, 3))
    random_integers: np.ndarray = rng.integers(1, 100, size=5)

    return {
        "matrix_A": A.tolist(),
        "determinant": det_A,
        "inverse_A": inv_A.tolist(),
        "eigenvalues": eigenvalues.tolist(),
        "solution_x": x_solution.tolist(),
        "l2_norm_b": l2_norm,
        "uniform_samples_count": len(uniform_samples),
        "normal_samples_shape": normal_samples.shape,
        "random_integers": random_integers.tolist(),
    }


def demonstrate_02_advanced_string_arrays_and_io() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> string_arrays_and_io.py]
    Demonstrates string array operations using np.char routines (upper, replace, equal),
    and binary (.npy) / delimited text (.csv) persistence.

    Returns:
        Dict[str, Any]: String transformations and file persistence verification.
    """
    # 1. String array manipulations
    car_brands = np.array(["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Audi"])
    upper_cars: np.ndarray = np.char.upper(car_brands)
    replaced_cars: np.ndarray = np.char.replace(car_brands, "o", "0")
    is_ford: np.ndarray = np.char.equal(car_brands, "Ford")

    # 2. Binary & Text File I/O
    temp_dir = Path("./temp_numpy_io")
    temp_dir.mkdir(exist_ok=True)
    bin_file = temp_dir / "sample_array.npy"
    txt_file = temp_dir / "sample_matrix.csv"

    sample_arr = np.array([10, 20, 30, 40, 50])
    sample_mat = np.eye(4)

    np.save(bin_file, sample_arr)
    loaded_bin: np.ndarray = np.load(bin_file)

    np.savetxt(txt_file, sample_mat, fmt="%.4f", delimiter=",")
    loaded_txt: np.ndarray = np.loadtxt(txt_file, delimiter=",")

    bin_matched: bool = bool(np.array_equal(sample_arr, loaded_bin))
    txt_matched: bool = bool(np.allclose(sample_mat, loaded_txt))

    # Cleanup temp files
    bin_file.unlink(missing_ok=True)
    txt_file.unlink(missing_ok=True)
    temp_dir.rmdir()

    return {
        "upper_cars": upper_cars.tolist(),
        "replaced_cars": replaced_cars.tolist(),
        "is_ford_flags": is_ford.tolist(),
        "binary_io_matched": bin_matched,
        "text_io_matched": txt_matched,
    }


# ─── SUBFOLDER 3: 03-RANGE-EVOLUTION-AND-PERFORMANCE ──────────────────────────


def demonstrate_03_range_vs_arange() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> arange_vs_range.py]
    Demonstrates parameter signature differences between Python range() and NumPy np.arange(),
    floating-point step sizes, and negative directional stepping.

    Returns:
        Dict[str, Any]: Generated range sequences and np.arange arrays.
    """
    py_rng = range(7, 77, 3)
    np_arr = np.arange(7, 77, 3)

    float_stepped: np.ndarray = np.arange(0.0, 2.0, 0.25)
    negative_stepped: np.ndarray = np.arange(101, 35, -5)

    return {
        "python_range_list": list(py_rng)[:5],
        "numpy_arange_array": np_arr[:5].tolist(),
        "float_stepped": float_stepped.tolist(),
        "negative_stepped": negative_stepped.tolist(),
        "same_integer_sequence": list(py_rng) == list(np_arr),
    }


def demonstrate_03_range_performance_and_evolution() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> range_performance_and_evolution.py]
    Demonstrates memory footprint benchmarks via sys.getsizeof, summation execution time speedups,
    and Python 3.3 to Python 3.13 evolution matrix for NumPy.

    Returns:
        Dict[str, Any]: Memory footprints, performance benchmarks, and evolution matrix.
    """
    element_count = 100_000
    py_range = range(element_count)
    np_array = np.arange(element_count, dtype=np.int64)

    range_bytes: int = sys.getsizeof(py_range)
    numpy_bytes: int = sys.getsizeof(np_array)
    numpy_nbytes: int = int(np_array.nbytes)

    # Performance Benchmark
    start_py = time.perf_counter()
    _ = sum(range(element_count))
    time_py = time.perf_counter() - start_py

    start_np = time.perf_counter()
    _ = np_array.sum()
    time_np = time.perf_counter() - start_np

    speedup: float = time_py / time_np if time_np > 0 else 0.0

    evolution_matrix: Dict[str, str] = {
        "Python 3.3": "O(1) lazy range sequence slicing support (range(100)[::2]); yield from generator delegation.",
        "Python 3.4": "enum module and pathlib integration for safe path-based NumPy binary file saving (.npy).",
        "Python 3.5": "PEP 465 matrix multiplication operator (@) introduced for NumPy ndarray.__matmul__.",
        "Python 3.6": "Formatted string literals (f-strings) for fast matrix logging and inline variable formatting.",
        "Python 3.7": "Dataclasses; CPython opcode optimizations accelerating numeric loop dispatches.",
        "Python 3.8": "Positional-only parameter syntax (/) (PEP 570) and Walrus operator (:=) (PEP 572) for array filtering.",
        "Python 3.9": "Dictionary union operators (| and |=); built-in generic type hints (list[int] instead of typing.List).",
        "Python 3.10": "Structural Pattern Matching (match/case PEP 634) over ndarray shapes and dimensions.",
        "Python 3.11": "CPython Specializing Adaptive Interpreter (PEP 659) accelerates binary operator dispatches by 10-25%.",
        "Python 3.12": "Per-interpreter GIL and detailed traceback error indicators for vector arithmetic.",
        "Python 3.13": "Free-threaded CPython (PEP 703 - GIL removal) and Tier 2 JIT compilation for multi-threaded NumPy operations.",
    }

    return {
        "range_object_bytes": range_bytes,
        "numpy_array_bytes": numpy_bytes,
        "numpy_nbytes_attribute": numpy_nbytes,
        "python_range_sum_seconds": time_py,
        "numpy_array_sum_seconds": time_np,
        "speedup_factor": speedup,
        "evolution_matrix": evolution_matrix,
    }


def demonstrate_03_reflection_and_introspection() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> reflection_and_introspection.py]
    Demonstrates reflection via dir(range) and dir(np.ndarray), and executes key running attributes
    and methods on ndarray objects.

    Returns:
        Dict[str, Any]: Public reflection attributes and ndarray running statistics/methods.
    """
    r = range(10, 100, 5)
    range_public_attrs = [attr for attr in dir(r) if not attr.startswith("_")]

    sample_mat = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.int32)
    ndarray_public_attrs = [
        attr for attr in dir(sample_mat) if not attr.startswith("_")
    ]

    # Execute running attributes & methods
    working_arr = sample_mat.copy()
    floated_arr = working_arr.astype(np.float64)
    clipped_arr = working_arr.clip(15, 45)
    repeated_arr = working_arr.repeat(2, axis=0)

    return {
        "range_public_attributes": range_public_attrs,
        "range_start": r.start,
        "range_stop": r.stop,
        "range_step": r.step,
        "range_count_25": r.count(25),
        "range_index_30": r.index(30),
        "ndarray_public_attributes_count": len(ndarray_public_attrs),
        "sample_public_attributes": ndarray_public_attrs[:15],
        "ndim": sample_mat.ndim,
        "shape": sample_mat.shape,
        "size": sample_mat.size,
        "dtype": str(sample_mat.dtype),
        "itemsize": sample_mat.itemsize,
        "nbytes": sample_mat.nbytes,
        "transposed_shape": sample_mat.T.shape,
        "real_part": sample_mat.real.tolist(),
        "imag_part": sample_mat.imag.tolist(),
        "sum": float(sample_mat.sum()),
        "mean": float(sample_mat.mean()),
        "std": float(sample_mat.std()),
        "var": float(sample_mat.var()),
        "max": float(sample_mat.max()),
        "min": float(sample_mat.min()),
        "argmax": int(sample_mat.argmax()),
        "argmin": int(sample_mat.argmin()),
        "flattened_list": sample_mat.flatten().tolist(),
        "raveled_shape": sample_mat.ravel().shape,
        "clipped_sample": clipped_arr.tolist(),
        "repeated_shape": repeated_arr.shape,
    }


def demonstrate_02_3d_tensors_and_batch_operations() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math -> 3d_tensors_and_batch_ops.py]
    Demonstrates professional 3D Tensor operations for Deep Learning & Scientific ML:
    - 3D Tensor batch representation: (batch_size=4, seq_len=6, d_model=8)
    - Axis permutation (transpose) from Batch-First to Sequence-First layout
    - Batch Matrix Multiplication with Einstein Summation (np.einsum)
    - 3D Spatial Reductions (Mean pooling along token sequence axis)
    - 3D Volumetric Slicing (CLS token embedding extraction)

    Returns:
        Dict[str, Any]: Tensor shapes, transposed views, attention scores, and pooled vectors.
    """
    np.random.seed(42)

    # 1. 3D Tensor: Batch=4 samples, SeqLen=6 tokens, EmbeddingDim=8 features
    batch_size, seq_len, d_model = 4, 6, 8
    tensor_3d = np.random.randn(batch_size, seq_len, d_model).astype(np.float32)

    # 2. Axis Permutation: Convert Batch-First (4, 6, 8) to Sequence-First (6, 4, 8)
    seq_first_tensor = np.transpose(tensor_3d, (1, 0, 2))

    # 3. Batch Matrix Multiplication: Attention Score Matrix via Einstein Summation
    # S = Q * K^T -> (B, S, D) x (B, D, M) = (B, S, M)
    Q = tensor_3d
    K = tensor_3d
    # Scaled dot-product attention scores
    attn_scores_einsum = np.einsum("bsd,bmd->bsm", Q, K) / np.sqrt(d_model)
    attn_scores_matmul = (Q @ K.swapaxes(-1, -2)) / np.sqrt(d_model)

    # 4. Spatial 3D Reduction: Mean-pooling across sequence dimension (axis=1)
    # Extracts sentence-level pooled embedding of shape (batch_size, d_model)
    pooled_embeddings = tensor_3d.mean(axis=1)

    # 5. Volumetric 3D Slicing: Extract first token (CLS token) for all batches
    cls_tokens = tensor_3d[:, 0, :]  # Shape: (4, 8)

    return {
        "tensor_shape": tensor_3d.shape,
        "seq_first_shape": seq_first_tensor.shape,
        "attn_scores_shape": attn_scores_einsum.shape,
        "einsum_equals_matmul": bool(np.allclose(attn_scores_einsum, attn_scores_matmul, atol=1e-5)),
        "pooled_shape": pooled_embeddings.shape,
        "cls_tokens_shape": cls_tokens.shape,
        "batch_mean_norm": round(float(np.linalg.norm(pooled_embeddings)), 4),
    }


def run_all_numpy_module_demos() -> Dict[str, Any]:
    """
    Executes all 3 subfolder NumPy curriculum demonstrations in sequence.
    """
    return {
        "01_fundamentals": {
            "creation": demonstrate_01_fundamentals_creation(),
            "shapes_metadata": demonstrate_01_fundamentals_shapes_and_metadata(),
        },
        "02_advanced_math": {
            "indexing_masking": demonstrate_02_advanced_indexing_and_masking(),
            "math_ufuncs": demonstrate_02_advanced_math_and_ufuncs(),
            "broadcasting_axes": demonstrate_02_broadcasting_and_axis_operations(),
            "linalg_random": demonstrate_02_linear_algebra_and_random_sampling(),
            "string_io": demonstrate_02_advanced_string_arrays_and_io(),
            "3d_tensors": demonstrate_02_3d_tensors_and_batch_operations(),
        },
        "03_range_performance": {
            "arange_vs_range": demonstrate_03_range_vs_arange(),
            "performance_evolution": demonstrate_03_range_performance_and_evolution(),
            "reflection_introspection": demonstrate_03_reflection_and_introspection(),
        },
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(run_all_numpy_module_demos())

