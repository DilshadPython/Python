# 🔢 Python Data Model: Emulating Numeric Types (`emulating_numeric_types`) Pedagogical Module

Welcome to the **`emulating_numeric_types` Pedagogical Module**. This module provides a complete reference guide and executable codebase for mastering Section 3.3.8 of the Python Data Model: **Emulating Numeric Types**.

By implementing special double-underscore ("dunder") methods, custom Python objects can seamlessly overload standard arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`), matrix multiplication (`@`), bitwise operators (`&`, `|`, `^`, `<<`, `>>`), and unary operators (`-x`, `+x`, `abs()`, `~x`).

---

## 📂 Module Architecture

```
emulating_numeric_types/
├── emulate_add.py                  # Addition (+): __add__, __radd__, __iadd__
├── emulate_sub.py                  # Subtraction (-): __sub__, __rsub__, __isub__
├── emulate_mul.py                  # Multiplication (*): __mul__, __rmul__, __imul__
├── emulate_matmul.py               # Matrix Multiplication (@): __matmul__, __rmatmul__, __imatmul__
├── emulate_truediv.py              # True Division (/): __truediv__, __rtruediv__, __itruediv__
├── emulate_floordiv.py             # Floor Division (//): __floordiv__, __rfloordiv__, __ifloordiv__
├── emulate_mod.py                  # Modulo (%): __mod__, __rmod__, __imod__
├── emulate_divmod.py               # Divmod: __divmod__, __rdivmod__
├── emulate_pow.py                  # Power (**): __pow__, __rpow__, __ipow__
├── emulate_bitwise_and.py          # Bitwise AND (&): __and__, __rand__, __iand__
├── emulate_bitwise_or.py           # Bitwise OR (|): __or__, __ror__, __ior__
├── emulate_bitwise_xor.py          # Bitwise XOR (^): __xor__, __rxor__, __ixor__
├── emulate_shift.py                # Bitwise Shifts (<<, >>): __lshift__, __rshift__, __ilshift__, __irshift__
├── emulate_unary.py                # Unary Operators (-x, +x, abs, ~): __neg__, __pos__, __abs__, __invert__
├── test_emulating_numeric_types.py # Unittest suite testing all 14 numeric emulation scripts
├── requirements.txt                # Dependency specification (Standard library footprint)
└── README.md                       # Module documentation and usage guide
```

---

## 🌟 What is New in This Module Update

1. **Structured `emulate_<operator>.py` Naming**: Replaced empty/stub legacy files (`and.py`, `divmod.py`, `floordiv.py`, etc.) with descriptive filenames matching the target mathematical operations.
2. **Complete 3-Tier Dunder Operator Matrix**: Every arithmetic operation is demonstrated across forward evaluation (`__op__`), reflected evaluation (`__rop__`), and in-place mutation (`__iop__`).
3. **PEP 465 `@` Matrix Operator**: Added dedicated demonstration of Python 3.5+ matrix multiplication using `__matmul__`, `__rmatmul__`, and `__imatmul__`.
4. **PEP 8 Compliance & Type Hints**: Modernized code with standard Pythonic conventions, complete type hints (`Union`, `Tuple`, `Optional`), docstrings, and `if __name__ == "__main__":` entry points.
5. **Comprehensive Unittest Suite**: Introduced `test_emulating_numeric_types.py` covering all dunder methods using Python's `unittest` framework.

---

## 🔍 Numeric Dunder Methods & Attributes Reference

Below is a complete reference of the magic dunder methods implemented across this module.

| Category | Operator / Function | Forward Dunder | Reflected Dunder | In-place Dunder | Module Script |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Addition** | `a + b` | `__add__(self, b)` | `__radd__(self, a)` | `__iadd__(self, b)` | [emulate_add.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_add.py) |
| **Subtraction** | `a - b` | `__sub__(self, b)` | `__rsub__(self, a)` | `__isub__(self, b)` | [emulate_sub.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_sub.py) |
| **Multiplication** | `a * b` | `__mul__(self, b)` | `__rmul__(self, a)` | `__imul__(self, b)` | [emulate_mul.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_mul.py) |
| **Matrix Multiply** | `a @ b` | `__matmul__(self, b)` | `__rmatmul__(self, a)` | `__imatmul__(self, b)` | [emulate_matmul.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_matmul.py) |
| **True Division** | `a / b` | `__truediv__(self, b)` | `__rtruediv__(self, a)` | `__itruediv__(self, b)` | [emulate_truediv.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_truediv.py) |
| **Floor Division** | `a // b` | `__floordiv__(self, b)` | `__rfloordiv__(self, a)` | `__ifloordiv__(self, b)` | [emulate_floordiv.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_floordiv.py) |
| **Modulo** | `a % b` | `__mod__(self, b)` | `__rmod__(self, a)` | `__imod__(self, b)` | [emulate_mod.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_mod.py) |
| **Divmod** | `divmod(a, b)` | `__divmod__(self, b)` | `__rdivmod__(self, a)` | N/A | [emulate_divmod.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_divmod.py) |
| **Exponentiation** | `a ** b` | `__pow__(self, b)` | `__rpow__(self, a)` | `__ipow__(self, b)` | [emulate_pow.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_pow.py) |
| **Bitwise AND** | `a & b` | `__and__(self, b)` | `__rand__(self, a)` | `__iand__(self, b)` | [emulate_bitwise_and.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_bitwise_and.py) |
| **Bitwise OR** | `a \| b` | `__or__(self, b)` | `__ror__(self, a)` | `__ior__(self, b)` | [emulate_bitwise_or.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_bitwise_or.py) |
| **Bitwise XOR** | `a ^ b` | `__xor__(self, b)` | `__rxor__(self, a)` | `__ixor__(self, b)` | [emulate_bitwise_xor.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_bitwise_xor.py) |
| **Bitwise Shift** | `a << b`, `a >> b` | `__lshift__`, `__rshift__` | `__rlshift__`, `__rrshift__` | `__ilshift__`, `__irshift__` | [emulate_shift.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_shift.py) |
| **Unary Ops** | `-a`, `+a`, `abs()`, `~` | `__neg__`, `__pos__`, `__abs__`, `__invert__` | N/A | N/A | [emulate_unary.py](file:///home/monika/PycharmProjects/Devel/Python/emulating_numeric_types/emulate_unary.py) |

---

## 💻 Code Examples by Feature

### 1. Vector Addition (`emulate_add.py`)

```python
from emulating_numeric_types.emulate_add import Vector2D

v1 = Vector2D(3.0, 4.0)
v2 = Vector2D(1.0, 2.0)

# Forward addition
print(v1 + v2)      # Vector2D(x=4.0, y=6.0)

# Reflected addition with scalar
print(10.0 + v1)    # Vector2D(x=13.0, y=14.0)

# In-place addition
v1 += v2
print(v1)           # Vector2D(x=4.0, y=6.0)
```

---

### 2. Matrix Multiplication `@` (`emulate_matmul.py`)

```python
from emulating_numeric_types.emulate_matmul import Matrix2x2

m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(2, 0, 1, 2)

# Matrix dot product using @ operator
result = m1 @ m2
print(result)       # Matrix2x2([4.0, 4.0], [10.0, 8.0])
```

---

### 3. Bitwise & Shift Operations (`emulate_shift.py`)

```python
from emulating_numeric_types.emulate_shift import BitRegister

reg = BitRegister(0b0001)

# Left and Right Shift
left = reg << 3     # BitRegister(bin=0b1000, dec=8)
right = left >> 2   # BitRegister(bin=0b10, dec=2)
```

---

## 🚀 Execution & Testing Guide

### 1. Run Individual Scripts

Execute any numeric emulation script directly:

```bash
python3 emulating_numeric_types/emulate_add.py
python3 emulating_numeric_types/emulate_matmul.py
python3 emulating_numeric_types/emulate_shift.py
python3 emulating_numeric_types/emulate_unary.py
```

### 2. Run the Unittest Suite

Execute the complete test suite:

```bash
python3 -m unittest emulating_numeric_types/test_emulating_numeric_types.py
```

Or using `pytest`:

```bash
pytest emulating_numeric_types/test_emulating_numeric_types.py
```
