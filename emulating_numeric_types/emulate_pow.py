"""
Python Data Model: Emulating Exponentiation (`__pow__`, `__rpow__`, `__ipow__`)

This module demonstrates overloading the exponentiation operator `**` and the
three-argument built-in `pow(base, exp, mod)`.

Magic Methods:
- `__pow__(self, other, modulo=None)`: Implements `self ** other` or `pow(self, exp, mod)`.
- `__rpow__(self, other)`: Implements `other ** self` (reflected power).
- `__ipow__(self, other)`: Implements `self **= other` (in-place power).
"""
from typing import Union, Optional


class PowerBase:
    """Custom numeric type supporting power and modular exponentiation."""

    def __init__(self, value: int) -> None:
        self.value = int(value)

    def __pow__(self, exp: Union["PowerBase", int], modulo: Optional[int] = None) -> "PowerBase":
        """Handles `self ** exp` and ternary `pow(self, exp, modulo)`."""
        exponent = exp.value if isinstance(exp, PowerBase) else exp
        if modulo is not None:
            return PowerBase(pow(self.value, exponent, modulo))
        return PowerBase(self.value ** exponent)

    def __rpow__(self, base: int) -> "PowerBase":
        """Handles `base ** self`."""
        if isinstance(base, int):
            return PowerBase(base ** self.value)
        return NotImplemented

    def __ipow__(self, exp: Union["PowerBase", int]) -> "PowerBase":
        """Handles `self **= exp` in-place."""
        exponent = exp.value if isinstance(exp, PowerBase) else exp
        self.value = self.value ** exponent
        return self

    def __repr__(self) -> str:
        return f"PowerBase({self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PowerBase):
            return False
        return self.value == other.value


def main() -> None:
    """Demonstrates exponentiation (**) operator overloading."""
    b = PowerBase(3)

    # 1. Forward Exponentiation
    result = b ** 4
    print(f"Forward Exponentiation ({b} ** 4): {result}")

    # 2. Ternary Modular Exponentiation
    mod_pow = pow(b, 4, 10)
    print(f"Modular Exponentiation (pow({b}, 4, 10)): {mod_pow}")

    # 3. Reflected Exponentiation
    ref_pow = 2 ** b
    print(f"Reflected Exponentiation (2 ** {b}): {ref_pow}")

    # 4. In-place Exponentiation
    b **= 3
    print(f"In-place Exponentiation (b **= 3): {b}")


if __name__ == "__main__":
    main()
