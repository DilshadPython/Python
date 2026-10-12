"""
Python Data Model: Emulating Subtraction (`__sub__`, `__rsub__`, `__isub__`)

This module demonstrates overloading the subtraction operator `-` for a custom
`Currency` class.

Magic Methods:
- `__sub__(self, other)`: Implements `self - other`.
- `__rsub__(self, other)`: Implements `other - self` (reflected subtraction).
- `__isub__(self, other)`: Implements `self -= other` (in-place subtraction).
"""
from typing import Union


class Currency:
    """Represents a monetary amount in a single currency."""

    def __init__(self, amount: float, symbol: str = "$") -> None:
        self.amount = float(amount)
        self.symbol = symbol

    def __sub__(self, other: Union["Currency", float, int]) -> "Currency":
        """Handles `self - other`."""
        if isinstance(other, Currency):
            if self.symbol != other.symbol:
                raise ValueError(f"Cannot subtract different currencies ({self.symbol} vs {other.symbol})")
            return Currency(self.amount - other.amount, self.symbol)
        if isinstance(other, (int, float)):
            return Currency(self.amount - float(other), self.symbol)
        return NotImplemented

    def __rsub__(self, other: Union[float, int]) -> "Currency":
        """Handles `other - self` when `other` is a numeric scalar."""
        if isinstance(other, (int, float)):
            return Currency(float(other) - self.amount, self.symbol)
        return NotImplemented

    def __isub__(self, other: Union["Currency", float, int]) -> "Currency":
        """Handles `self -= other` in-place."""
        if isinstance(other, Currency):
            if self.symbol != other.symbol:
                raise ValueError("Currency mismatch during in-place subtraction")
            self.amount -= other.amount
            return self
        if isinstance(other, (int, float)):
            self.amount -= float(other)
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"{self.symbol}{self.amount:.2f}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Currency):
            return False
        return self.amount == other.amount and self.symbol == other.symbol


def main() -> None:
    """Demonstrates currency subtraction operator overloading."""
    c1 = Currency(100.0)
    c2 = Currency(35.50)

    # 1. Forward Subtraction
    diff = c1 - c2
    print(f"Forward Subtraction ({c1} - {c2}): {diff}")

    # 2. Reflected Subtraction
    ref_diff = 200.0 - c2
    print(f"Reflected Subtraction (200.0 - {c2}): {ref_diff}")

    # 3. In-place Subtraction
    c1 -= c2
    print(f"In-place Subtraction (c1 -= c2): {c1}")


if __name__ == "__main__":
    main()
