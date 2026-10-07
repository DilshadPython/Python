# =========================================================================
# SUBFOLDER 02: v37_to_v310_modern_features -> version_37_to_310_features.py
# =========================================================================
# Demonstrates key evolution features from Python 3.7 to Python 3.10:
# - Python 3.7: @dataclass decorator, guaranteed dict insertion order, time.time_ns().
# - Python 3.8: Positional-only parameters (/), Walrus operator (:=), math.prod().
# - Python 3.9: Dict union operators (| and |=), str.removeprefix(), str.removesuffix().
# - Python 3.10: Structural Pattern Matching (match/case), strict parameter in zip().
# =========================================================================
from dataclasses import dataclass
import math
from typing import Any, Dict, List, Tuple
import numpy as np


@dataclass
class MatrixMetadata:
    name: str
    shape: Tuple[int, ...]
    dtype: str
    is_square: bool


def divide_numbers(numerator: float, denominator: float, /) -> float:
    """Python 3.8: Positional-only parameters syntax (/)."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return numerator / denominator


def evaluate_tensor_shape(arr: np.ndarray) -> str:
    """Python 3.10: Structural Pattern Matching (match / case) over ndarray shapes."""
    match arr.shape:
        case (n,) if n > 0:
            return f"1D Vector with {n} elements"
        case (r, c) if r == c:
            return f"Square 2D Matrix ({r}x{c})"
        case (r, c):
            return f"Rectangular 2D Matrix ({r}x{c})"
        case (d, r, c):
            return f"3D Tensor ({d}x{r}x{c})"
        case _:
            return f"Higher-Dimensional Array (ndim={arr.ndim})"


def demonstrate_python37_to_310_features() -> Dict[str, Any]:
    """
    Executes feature demonstrations across Python 3.7, 3.8, 3.9, and 3.10.

    Returns:
        Dict[str, Any]: Structured execution outputs per version step.
    """
    # ── Python 3.7 Features ──
    sample_mat = np.eye(3, dtype=np.float64)
    meta = MatrixMetadata(
        name="Identity",
        shape=sample_mat.shape,
        dtype=str(sample_mat.dtype),
        is_square=True,
    )

    ordered_dict = {"first": 1, "second": 2, "third": 3}
    dict_keys_order = list(ordered_dict.keys())

    # ── Python 3.8 Features ──
    pos_only_result: float = divide_numbers(100.0, 4.0)
    numbers_list = [2, 3, 4, 5]
    prod_result: int = math.prod(numbers_list)

    # Walrus Operator (:=) inline condition assignment
    sample_arr = np.array([10, 25, 40, 55, 70])
    if (mean_val := float(sample_arr.mean())) > 30:
        filtered_arr = sample_arr[sample_arr > mean_val]

    # ── Python 3.9 Features ──
    dict_a = {"a": 1, "b": 2}
    dict_b = {"b": 20, "c": 30}
    merged_dict = dict_a | dict_b  # {'a': 1, 'b': 20, 'c': 30}

    raw_string = "Prefix_NumPy_Array_Suffix"
    stripped_prefix = raw_string.removeprefix("Prefix_").removesuffix("_Suffix")

    # ── Python 3.10 Features ──
    shape_pattern_1d = evaluate_tensor_shape(np.array([1, 2, 3]))
    shape_pattern_square = evaluate_tensor_shape(sample_mat)
    shape_pattern_rect = evaluate_tensor_shape(np.zeros((2, 5)))

    # strict parameter in zip()
    zipped_pairs = list(zip([1, 2, 3], ["a", "b", "c"], strict=True))

    return {
        "3.7_dataclass_name": meta.name,
        "3.7_dataclass_is_square": meta.is_square,
        "3.7_dict_keys": dict_keys_order,
        "3.8_pos_only_result": pos_only_result,
        "3.8_math_prod": prod_result,
        "3.8_walrus_mean": mean_val,
        "3.8_walrus_filtered": filtered_arr.tolist(),
        "3.9_dict_union": merged_dict,
        "3.9_string_removeprefix": stripped_prefix,
        "3.10_pattern_1d": shape_pattern_1d,
        "3.10_pattern_square": shape_pattern_square,
        "3.10_pattern_rect": shape_pattern_rect,
        "3.10_zip_strict": zipped_pairs,
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(demonstrate_python37_to_310_features())
