"""
cloud_app/tutorials/operator_basics.py — Python Operators & Expressions Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A production-grade, highly structured tutorial module demonstrating Python operators:
1. Arithmetic Operators (+, -, *, /, //, %, **)
2. Assignment & Augmented Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=, := walrus)
3. Comparison & Logical Operators (==, !=, <, >, <=, >=, and, or, not)
4. Bitwise Operators (&, |, ^, ~, <<, >>)
5. Identity & Membership Operators (is, is not, in, not in)
6. Custom Operator Overloading via Dunder Methods (__add__, __sub__, __mul__, __eq__)
7. Standard Library `operator` Module & Programmatic Reflection Matrix (dir(range))
"""

# Standard library module for inspecting object memory footprint.
import sys

# Standard library module mapping syntax operators to callable functions.
import operator

# Standard typing module symbols for explicit type signatures.
from typing import Any, Dict, List, Tuple, Union

Numeric = Union[int, float]


# ── 1. Custom Vector Class Demonstrating Operator Overloading Dunders ────────

class CustomVector2D:
    """
    Encapsulates a 2D mathematical vector to demonstrate operator overloading.

    Supported Operators:
    - Addition (+): __add__
    - Subtraction (-): __sub__
    - Scalar Multiplication (*): __mul__
    - Equality (==): __eq__
    - Containment (in): __contains__
    """

    def __init__(self, x: Numeric, y: Numeric) -> None:
        if isinstance(x, bool) or isinstance(y, bool) or not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Vector coordinates must be valid integer or float numbers.")
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"CustomVector2D(x={self.x}, y={self.y})"

    def __add__(self, other: Any) -> "CustomVector2D":
        if not isinstance(other, CustomVector2D):
            return NotImplemented
        return CustomVector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Any) -> "CustomVector2D":
        if not isinstance(other, CustomVector2D):
            return NotImplemented
        return CustomVector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Numeric) -> "CustomVector2D":
        if isinstance(scalar, bool) or not isinstance(scalar, (int, float)):
            return NotImplemented
        return CustomVector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CustomVector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __contains__(self, value: Numeric) -> bool:
        return value == self.x or value == self.y

    def __len__(self) -> int:
        return 2


# ── 2. Arithmetic & Precedence Demonstrations ─────────────────────────────────

def calculate_arithmetic_operations(a: Numeric, b: Numeric) -> Dict[str, Numeric]:
    """Perform core arithmetic operations across numeric operands."""
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be valid integers or floats.")
    if b == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")

    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "float_division": a / b,
        "floor_division": a // b,
        "modulus": a % b,
        "exponentiation": a ** b,
    }


# ── 3. Assignment & Walrus Operator Demonstrations ───────────────────────────

def demonstrate_assignment_operators(initial_value: float = 10.0) -> Dict[str, float]:
    """Demonstrate basic, augmented arithmetic assignments, and walrus (:=)."""
    results: Dict[str, float] = {}
    val = float(initial_value)
    results["initial"] = val

    val += 5.0    # Add & assign (15.0)
    results["add_assign"] = val

    val -= 3.0    # Subtract & assign (12.0)
    results["sub_assign"] = val

    val *= 2.0    # Multiply & assign (24.0)
    results["mul_assign"] = val

    val /= 4.0    # Float divide & assign (6.0)
    results["div_assign"] = val

    val //= 2.0   # Floor divide & assign (3.0)
    results["floor_div_assign"] = val

    val %= 2.0    # Modulus & assign (1.0)
    results["mod_assign"] = val

    val **= 3.0   # Exponent & assign (1.0)
    results["pow_assign"] = val

    # Walrus Operator (:=)
    if (walrus_val := val + 99.0) > 50.0:
        results["walrus_assign"] = walrus_val

    return results


# ── 4. Comparison, Logical & Bitwise Operators ───────────────────────────────

def evaluate_comparison_and_logical(x: int, y: int) -> Dict[str, bool]:
    """Evaluate relational comparisons and logical short-circuiting."""
    return {
        "equal": x == y,
        "not_equal": x != y,
        "less_than": x < y,
        "greater_than": x > y,
        "less_equal": x <= y,
        "greater_equal": x >= y,
        "logical_and": (x > 0) and (y > 0),
        "logical_or": (x > 0) or (y > 0),
        "logical_not": not (x == y),
    }


def perform_bitwise_operations(a: int, b: int) -> Dict[str, int]:
    """Perform low-level bitwise operations."""
    return {
        "bitwise_and": a & b,
        "bitwise_or": a | b,
        "bitwise_xor": a ^ b,
        "bitwise_not_a": ~a,
        "left_shift": a << 2,
        "right_shift": a >> 1,
    }


# ── 5. Operator Module & Introspection Reflection Matrix ────────────────────

def inspect_operator_module_and_dunders() -> Dict[str, Any]:
    """Inspect the standard library `operator` module and object dunder methods."""
    a, b = 15, 4

    op_add = operator.add(a, b)
    op_sub = operator.sub(a, b)
    op_mul = operator.mul(a, b)
    op_eq = operator.eq(a, b)
    op_contains = operator.contains([10, 15, 20], a)

    int_dunders = [attr for attr in dir(int) if attr.startswith("__") and "add" in attr or "eq" in attr or "mul" in attr]

    students = [
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 85},
        {"name": "Charlie", "score": 95},
    ]
    sorted_by_score = sorted(students, key=operator.itemgetter("score"), reverse=True)

    return {
        "operator_add": op_add,
        "operator_sub": op_sub,
        "operator_mul": op_mul,
        "operator_eq": op_eq,
        "operator_contains": op_contains,
        "sample_int_dunders": int_dunders,
        "top_student": sorted_by_score[0]["name"],
    }


def inspect_range_operator_features(start: int, stop: int, step: int) -> Dict[str, Any]:
    """Demonstrate range sequence operators (in, indexing) and O(1) RAM."""
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        raise TypeError("Range parameters must be integers.")
    if step == 0:
        raise ValueError("Range step cannot be zero.")

    r = range(start, stop, step)

    return {
        "range_repr": repr(r),
        "start": r.start,
        "stop": r.stop,
        "step": r.step,
        "length": len(r),
        "contains_target": (start + step) in r,
        "first_element": r[0] if len(r) > 0 else None,
        "memory_bytes": sys.getsizeof(r),
    }


def inspect_range_attributes_and_methods() -> Dict[str, Any]:
    """Reflectively inspect all attributes and methods on range using dir()."""
    r = range(1, 10)
    all_attrs = dir(r)

    public_methods = [attr for attr in all_attrs if not attr.startswith("__")]
    dunder_methods = [attr for attr in all_attrs if attr.startswith("__")]

    return {
        "total_attributes_count": len(all_attrs),
        "public_methods": public_methods,
        "sample_dunder_methods": dunder_methods[:5],
        "has_count_method": "count" in public_methods,
        "has_index_method": "index" in public_methods,
        "has_start_attr": "start" in public_methods,
        "has_stop_attr": "stop" in public_methods,
        "has_step_attr": "step" in public_methods,
    }


# ── 6. Master Demonstration Functions ────────────────────────────────────────

def demonstrate_all_operators() -> Dict[str, Any]:
    """Master entrypoint returning summarized demonstration metrics."""
    v1 = CustomVector2D(3, 4)
    v2 = CustomVector2D(1, 2)
    v_sum = v1 + v2
    v_scaled = v1 * 3

    return {
        "arithmetic": calculate_arithmetic_operations(10, 3),
        "assignment": demonstrate_assignment_operators(10.0),
        "comparison_logical": evaluate_comparison_and_logical(10, 5),
        "bitwise": perform_bitwise_operations(12, 5),
        "vector_overloading": {
            "v1": repr(v1),
            "v2": repr(v2),
            "v_sum": repr(v_sum),
            "v_scaled": repr(v_scaled),
            "contains_3": 3.0 in v1,
        },
        "operator_module_reflection": inspect_operator_module_and_dunders(),
        "range_operators": inspect_range_operator_features(0, 100, 5),
        "reflection": inspect_range_attributes_and_methods(),
    }


if __name__ == "__main__":
    import pprint
    print("=== Python Operators Architecture Master Demo ===")
    pprint.pprint(demonstrate_all_operators())
