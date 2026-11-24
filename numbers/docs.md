# Python Numbers & Arithmetic Evolution Guide (Python 3.3 – 3.13 & Python 2.7 Comparison)

> [!NOTE]
> **Module Scope**: This document provides an exhaustive breakdown of all 14 files in the `2.Numbers` directory. All scripts have been modernized to be **100% compatible with Python 3.3 through Python 3.13** while incorporating compatibility shims and side-by-side comparative code for **Python 2.7**.

---

## 🌟 Executive Summary & Notification Dashboard

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   PYTHON NUMBERS WORKSPACE STATUS                        │
├──────────────────┬──────────────────────────┬────────────────────────────┤
│ Target Standards │ Python 3.3 – Python 3.13│ Full Modern Compatibility  │
├──────────────────┼──────────────────────────┼────────────────────────────┤
│ Legacy Reference │ Python 2.7               │ Side-by-Side Comparison    │
├──────────────────┼──────────────────────────┼────────────────────────────┤
│ Total Files      │ 14 Scripts + Test Suite  │ Fully Refactored & Tested  │
├──────────────────┼──────────────────────────┼────────────────────────────┤
│ Unit Test Suite  │ test_numbers.py          │ 14/14 Modules Passing      │
└──────────────────┴──────────────────────────┴────────────────────────────┘
```

> [!TIP]
> **Key Refactoring Highlights**:
> 1. **Pure Modular Functions**: Extracted standalone, testable functions from all CLI and loop scripts.
> 2. **Default Parameter Bug Fix**: Removed executable `input()` calls inside function default arguments in `calculator.py`.
> 3. **Range & Type Safety**: Wrapped `math.floor()` with `int()` in prime checking algorithms to eliminate float parameter type errors in legacy environments.
> 4. **String Formatting**: Replaced unescaped f-strings with `str.format()` where universal version support was required, while documenting f-string evolution from 3.6 to 3.13.
> 5. **Input Shim**: Implemented cross-version `get_input` handling `raw_input` (Python 2.7) and `input()` (Python 3.3+).

---

## 📚 Table of Contents
1. [Python Version Compatibility Matrix](#-python-version-compatibility-matrix)
2. [Detailed File Refactoring & Diffs](#-detailed-file-refactoring--diffs)
3. [Python 2.7 vs Python 3.3–3.13 Comparative Analysis](#-python-27-vs-python-33313-comparative-analysis)
4. [Dual-Level Educational Explanations](#-dual-level-educational-explanations)
   - [Beginner Level (New to Python)](#beginner-level-new-to-python)
   - [Advanced & Senior Level (Deep Dive)](#advanced--senior-level-deep-dive)
5. [Unit Test Suite & Verification](#-unit-test-suite--verification)

---

## 📊 Python Version Compatibility Matrix

| Feature / Behavior | Python 2.7 | Python 3.3 – 3.5 | Python 3.6 – 3.12 | Python 3.13 | Refactored Standard |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`print` Syntax** | Statement (`print x`) | Function (`print(x)`) | Function (`print(x)`) | Function (REPL colors) | `from __future__ import print_function` |
| **Division `/`** | Floor Truncation (`5/2 == 2`) | True Division (`5/2 == 2.5`) | True Division (`5/2 == 2.5`) | True Division (`5/2 == 2.5`) | `from __future__ import division` |
| **Integer Types** | `int` (32/64-bit) + `long` | Unified `int` (Arbitrary) | Unified `int` (Arbitrary) | Unified `int` (Arbitrary) | Modern `int` |
| **Input Function** | `raw_input()` string, `input()` eval | `input()` string | `input()` string | `input()` string | `get_input` shim |
| **`math.floor()` Return** | Returns `float` (`2.0`) | Returns `int` (`2`) | Returns `int` (`2`) | Returns `int` (`2`) | `int(math.floor(...))` |
| **`round()` Algorithm** | Half-Away-From-Zero (`2.5 -> 3`) | Banker's Rounding (`2.5 -> 2`) | Banker's Rounding (`2.5 -> 2`) | Banker's Rounding (`2.5 -> 2`) | `round()` + explicit format |
| **String Formatting** | `%` / `.format()` | `.format()` | F-strings `f"{x}"` | PEP 701 f-strings | Universal `.format()` |
| **`random.sample()`** | Sampled from `list` | Sampled from `range` | Sampled from `range` | Sampled from `range` | `list(range(...))` safe |

---

## 🛠 Detailed File Refactoring & Diffs

Here is the exact transformation applied to each of the 14 files in `2.Numbers/`:

### 1. `bin_hex_oct_num.py`
- **What Changed**: Extracted base conversion logic into `convert_number_bases(x)` and `to_complex(y)`.
- **Why**: Allows unit testing without executing loops on import.
```diff
- numbers = 100
- for x in range(numbers):
- 	print('Binary of ', x, ' = ', bin(x), \
- 		 'Hexadecamal of ', x, ' = ', hex(x), \
- 		 'Octal of ', x, ' = ', oct(x))
+ from __future__ import print_function
+ def convert_number_bases(x):
+     return {"number": x, "binary": bin(x), "hexadecimal": hex(x), "octal": oct(x)}
```

---

### 2. `calculator.py`
- **What Changed**: Fixed critical bug where `input()` ran during module import inside default parameters. Extracted pure `calculate(num1, op, num2)` function.
- **Why**: Eliminates import side-effects and enables complete unit test automation.
```diff
- def main(num1=int(input("Enter num1: ")), op=input('Enter op: '), num2=int(input("Enter num2: "))):
+ def calculate(num1, op, num2):
+     if op == '+': return num1 + num2
+     elif op == '/':
+         if num2 == 0: raise ZeroDivisionError("Cannot divide by zero.")
+         return num1 / num2
```

---

### 3. `complex_num.py`
- **What Changed**: Added `get_complex_details(val)` to return structured dictionary (`value`, `type`, `real`, `imag`).
- **Why**: Standardized complex number inspection.
```diff
- a = 4+8+3j
- print(a)
- print(type(a))
+ def get_complex_details(val):
+     return {"value": val, "type": type(val), "real": val.real, "imag": val.imag}
```

---

### 4. `deciamel.py`
- **What Changed**: Added `decimal_operations(num1, num2)` and cross-version `get_input` compatibility.
- **Why**: Ensures interactive CLI input does not block headless test execution.
```diff
- num1 = int(input('Enter num1 as decimal: '))
+ try: get_input = raw_input
+ except NameError: get_input = input
+ def decimal_operations(num1, num2): ...
```

---

### 5. `example.py`
- **What Changed**: Wrapped base parsing in `parse_base_string(val_str, base)` function.
- **Why**: Encapsulates positional radix integer conversions (Base 2, Base 3, Base 4).
```diff
- x = int('10000', 3)
+ def parse_base_string(val_str, base):
+     return int(val_str, base)
```

---

### 6. `f_num.py`
- **What Changed**: Replaced unescaped f-strings (SyntaxError in Py2.7–3.5) with `str.format()` and extracted `add_constant_to_list()`.
- **Why**: Grants universal execution compatibility across Python 2.7 to 3.13.
```diff
- print(f'{num}', ' + ',  f'{addnum} = ')
+ print("{0} + {1} = {2}".format(num, addnum, new_val))
```

---

### 7. `floats.py`
- **What Changed**: Created `float_operations()` and `inspect_special_floats()` for checking `nan`, `inf`, `-inf`, and scientific notation (`3e8`).
- **Why**: Provides testable API for float arithmetic and special floating-point constants.
```diff
- d = float('nan')
+ def inspect_special_floats():
+     return {"nan": float('nan'), "inf": float('inf'), "scientific_3e8": 3e8}
```

---

### 8. `inte.py`
- **What Changed**: Refactored into `integer_operations(num1, num2)` and documented Python 3 integer arbitrary precision.
- **Why**: Clean separation of calculation logic and CLI input.
```diff
- num1 = int(input('Enter num1: '))
+ def integer_operations(num1, num2):
+     return {"sum": num1 + num2, "division": num1 / num2, "floor_division": num1 // num2}
```

---

### 9. `is_prime_v.py`
- **What Changed**: Updated `is_prime_v(num)` to return `False` for `num <= 1` and created `benchmark_prime_v()`.
- **Why**: Corrected edge case where non-positive numbers and 1 were misclassified.
```diff
  def is_prime_v(num):
-     if num == 1:
-         return False
+     if num <= 1:
+         return False
```

---

### 10. `is_prime_v2.py`
- **What Changed**: Wrapped `math.floor()` in `int()`: `int(math.floor(math.sqrt(num)))`.
- **Why**: Crucial fix! In Python 2.7 `math.floor()` returned a float, which caused `range(2, float)` to throw a `TypeError`.
```diff
- max_divisor = math.floor(math.sqrt(num))
+ max_divisor = int(math.floor(math.sqrt(num)))
```

---

### 11. `is_prime_v3.py`
- **What Changed**: Applied `int(math.floor(...))` cast and structured `is_prime_v3(num)` to test even numbers first, then odd divisors.
- **Why**: Optimized $O(\sqrt{N}/2)$ performance while maintaining cross-version range safety.
```diff
- max_divisor = math.floor(math.sqrt(num))
+ max_divisor = int(math.floor(math.sqrt(num)))
```

---

### 12. `nearst_number.py`
- **What Changed**: Created `format_and_round(num1, num2)` using `str.format()` (`"{:,}".format(val)`).
- **Why**: Fixed f-string compatibility and documented Banker's Rounding vs Round-Half-Away.
```diff
- print(f"{cal:,}")
+ res["rounded_sum_formatted"] = "{:,}".format(rounded_sum)
```

---

### 13. `none_bool.py`
- **What Changed**: Built `evaluate_truthiness(value)` function and fixed typo `print('o os ', o)` -> `'o is '`.
- **Why**: Standardized truthiness testing for 15 distinct Python data types.
```diff
- print('o os ', o)
+ print("{0} is {1}".format(var_name, evaluate_truthiness(val)))
```

---

### 14. `random_num.py`
- **What Changed**: Extracted `get_random_single()` and `get_random_sample()`, converting ranges to `list(range(...))` for universal safety.
- **Why**: Guarantees compatibility across Py2.7 list ranges and Py3 range objects.
```diff
- for x in random.sample(range(1, 12), 4):
+ sample_range = list(range(start, stop))
+ return random.sample(sample_range, count)
```

---

## 🔄 Python 2.7 vs Python 3.3–3.13 Comparative Analysis

To illustrate language evolution, here are side-by-side examples comparing legacy **Python 2.7** syntax against **Python 3.3 – 3.13**:

### 1. Integer Division (PEP 238)
```python
# --- PYTHON 2.7 ---
# Default integer division truncates decimal values
result = 5 / 2  # Returns 2 (int)

# --- PYTHON 3.3 - 3.13 ---
# Division / always performs true floating point division
result = 5 / 2   # Returns 2.5 (float)
floor_div = 5 // 2  # Returns 2 (int, explicit floor division)
```

### 2. Built-in `print` Statement vs Function (PEP 3105)
```python
# --- PYTHON 2.7 ---
print "Binary of", 10, "=", bin(10)  # Language statement
print("A", "B")  # Prints tuple: ('A', 'B')

# --- PYTHON 3.3 - 3.13 ---
print("Binary of", 10, "=", bin(10))  # Built-in function
print("A", "B", sep=", ", end="\n")  # Supports keyword arguments (sep, end, file, flush)
```

### 3. Integer Unification (`int` & `long`)
```python
# --- PYTHON 2.7 ---
small_int = 42          # Type: <type 'int'>
huge_int = 10**20       # Type: <type 'long'>, outputs: 100000000000000000000L

# --- PYTHON 3.3 - 3.13 ---
small_int = 42          # Type: <class 'int'>
huge_int = 10**20       # Type: <class 'int'> (Arbitrary precision, no 'L' suffix)
```

### 4. Rounding Behavior (Banker's Rounding)
```python
# --- PYTHON 2.7 ---
round(2.5)  # Returns 3.0 (Float, rounds half away from zero)
round(3.5)  # Returns 4.0

# --- PYTHON 3.3 - 3.13 ---
round(2.5)  # Returns 2 (Int, Banker's Rounding: rounds to nearest EVEN number)
round(3.5)  # Returns 4 (Int)
```

### 5. Input Function (`raw_input` vs `input`)
```python
# --- PYTHON 2.7 ---
user_str = raw_input("Enter text: ")  # Returns str
user_eval = input("Enter expression: ")  # Evaluates code! (Security risk)

# --- PYTHON 3.3 - 3.13 ---
user_str = input("Enter text: ")  # Always returns str safely
```

---

## 🎓 Dual-Level Educational Explanations

### Beginner Level (New to Python)

> [!NOTE]
> **Welcome to Python Numbers!** Python handles numbers easily and intuitively. Here are the core building blocks:

1. **Number Types in Python**:
   - **Integers (`int`)**: Whole numbers like `-5`, `0`, `42`.
   - **Floats (`float`)**: Decimal numbers like `3.14`, `-0.001`, or scientific notation `3e8` ($3 \times 10^8 = 300,000,000$).
   - **Complex Numbers (`complex`)**: Numbers with a real part and an imaginary part (written with `j`), e.g., `4 + 3j`.

2. **Basic Operations**:
   - `+` (Addition), `-` (Subtraction), `*` (Multiplication).
   - `/` (**True Division**): Always gives a decimal answer (e.g., `7 / 2 = 3.5`).
   - `//` (**Floor Division**): Cuts off the decimal part (e.g., `7 // 2 = 3`).
   - `%` (**Modulus**): Gives the remainder of division (e.g., `7 % 2 = 1`).
   - `**` or `^` in calculator (**Exponent**): Powers (e.g., `2 ** 3 = 8`).

3. **What is Truthiness?**
   In Python, every number or object can act as `True` or `False`:
   - `0`, `0.0`, `None`, and empty lists `[]` are **False**.
   - Any non-zero number (like `1`, `-5`, `0.201`) or non-empty string is **True**.

4. **Prime Numbers**:
   A prime number is a number greater than 1 that can only be divided by 1 and itself (e.g., 2, 3, 5, 7, 11, 13, 17, 19, 23, 29).

---

### Advanced & Senior Level (Deep Dive)

> [!IMPORTANT]
> **Architectural & Implementation Details for Senior Engineers**:

1. **CPython `PyLongObject` Internal Representation**:
   In CPython (Python 3.3+), integers are represented as variable-length structures:
   ```c
   struct _longobject {
       PyObject_HEAD
       statictop _PyLongValue val; // Array of digits (digit = 30-bit or 15-bit unsigned int)
   };
   ```
   Unlike C's fixed `int64_t`, Python integers grow dynamically in memory. There is no integer overflow; operations automatically allocate additional memory digits as required.

2. **IEEE 754 Floating-Point & Precision**:
   Python floats correspond to double-precision (64-bit) IEEE 754 binary floating-point numbers in C (`double`).
   - **Representation Limits**: 53 bits of mantissa precision ($\approx 15\text{--}17$ decimal digits).
   - **Special Values**: `float('nan')` (Not a Number, `nan != nan`), `float('inf')`, `float('-inf')`.

3. **Banker's Rounding (IEEE 754 Standard)**:
   Python 3 implements round-half-to-even (`round()`):
   $$\text{round}(x) = \text{nearest integer}, \quad \text{if } x = k + 0.5 \implies \text{even integer}$$
   This eliminates statistical bias when summing rounded numbers over large data sets.

4. **Prime Algorithm Computational Complexity**:
   - **Version 1 (`is_prime_v`)**: $O(N)$ trial division.
   - **Version 2 (`is_prime_v2`)**: $O(\sqrt{N})$ trial division. Limit $D \le \lfloor\sqrt{N}\rfloor$.
   - **Version 3 (`is_prime_v3`)**: $O(\frac{\sqrt{N}}{2})$ trial division. Evaluates $N=2$, rejects even numbers ($N \pmod 2 = 0$), and increments divisors by 2 ($3, 5, 7, \dots$).

5. **CPython Bytecode Opcodes**:
   In Python 3.11+, Adaptive Inline Caching optimizes numerical bytecodes (e.g., `BINARY_OP_ADD_INT`, `BINARY_OP_MULTIPLY_FLOAT`), dynamically specializing operations when types remain monomorphic.

---

## 🧪 Unit Test Suite & Verification

A unified test suite (`test_numbers.py`) has been written using Python's standard `unittest` library.

### Running the Unit Tests:
```bash
python -m unittest discover -s ~/PycharmProjects/Devel/Python/2.Numbers -p "test_*.py"
```

### Test Coverage Summary:
- `test_bin_hex_oct_num`: Validates radix conversions and complex type creation.
- `test_calculator`: Tests arithmetic operations, exponent, modulus, floor division, and `ZeroDivisionError`/`ValueError` exceptions.
- `test_complex_num`: Asserts real/imag float decomposition.
- `test_deciamel`: Checks all integer/decimal arithmetic operators.
- `test_example`: Validates radix parsing for base 2, 3, and 4.
- `test_f_num`: Verifies list transformation and formatted string outputs.
- `test_floats`: Validates float arithmetic and IEEE 754 special values (`nan`, `inf`).
- `test_inte`: Tests arbitrary precision integer arithmetic.
- `test_is_prime_v`, `test_is_prime_v2`, `test_is_prime_v3`: Asserts boundary values (negative, 0, 1, 2, 3, composite 4, prime 29) across all algorithm implementations.
- `test_nearst_number`: Asserts Banker's rounding and comma string formatting (`1,000`).
- `test_none_bool`: Checks boolean truthiness for all 15 test cases.
- `test_random_num`: Asserts range boundaries, sample uniqueness, and length constraints.

> [!NOTE]
> All 14 tests execute cleanly without needing user interactive input.
