# Technical Documentation: Python Fractions (`fractions.Fraction`)

## 📊 Fraction Type Coercion & Arithmetic Rules

| Operation | Operand 1 | Operand 2 | Return Type | Explanation |
| :--- | :--- | :--- | :--- | :--- |
| `Fraction + int` | `Fraction` | `int` | `Fraction` | Integer coerced to `Fraction(int, 1)`; returns exact fraction. |
| `Fraction + float` | `Fraction` | `float` | `float` | Fraction converted to binary float; float precision rules apply. |
| `Fraction + Decimal` | `Fraction` | `Decimal` | `TypeError` | Direct arithmetic between `Fraction` and `Decimal` raises `TypeError`. Must convert explicitly. |
| `Fraction / Fraction` | `Fraction` | `Fraction` | `Fraction` | True division produces reduced exact fraction `(a.num * b.den) / (a.den * b.num)`. |
| `Fraction // Fraction`| `Fraction` | `Fraction` | `int` | Floor division rounds quotient down to integer. |

---

## 🛠️ Internal Dunder Hooks & Operator Overloading Matrix

Fraction instances implement standard CPython numeric protocol hooks:

- `__add__(self, other)`: Addition operator `+`.
- `__sub__(self, other)`: Subtraction operator `-`.
- `__mul__(self, other)`: Multiplication operator `*`.
- `__truediv__(self, other)`: True division operator `/`.
- `__floordiv__(self, other)`: Floor division operator `//`.
- `__mod__(self, other)`: Modulo operator `%`.
- `__divmod__(self, other)`: Built-in `divmod(a, b)`.
- `__pow__(self, other)`: Exponentiation operator `**`.
- `__eq__(self, other)`, `__lt__(self, other)`: Relational operators.
- `__floor__(self)`, `__ceil__(self)`, `__trunc__(self)`: Integration with `math` module.

---

## ⚡ Performance & Memory Notes (`range` vs `List[Fraction]`)

- **Range Sequence Footprint**: `range` stores 3 C integer fields (`start`, `stop`, `step`), maintaining a constant **48 bytes** footprint in RAM ($O(1)$ space).
- **List[Fraction] Footprint**: Creating a list of 1,000 Fraction objects consumes pointer array overhead plus ~48–56 bytes per `Fraction` instance (~8,000+ bytes total, $O(N)$ space).
- **Containment Lookups**: `x in range(...)` runs in $O(1)$ time via arithmetic modulus check.
