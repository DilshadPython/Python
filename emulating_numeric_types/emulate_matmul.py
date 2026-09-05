"""
Python Data Model: Emulating Matrix Multiplication (`__matmul__`, `__rmatmul__`, `__imatmul__`)

Introduced in PEP 465 (Python 3.5+), the `@` operator allows custom types to
implement dedicated matrix multiplication semantics distinct from standard `*`.

Magic Methods:
- `__matmul__(self, other)`: Implements `self @ other`.
- `__rmatmul__(self, other)`: Implements `other @ self` (reflected matrix multiplication).
- `__imatmul__(self, other)`: Implements `self @= other` (in-place matrix multiplication).
"""


class Matrix2x2:
    """A 2x2 matrix class supporting matrix multiplication via `@`."""

    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        # Layout: [[a, b], [c, d]]
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    def __matmul__(self, other: "Matrix2x2") -> "Matrix2x2":
        """Handles `self @ other` for 2x2 matrices."""
        if not isinstance(other, Matrix2x2):
            return NotImplemented

        # Standard matrix dot product for 2x2 matrices
        new_a = self.a * other.a + self.b * other.c
        new_b = self.a * other.b + self.b * other.d
        new_c = self.c * other.a + self.d * other.c
        new_d = self.c * other.b + self.d * other.d
        return Matrix2x2(new_a, new_b, new_c, new_d)

    def __rmatmul__(self, other: "Matrix2x2") -> "Matrix2x2":
        """Handles `other @ self`."""
        if isinstance(other, Matrix2x2):
            return other.__matmul__(self)
        return NotImplemented

    def __imatmul__(self, other: "Matrix2x2") -> "Matrix2x2":
        """Handles `self @= other` in-place."""
        result = self.__matmul__(other)
        if result is NotImplemented:
            return NotImplemented
        self.a, self.b, self.c, self.d = result.a, result.b, result.c, result.d
        return self

    def __repr__(self) -> str:
        return f"Matrix2x2([{self.a}, {self.b}], [{self.c}, {self.d}])"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix2x2):
            return False
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)


def main() -> None:
    """Demonstrates matrix multiplication (@) operator overloading."""
    m1 = Matrix2x2(1, 2, 3, 4)
    m2 = Matrix2x2(2, 0, 1, 2)

    # 1. Forward Matrix Multiplication
    result = m1 @ m2
    print(f"Matrix Multiplication ({m1} @ {m2}):")
    print(f"  Result: {result}")

    # 2. In-place Matrix Multiplication
    m1 @= m2
    print(f"In-place Matrix Multiplication (m1 @= m2):")
    print(f"  m1 updated: {m1}")


if __name__ == "__main__":
    main()
