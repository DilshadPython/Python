# =========================================================================
# SUBFOLDER 01: v33_to_v36_foundations -> version_33_to_36_features.py
# =========================================================================
# Demonstrates key evolution features from Python 3.3 to Python 3.6:
# - Python 3.3: yield from generator delegation, O(1) range slicing, importlib.
# - Python 3.4: enum module, pathlib.Path, statistics module.
# - Python 3.5: PEP 465 matrix multiplication operator (@), async/await, typing.
# - Python 3.6: Formatted string literals (f-strings), numeric underscores, secrets module.
# =========================================================================
from enum import Enum
from pathlib import Path
import secrets
import statistics
from typing import Any, Dict, List, Tuple
import numpy as np


class StatusEnum(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"


def generate_sub_sequence():
    yield "Python 3.3"
    yield "Generator Delegation"


def demonstrate_generator_delegation():
    """Python 3.3: yield from syntax."""
    yield from generate_sub_sequence()
    yield "Completed"


def demonstrate_python33_to_36_features() -> Dict[str, Any]:
    """
    Executes feature demonstrations across Python 3.3, 3.4, 3.5, and 3.6.

    Returns:
        Dict[str, Any]: Structured execution outputs per version step.
    """
    # ── Python 3.3 Features ──
    generator_output: List[str] = list(demonstrate_generator_delegation())
    lazy_range: range = range(100, 1000, 5)[::2]
    lazy_range_slice: List[int] = list(lazy_range[:4])

    # ── Python 3.4 Features ──
    active_status: str = StatusEnum.ACTIVE.value
    sample_path: Path = Path("/tmp/demo_file.txt")
    stat_mean: float = float(statistics.mean([10, 20, 30, 40, 50]))

    # ── Python 3.5 Features ──
    # PEP 465 @ Operator with NumPy ndarray
    mat_a: np.ndarray = np.array([[1, 2], [3, 4]], dtype=np.float64)
    mat_b: np.ndarray = np.array([[5, 6], [7, 8]], dtype=np.float64)
    matmul_result: np.ndarray = mat_a @ mat_b  # [[19, 22], [43, 50]]

    # ── Python 3.6 Features ──
    one_million: int = 1_000_000
    formatted_fstring: str = (
        f"Value: {one_million:,} | Matmul Trace: {float(np.trace(matmul_result))}"
    )
    secure_hex: str = secrets.token_hex(4)

    return {
        "3.3_yield_from": generator_output,
        "3.3_range_slice": lazy_range_slice,
        "3.4_enum_value": active_status,
        "3.4_pathlib_name": sample_path.name,
        "3.4_statistics_mean": stat_mean,
        "3.5_matmul_result": matmul_result.tolist(),
        "3.5_matmul_shape": matmul_result.shape,
        "3.6_numeric_literal": one_million,
        "3.6_fstring": formatted_fstring,
        "3.6_secure_hex_len": len(secure_hex),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(demonstrate_python33_to_36_features())
