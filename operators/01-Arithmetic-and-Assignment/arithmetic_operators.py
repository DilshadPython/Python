"""
Python Operators: Arithmetic Operators Module.

This module demonstrates all Python arithmetic operators:
- Basic Arithmetic: +, -, *, / (True Division), // (Floor Division), % (Modulo), ** (Exponentiation)
- Matrix Multiplication: @ (Python 3.5+ PEP 465)
- Standard Library Functional Equivalents: operator.add, operator.truediv, operator.floordiv, etc.
"""
# "import module" loads operator standard library module into local namespace.
import operator
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Tuple, Union

Numeric = Union[int, float]


def basic_arithmetic_operations(a: Numeric, b: Numeric) -> Tuple[float, float, float, float, int, float, float]:
    """
    Perform fundamental arithmetic operations between two numeric values.

    Args:
        a (Numeric): Left operand.
        b (Numeric): Right operand.

    Returns:
        Tuple: Results of (sum, difference, product, true_division, floor_division, modulo, power).
    """
    if b == 0:
        raise ValueError("Division or modulo by zero is undefined.")

    addition: float = float(a + b)
    subtraction: float = float(a - b)
    multiplication: float = float(a * b)
    true_division: float = a / b       # Always returns float in Python 3+
    floor_division: int = int(a // b)   # Rounds down to nearest integer
    modulo_val: float = float(a % b)     # Remainder of division
    power_val: float = float(a ** b)     # Exponentiation

    return addition, subtraction, multiplication, true_division, floor_division, modulo_val, power_val


def operator_module_equivalents(a: Numeric, b: Numeric) -> Tuple[float, float, int]:
    """
    Demonstrate functional arithmetic operations using standard library operator module.

    Args:
        a (Numeric): Left operand.
        b (Numeric): Right operand.

    Returns:
        Tuple: Results of (operator.add, operator.mul, operator.floordiv).
    """
    return operator.add(a, b), operator.mul(a, b), operator.floordiv(a, b)


class Matrix2D:
    """
    Class demonstrating custom matrix multiplication (@ operator via __matmul__ hook introduced in Python 3.5).
    """

    def __init__(self, data: List[List[Numeric]]) -> None:
        """Initialize 2D matrix data."""
        self.data: List[List[Numeric]] = data

    def __matmul__(self, other: "Matrix2D") -> "Matrix2D":
        """Overload @ matrix multiplication operator."""
        if not isinstance(other, Matrix2D):
            return NotImplemented

        rows_a = len(self.data)
        cols_a = len(self.data[0])
        rows_b = len(other.data)
        cols_b = len(other.data[0])

        if cols_a != rows_b:
            raise ValueError(f"Cannot multiply matrix of shape ({rows_a}, {cols_a}) with ({rows_b}, {cols_b})")

        result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix2D(result)

    def __eq__(self, other: object) -> bool:
        """Check matrix equality."""
        if not isinstance(other, Matrix2D):
            return False
        return self.data == other.data
