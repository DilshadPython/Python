# Python Rational Fractions & Numeric Operations Reference Suite

A comprehensive, production-grade Python reference suite demonstrating exact rational arithmetic, conversions, float approximations, rounding, range sequences, and memory introspection using Python's standard library (`fractions.Fraction`, `math`, `decimal`, `range`).

---

## What is New

This directory has been refactored and flattened from nested hyphenated subdirectories (`01-Fundamentals`, `02-Advanced-Math-and-Operators`, `03-Range-Evolution-and-Performance`) into a clean, PEP 8-compliant 5-tier architecture:

1. **`fraction_basics_ops.py`**: Instantiation from integers, strings, floats, and Decimals (`Fraction(numerator, denominator)`), automated GCD reduction, and attribute access (`.numerator`, `.denominator`).
2. **`fraction_conversions_ops.py`**: Rational float approximations (`limit_denominator()`), integer ratio extraction (`as_integer_ratio()`), primitive type conversions (`float`, `int`, `str`), and numerator GCD calculations (`math.gcd()`).
3. **`fraction_arithmetic_ops.py`**: Exact arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), divmod evaluation (`divmod(a, b)`), relational comparisons (`==`, `!=`, `>`, `<`, `>=`, `<=`), and mixed-type arithmetic with integers and floats.
4. **`fraction_advanced_math_ops.py`**: Mathematical rounding (`math.floor`, `math.ceil`, `math.trunc`, `round()`), precision summation over iterables (`sum()`), and bi-directional Decimal interop.
5. **`fraction_range_evolution_ops.py`**: Fractional sequence range generation, `range()` O(1) space memory footprint analysis, `dir(range)` introspection, and Python version evolution timeline (Python 2.7 to 3.13).
6. **`test_fractions.py`**: Master unittest test suite running 21 test cases validating all 5 fraction modules.

---

## Standard Library Modules Used

- **`fractions.Fraction`**: Standard library class for exact rational number arithmetic and representation.
- **`math`**: Mathematical functions (`floor`, `ceil`, `trunc`, `gcd`).
- **`decimal.Decimal`**: High-precision fixed-point decimal arithmetic interop.
- **`sys`**: System-specific memory size inspection (`sys.getsizeof`).

---

## Detailed Attributes & Methods Reference

### 1. `fractions.Fraction` Class Instantiation

#### `Fraction(numerator=0, denominator=1)`
Creates a rational fraction from integer numerator and denominator. Automatically divides both by their Greatest Common Divisor (GCD) to simplify to lowest terms.

```python
from fractions import Fraction

f = Fraction(4, 14)
print(f)  # Output: '2/7'
```

#### `Fraction(other_fraction)` / `Fraction(string)` / `Fraction(float)` / `Fraction(decimal)`
Creates a Fraction instance from a parsed string, binary float, or Decimal object.

```python
from decimal import Decimal

f_str = Fraction(" 3 / 8 ")        # Output: 3/8
f_float = Fraction(0.25)           # Output: 1/4
f_dec = Fraction(Decimal("0.125")) # Output: 1/8
```

---

### 2. `fractions.Fraction` Core Attributes

#### `.numerator`
Returns the integer numerator of the fraction in lowest terms.

#### `.denominator`
Returns the integer denominator of the fraction in lowest terms (always positive).

```python
f = Fraction(-6, 8)  # Simplified to Fraction(-3, 4)
print(f.numerator)    # -3
print(f.denominator)  # 4
```

---

### 3. `fractions.Fraction` Key Methods

#### `limit_denominator(max_denominator=1000000)`
Finds and returns the closest `Fraction` to `self` that has a denominator at most `max_denominator`. Useful for approximating binary floats.

```python
val = 0.3333333333333333
f = Fraction(val).limit_denominator(10)
print(f)  # Output: 1/3
```

#### `as_integer_ratio()`
Returns a 2-tuple pair `(numerator, denominator)` of integers. Standardized across `int`, `float`, and `Fraction` in Python 3.8+.

```python
f = Fraction(3, 4)
print(f.as_integer_ratio())  # Output: (3, 4)
```

---

### 4. Arithmetic & Rounding Operations

#### Arithmetic Operators
Supports exact rational arithmetic returning a reduced `Fraction`:
- `a + b` (Addition)
- `a - b` (Subtraction)
- `a * b` (Multiplication)
- `a / b` (Division)
- `a // b` (Floor Division, returns `int`)
- `a % b` (Modulo, returns `Fraction`)
- `a ** n` (Exponentiation)

#### `divmod(a, b)`
Returns a tuple `(quotient, remainder)` where `quotient = a // b` (`int`) and `remainder = a % b` (`Fraction`).

```python
a = Fraction(7, 3)
b = Fraction(2, 3)
print(divmod(a, b))  # Output: (3, Fraction(1, 3))
```

#### Rounding & Truncation (`math.floor`, `math.ceil`, `math.trunc`, `round`)
- `math.floor(f)`: Returns largest integer `<= f`.
- `math.ceil(f)`: Returns smallest integer `>= f`.
- `math.trunc(f)`: Returns integer truncated towards zero.
- `round(f)`: Rounds fraction to nearest integer.

```python
import math
from fractions import Fraction

f = Fraction(7, 3)
print(math.floor(f)) # 2
print(math.ceil(f))  # 3
print(math.trunc(f)) # 2
```

---

### 5. `range` Introspection & Attributes

#### `range(start, stop, step)` Attributes & Methods
- `.start`: Starting integer bound.
- `.stop`: Ending integer bound (exclusive).
- `.step`: Step increment value.
- `.index(value)`: Returns zero-based index of value.
- `.count(value)`: Returns 1 if value exists in range, 0 otherwise.

```python
r = range(10, 100, 5)
print(r.start, r.stop, r.step) # 10 100 5
print(r.index(25))              # 3
```

---

## File Structure Matrix

| Module | Primary Operations | Description |
| :--- | :--- | :--- |
| `fraction_basics_ops.py` | `Fraction()`, `.numerator`, `.denominator` | Instantiation from int, string, float, Decimal, and component extraction. |
| `fraction_conversions_ops.py` | `limit_denominator()`, `as_integer_ratio()`, `math.gcd` | Float approximations, tuple extraction, numeric casting, and GCD. |
| `fraction_arithmetic_ops.py` | `+`, `-`, `*`, `/`, `//`, `%`, `divmod`, `==` | Exact arithmetic, quotient/remainder, relational comparisons, mixed types. |
| `fraction_advanced_math_ops.py` | `floor`, `ceil`, `trunc`, `round`, `sum()`, `Decimal` | Mathematical rounding, exact list summation, and Decimal interop. |
| `fraction_range_evolution_ops.py` | `generate_fractional_range`, `dir(range)` | Fractional step sequences, memory benchmarking, and Python version history. |
| `test_fractions.py` | `unittest.TestCase` | Master test suite validating all 21 fraction operations. |

---

## Running the Code & Unit Tests

### Run Individual Modules Directly

```bash
python3 fraction_basics_ops.py
python3 fraction_conversions_ops.py
python3 fraction_arithmetic_ops.py
python3 fraction_advanced_math_ops.py
python3 fraction_range_evolution_ops.py
```

### Run Unit Test Suite

```bash
python3 -m unittest test_fractions.py
```

### Run Syntax Verification

```bash
python3 -m py_compile *.py
```
