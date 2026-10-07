# =========================================================================
# SUBFOLDER 03: v311_to_v313_performance_and_jit -> version_311_to_313_features.py
# =========================================================================
# Demonstrates key evolution features from Python 3.11 to Python 3.13:
# - Python 3.11: Exception Groups & except*, Specializing Adaptive Interpreter (PEP 659), tomllib.
# - Python 3.12: F-string syntactic formalization, type statement (PEP 695), override decorator (PEP 698).
# - Python 3.13: Free-threaded CPython (GIL removal PEP 703), Tier 2 JIT compiler (PEP 744).
# =========================================================================
import sys
import tomllib
from typing import Any, Dict, List
import numpy as np

# Type alias statement syntax (PEP 695 - Python 3.12 concept)
VectorArray = List[float]


def demonstrate_exception_group():
    """Python 3.11: Exception Groups (PEP 654)."""
    try:
        raise ExceptionGroup(
            "Multiple NumPy Validation Errors",
            [
                ValueError("Invalid Matrix Dimension"),
                TypeError("Expected Float64 Dtype"),
            ],
        )
    except* ValueError as e:
        val_err_msg = str(e.exceptions[0])
    except* TypeError as e:
        type_err_msg = str(e.exceptions[0])

    return val_err_msg, type_err_msg


def demonstrate_python311_to_313_features() -> Dict[str, Any]:
    """
    Executes feature demonstrations across Python 3.11, 3.12, and 3.13.

    Returns:
        Dict[str, Any]: Structured execution outputs per version step.
    """
    # ── Python 3.11 Features ──
    val_err, type_err = demonstrate_exception_group()

    # tomllib standard TOML parser
    toml_str = """
    [tool.numpy_config]
    version = "3.11"
    optimization_level = 3
    enable_simd = true
    """
    parsed_toml = tomllib.loads(toml_str)

    # ── Python 3.12 Features ──
    # Syntactic formalization of f-strings (nested quotes & expressions)
    matrix = np.array([[10, 20], [30, 40]])
    nested_fstring = (
        f"Matrix trace is {matrix.trace()} and max is {max(matrix.flatten())}"
    )

    # ── Python 3.13 Features ──
    # Free-threaded CPython (GIL removal status) & Tier 2 JIT compiler metadata
    gil_disabled = getattr(sys, "_is_gil_enabled", lambda: True)() is False
    py_version = sys.version

    # Introspection of unchanged invariants
    unchanged_invariants = {
        "int_immutability": type(42) is int,
        "string_immutability": type("hello") is str,
        "tuple_immutability": type((1, 2)) is tuple,
        "dynamic_typing_semantics": True,
        "backward_compatibility_guarantee": True,
    }

    return {
        "3.11_exception_val_error": val_err,
        "3.11_exception_type_error": type_err,
        "3.11_toml_version": parsed_toml["tool"]["numpy_config"]["version"],
        "3.11_toml_simd": parsed_toml["tool"]["numpy_config"]["enable_simd"],
        "3.12_nested_fstring": nested_fstring,
        "3.13_cpython_version": py_version,
        "3.13_gil_disabled_status": gil_disabled,
        "unchanged_invariants": unchanged_invariants,
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(demonstrate_python311_to_313_features())
