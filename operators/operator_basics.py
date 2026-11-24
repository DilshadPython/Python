"""
cloud_app/tutorials/operator_basics.py — Python Operators & Expressions Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A production-grade, highly structured master tutorial module demonstrating all 3 core operator tracks:
1. Title 1: Arithmetic & Assignment Operators (Basic, Complex, In-place Sequence Mutations, Walrus :=)
2. Title 2: Comparison & Logical Operators (Relational, Chained Range Comparisons, Short-Circuit Safety, Bitwise)
3. Title 3: Advanced Operators, Custom Dunders & Range (CustomVector2D, PermissionFlags, operator module, dir(range))
"""

# Standard library module for inspecting object memory footprint.
import sys

# Standard library module mapping syntax operators to callable functions.
import operator

# Standard typing module symbols for explicit type signatures.
from typing import Any, Dict, List, Tuple, Union

Numeric = Union[int, float]


# =============================================================================
# TITLE 1: ARITHMETIC AND ASSIGNMENT OPERATORS
# =============================================================================

def calculate_arithmetic_operations(a: Numeric, b: Numeric) -> Dict[str, Numeric]:
    """Perform core arithmetic operations across numeric operands (+, -, *, /, //, %, **)."""
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


def calculate_complex_arithmetic(c1: complex, c2: complex) -> Dict[str, complex]:
    """Perform complex number arithmetic operations."""
    return {
        "addition": c1 + c2,
        "subtraction": c1 - c2,
        "multiplication": c1 * c2,
        "division": c1 / c2,
    }


def demonstrate_assignment_operators(initial_value: float = 10.0) -> Dict[str, float]:
    """Demonstrate basic, augmented arithmetic assignments (=, +=, -=, *=, /=, //=, %=, **=, := walrus)."""
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


def demonstrate_inplace_sequence_mutations() -> Tuple[List[int], Dict[str, int]]:
    """Demonstrate augmented assignment operators on mutable sequences (lists, dicts)."""
    numbers_list = [1, 2, 3]
    numbers_list += [4, 5]     # In-place list extension
    numbers_list *= 2          # In-place list replication

    counts = {"apples": 5}
    counts["apples"] += 10     # In-place dictionary value mutation

    return numbers_list, counts


# =============================================================================
# TITLE 2: COMPARISON AND LOGICAL OPERATORS
# =============================================================================

def evaluate_comparison_and_logical(x: int, y: int) -> Dict[str, bool]:
    """Evaluate relational comparisons (==, !=, <, >, <=, >=) and logical operations (and, or, not)."""
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


def evaluate_chained_range_comparison(val: float, low: float, high: float) -> bool:
    """Evaluate Pythonic chained relational comparison (low <= val <= high)."""
    return low <= val <= high


def evaluate_short_circuit_safety(numbers: List[int]) -> Tuple[bool, int]:
    """Demonstrate short-circuiting preventing zero division error."""
    safe_ratio_possible = len(numbers) > 0 and numbers[0] != 0
    calculated_value = 100 // numbers[0] if safe_ratio_possible else -1
    return safe_ratio_possible, calculated_value


def perform_bitwise_operations(a: int, b: int) -> Dict[str, int]:
    """Perform low-level bitwise operations (&, |, ^, ~, <<, >>)."""
    return {
        "bitwise_and": a & b,
        "bitwise_or": a | b,
        "bitwise_xor": a ^ b,
        "bitwise_not_a": ~a,
        "left_shift": a << 2,
        "right_shift": a >> 1,
    }


# =============================================================================
# TITLE 3: ADVANCED OPERATORS, CUSTOM DUNDERS AND RANGE
# =============================================================================

class CustomVector2D:
    """Encapsulates a 2D mathematical vector to demonstrate operator overloading dunders."""

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


class PermissionFlags:
    """Demonstrates bitwise operator overloading (__or__, __and__, __contains__) for permission flags."""

    READ = 1 << 2   # 4
    WRITE = 1 << 1  # 2
    EXEC = 1 << 0   # 1

    def __init__(self, mask: int = 0) -> None:
        self.mask: int = mask

    def __or__(self, other: Any) -> "PermissionFlags":
        if isinstance(other, PermissionFlags):
            return PermissionFlags(self.mask | other.mask)
        elif isinstance(other, int):
            return PermissionFlags(self.mask | other)
        return NotImplemented

    def __and__(self, other: Any) -> "PermissionFlags":
        if isinstance(other, PermissionFlags):
            return PermissionFlags(self.mask & other.mask)
        elif isinstance(other, int):
            return PermissionFlags(self.mask & other)
        return NotImplemented

    def __contains__(self, flag: int) -> bool:
        return (self.mask & flag) == flag

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, PermissionFlags) and self.mask == other.mask


def inspect_operator_module_and_dunders() -> Dict[str, Any]:
    """Inspect standard library `operator` module and dunder methods."""
    a, b = 15, 4
    students = [
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 85},
        {"name": "Charlie", "score": 95},
    ]
    sorted_by_score = sorted(students, key=operator.itemgetter("score"), reverse=True)

    return {
        "operator_add": operator.add(a, b),
        "operator_sub": operator.sub(a, b),
        "operator_mul": operator.mul(a, b),
        "operator_eq": operator.eq(a, b),
        "operator_contains": operator.contains([10, 15, 20], a),
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

    return {
        "total_attributes_count": len(all_attrs),
        "public_methods": public_methods,
        "has_count_method": "count" in public_methods,
        "has_index_method": "index" in public_methods,
        "has_start_attr": "start" in public_methods,
        "has_stop_attr": "stop" in public_methods,
        "has_step_attr": "step" in public_methods,
    }


# =============================================================================
# MASTER DEMONSTRATION ENTRYPOINT
# =============================================================================

def demonstrate_all_operators() -> Dict[str, Any]:
    """Master entrypoint demonstrating all 3 operator titles."""
    v1 = CustomVector2D(3, 4)
    v2 = CustomVector2D(1, 2)
    p_read_write = PermissionFlags(PermissionFlags.READ) | PermissionFlags(PermissionFlags.WRITE)

    return {
        "title_1_arithmetic_assignment": {
            "basic_arithmetic": calculate_arithmetic_operations(10, 3),
            "complex_arithmetic": calculate_complex_arithmetic(3 + 4j, 1 - 2j),
            "assignment_walrus": demonstrate_assignment_operators(10.0),
            "inplace_mutations": demonstrate_inplace_sequence_mutations(),
        },
        "title_2_comparison_logical": {
            "comparison_logical": evaluate_comparison_and_logical(10, 5),
            "chained_comparison": evaluate_chained_range_comparison(50, 10, 100),
            "short_circuit_safety": evaluate_short_circuit_safety([20, 10]),
            "bitwise": perform_bitwise_operations(12, 5),
        },
        "title_3_advanced_dunders_range": {
            "vector_overloading": repr(v1 + v2),
            "permission_flags_overloading": PermissionFlags.READ in p_read_write,
            "operator_module_reflection": inspect_operator_module_and_dunders(),
            "range_operators": inspect_range_operator_features(0, 100, 5),
            "range_reflection": inspect_range_attributes_and_methods(),
        },
    }


if __name__ == "__main__":
    import pprint
    print("=== Python Operators Architecture Master Demo (Titles 1, 2 & 3) ===")
    pprint.pprint(demonstrate_all_operators())
