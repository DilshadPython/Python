# Python Operators & Expressions — Master Architecture & Performance Guide

## 1. Executive Summary & Overview

Python operators are foundational symbols and keywords that perform operations on values, variables, and data structures. Python supports a rich set of operators categorized into **Arithmetic**, **Assignment (including Augmented and Walrus `:=`)**, **Comparison**, **Logical**, **Bitwise**, **Identity**, and **Membership** operators.

Under the hood, Python operators invoke **Special Dunder Methods** (Magic Methods like `__add__`, `__sub__`, `__eq__`, `__contains__`) on object classes, allowing custom classes to overload operator behaviors. Furthermore, Python provides the standard library **`operator` module** (`import operator`) which exposes functional callables matching all syntax operators.

---

## 2. Core Categories of Python Operators

### 2.1 Arithmetic Operators

Arithmetic operators perform mathematical calculations across numeric types (`int`, `float`, `complex`).

| Operator | Name | Example | Behavior & Description |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `a + b` | Calculates sum of two numbers. |
| `-` | Subtraction | `a - b` | Calculates difference between two numbers. |
| `*` | Multiplication | `a * b` | Calculates product of two numbers. |
| `/` | Float Division | `a / b` | Computes exact division, **always returning a `float`**. |
| `//` | Floor Division | `a // b` | Divides and truncates fractional decimal remainder. |
| `%` | Modulus | `a % b` | Returns the remainder of division. |
| `**` | Exponentiation | `a ** b` | Raises `a` to the power of `b`. |

```python
# Arithmetic Calculations Example
add_res = 10 + 3      # 13
div_res = 10 / 3      # 3.3333333333333335
floor_res = 10 // 3   # 3
mod_res = 10 % 3      # 1
pow_res = 10 ** 3     # 1000
```

---

### 2.2 Assignment & Augmented Assignment Operators

Assignment operators assign values to variables and perform in-place mutation operations.

| Operator | Expression | Equivalent Statement | Behavior |
| :--- | :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` | Direct variable assignment. |
| `+=` | `x += 3` | `x = x + 3` | In-place addition. |
| `-=` | `x -= 2` | `x = x - 2` | In-place subtraction. |
| `*=` | `x *= 4` | `x = x * 4` | In-place multiplication. |
| `/=` | `x /= 2` | `x = x / 2` | In-place float division. |
| `//=` | `x //= 2` | `x = x // 2` | In-place floor division. |
| `%=` | `x %= 3` | `x = x % 3` | In-place modulo. |
| `**=` | `x **= 2` | `x = x ** 2` | In-place exponentiation. |
| `:=` | `(x := expr)` | Assignment Expression | **Walrus Operator** (Assigns inline within expressions). |

---

### 2.3 Comparison / Relational Operators

Comparison operators evaluate relational conditions between operands and return boolean values (`True` or `False`).

| Operator | Description | Example | Result (`x=10, y=5`) |
| :--- | :--- | :--- | :--- |
| `==` | Equal to | `x == y` | `False` |
| `!=` | Not equal to | `x != y` | `True` |
| `<` | Less than | `x < y` | `False` |
| `>` | Greater than | `x > y` | `True` |
| `<=` | Less than or equal to | `x <= y` | `False` |
| `>=` | Greater than or equal to | `x >= y` | `True` |

---

### 2.4 Logical & Short-Circuit Operators

Logical operators evaluate boolean conditions using short-circuiting logic.

- **`and`**: Returns `True` if BOTH conditions evaluate to `True`. Short-circuits if first condition is `False`.
- **`or`**: Returns `True` if EITHER condition evaluates to `True`. Short-circuits if first condition is `True`.
- **`not`**: Reverses the boolean truth value of an expression.

---

### 2.5 Bitwise Operators

Bitwise operators perform binary bit-level operations on integer representations.

| Operator | Name | Expression (`a=12 (1100), b=5 (0101)`) | Result |
| :--- | :--- | :--- | :--- |
| `&` | Bitwise AND | `a & b` | `4` (`0100`) |
| `\|` | Bitwise OR | `a \| b` | `13` (`1101`) |
| `^` | Bitwise XOR | `a ^ b` | `9` (`1001`) |
| `~` | Bitwise NOT | `~a` | `-13` (`-(a + 1)`) |
| `<<` | Bitwise Left Shift | `a << 2` | `48` (`110000`) |
| `>>` | Bitwise Right Shift | `a >> 1` | `6` (`0110`) |

---

## 3. The Walrus Operator (`:=`) — Syntax & Usage

Introduced in **Python 3.8 (PEP 572)**, the Walrus operator (`:=`) enables **assignment expressions**, allowing variables to be assigned within an expression context.

```python
# With Walrus Operator (:=)
if (n := len(fetch_input())) > 10:
    print(f"Data length: {n}")
```

---

## 4. Operator Special Dunder Methods & Custom Operator Overloading

When Python evaluates an operator expression like `a + b`, CPython translates it into an object method call `type(a).__add__(a, b)`. Custom classes can overload these dunder methods to define domain-specific operator behavior.

```python
class CustomVector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other: "CustomVector2D") -> "CustomVector2D":
        """Overloads the addition operator (+)"""
        return CustomVector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> "CustomVector2D":
        """Overloads the scalar multiplication operator (*)"""
        return CustomVector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        """Overloads equality comparison (==)"""
        return isinstance(other, CustomVector2D) and self.x == other.x and self.y == other.y

v1 = CustomVector2D(3, 4)
v2 = CustomVector2D(1, 2)

print(v1 + v2)  # CustomVector2D(x=4.0, y=6.0)
print(v1 * 3)   # CustomVector2D(x=9.0, y=12.0)
```

---

## 5. Standard Library `operator` Module (`import operator`)

The standard library `operator` module provides efficient, C-implemented functional callables corresponding to Python syntax operators:

```python
import operator

# Functional operator invocations
add_res = operator.add(10, 5)       # Same as 10 + 5
sub_res = operator.sub(10, 5)       # Same as 10 - 5
mul_res = operator.mul(10, 5)       # Same as 10 * 5
eq_res = operator.eq(10, 5)         # Same as 10 == 5
contains_res = operator.contains([1, 2, 3], 2)  # Same as 2 in [1, 2, 3]

# High-Performance Item & Attribute Getters for Sorting
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 95},
]

# Fast sorting using operator.itemgetter
sorted_students = sorted(students, key=operator.itemgetter("score"), reverse=True)
print(sorted_students[0]["name"])  # Charlie
```

---

## 6. Range Operator Integration & Reflection Matrix

### 6.1 $O(1)$ Constant-Time Containment Testing

Checking membership with `x in range(start, stop, step)` executes in **$O(1)$ constant time** using modular arithmetic:

$$\text{Contains}(x) = (x \ge \text{start}) \land (x < \text{stop}) \land ((x - \text{start}) \pmod{\text{step}} == 0)$$

```python
import sys
r = range(0, 10_000_000, 5)
print(sys.getsizeof(r))  # 48 bytes (Constant RAM)
print(5_000_000 in r)    # True (Instant O(1) evaluation)
```

### 6.2 Introspection Matrix via `dir(range)`

Using `dir(range)` exposes all attributes and sequence methods available on `range` objects:

```python
r = range(1, 10)
public_methods = [attr for attr in dir(r) if not attr.startswith("__")]
print(public_methods)  # ['count', 'index', 'start', 'step', 'stop']
```

---

## 7. CPython Version Evolution (Python 2.7 to 3.13)

| Version | Feature / Behavior | Technical Impact |
| :--- | :--- | :--- |
| **Python 2.7** | Classic Integer Division (`10 / 3 == 3`) | `/` truncated fractional digits on integers. Required `xrange()` for lazy evaluation. |
| **Python 3.0** | True Division (`10 / 3 == 3.333...`) | Introduced `//` for floor division. Replaced `xrange` with immutable `range` object. |
| **Python 3.8** | Walrus Operator (`:=`) | Introduced assignment expressions (PEP 572). |
| **Python 3.13** | Bytecode Specialization (`BINARY_OP`) | CPython adaptive interpreter optimizes binary operators, achieving **10–15% speedups**. |

---

## 8. Performance Notes & Best Practices

1. **Use `operator.itemgetter` and `operator.attrgetter` for Sorting**: Consistently faster than equivalent `lambda` functions due to C-level execution.
2. **Implement Dunder Methods in Custom Classes**: Implement `__add__`, `__sub__`, `__eq__` for intuitive class design.
3. **Use `//` explicitly for integer math**: Prevents unnecessary float conversions.
4. **Leverage Walrus `:=` in Loops**: Avoids redundant function or length calls in conditional expressions.
