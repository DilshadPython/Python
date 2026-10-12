# Workspace Task Summary: Modernizing `2.Numbers` (Python 3.3 – 3.13 & Python 2.7 Comparison)

All 17 scripts in `~/PycharmProjects/Devel/Python/2.Numbers` have been audited, refactored, modernized, and covered with automated unit tests.

Detailed documentation and side-by-side version comparison diffs have been saved to [docs.md](~/PycharmProjects/Devel/Python/2.Numbers/docs.md).

---

## 🚀 Key Improvements Across All 17 Files

1. **Python 3.3 – 3.13 Standardized Code**:
   - Standardized `print()` function syntax across all scripts (`from __future__ import print_function`).
   - Standardized true float division `/` vs explicit integer floor division `//` (`from __future__ import division`).
   - Extracted pure, reusable functions (`calculate()`, `decimal_operations()`, `is_prime_v()`, `is_prime_number()`, `shift_multiply()`, `calculate_average()`, etc.) so logic can be imported directly into test runners without side-effects.

2. **Fixed Bugs & Cross-Version Issues**:
   - **`primnumber.py`**: Refactored logic to fix broken return statements (`return print('No')`), zero-division error in step loop (`n / i == 0`), and added `is_prime_number(num)` pure function.
   - **`multipl.py`**: Extracted modular bitwise multiplication functions `shift_multiply()` and `shift_sequence()`, demonstrating left-shift (`<<=`) power-of-two multiplication.
   - **`get_average.py`**: Refactored with `calculate_average()` and `from __future__ import division` for true float division across Py2.7 and Py3.3-3.13.
   - **`calculator.py`**: Fixed a critical default argument bug where `num1=int(input(...))` evaluated input at module load time.
   - **`is_prime_v2.py` / `is_prime_v3.py`**: Wrapped `math.floor()` in `int()` (`int(math.floor(math.sqrt(num)))`) to prevent `TypeError` when passing floating-point range limits in legacy Python versions.
   - **`f_num.py` & `nearst_number.py`**: Converted unescaped f-strings to `str.format()` where universal version support was needed, while documenting f-string evolution from 3.6 to 3.13.
   - **`random_num.py`**: Wrapped ranges in `list(range(...))` to handle sequence sampling safely across version iterators.

3. **Added Comprehensive Unit Tests (`test_numbers.py`)**:
   - Created [test_numbers.py](~/PycharmProjects/Devel/Python/2.Numbers/test_numbers.py) using Python's standard `unittest` framework. Covers all 17 modules with test cases testing assertions, edge cases, exceptions (`ZeroDivisionError`, `ValueError`), boundary conditions, bitwise shifts, averages, and prime limits.

---

## 📊 Summary Table of Changed Files

| File | Primary Changes | Python Version Impact |
| :--- | :--- | :--- |
| **`bin_hex_oct_num.py`** | Extracted `convert_number_bases(x)` & `to_complex(y)` | Handles Py3 `0o` vs Py2 `0` octal prefixes |
| **`calculator.py`** | Fixed `input()` default argument execution; extracted `calculate(num1, op, num2)` | Safe headless CLI & unit testing |
| **`complex_num.py`** | Extracted `get_complex_details(val)` returning real & imag components | Standardized complex tuple inspection |
| **`deciamel.py`** | Extracted `decimal_operations(num1, num2)` with `get_input` compatibility | Fixed `input` vs `raw_input` security |
| **`example.py`** | Extracted `parse_base_string(val_str, base)` | Positional radix parsing (Base 2, 3, 4) |
| **`f_num.py`** | Replaced Py3.6+ f-strings with `str.format()`; extracted `add_constant_to_list()` | Grants universal Py2.7 - Py3.13 compatibility |
| **`floats.py`** | Added `float_operations()` and `inspect_special_floats()` | Tests IEEE 754 `nan`, `inf`, `-inf`, `3e8` |
| **`get_average.py`** | Extracted `calculate_average()` and `run_average_demo()` | Ensures true division float return across Py2.7 & Py3 |
| **`inte.py`** | Extracted `integer_operations(num1, num2)` | Documents Py3 `int` arbitrary precision |
| **`is_prime_v.py`** | Added $num \le 1$ edge case handling; extracted `benchmark_prime_v()` | $O(N)$ trial division benchmark |
| **`is_prime_v2.py`** | Wrapped `math.floor()` in `int()` cast for range bounds | Fixed `TypeError` on float limits |
| **`is_prime_v3.py`** | Added `int(math.floor(...))` cast & even number skip logic | Optimized $O(\sqrt{N}/2)$ prime check |
| **`multipl.py`** | Extracted `shift_multiply()` & `shift_sequence()` | Bitwise left-shift power-of-two multiplication |
| **`nearst_number.py`** | Extracted `format_and_round()`; added comma formatting `"{:,}".format()` | Documents Banker's Rounding vs Round-Half-Away |
| **`none_bool.py`** | Extracted `evaluate_truthiness()`; fixed typo (`o os` $\rightarrow$ `o is`) | Standardized truthiness testing for 15 types |
| **`primnumber.py`** | Fixed return statements & trial division modulo bug; added `is_prime_number()` | Clean $O(\sqrt{N}/2)$ trial division prime checker |
| **`random_num.py`** | Extracted `get_random_single()` and `get_random_sample()` | Safe range sampling across Python 3.3-3.13 |

---

## 🔍 Side-by-Side Python 2.7 Comparison Examples

### 1. Division Operator (`/` vs `//`)
```python
# --- PYTHON 2.7 ---
res = 5 / 2       # Truncates to 2 (int)

# --- PYTHON 3.3 - 3.13 ---
res = 5 / 2       # Always returns 2.5 (float)
floor_div = 5 // 2 # Returns 2 (int floor division)
```

### 2. Rounding Logic (Banker's Rounding vs Round-Half-Away)
```python
# --- PYTHON 2.7 ---
round(2.5)  # Returns 3.0 (Rounds half away from zero)

# --- PYTHON 3.3 - 3.13 ---
round(2.5)  # Returns 2 (Banker's Rounding: rounds to nearest EVEN integer)
round(3.5)  # Returns 4
```

### 3. `print` Statement vs Built-in Function
```python
# --- PYTHON 2.7 ---
print "Number:", 10  # Language keyword statement

# --- PYTHON 3.3 - 3.13 ---
print("Number:", 10, sep=" ", end="\n")  # Built-in function with sep/end/file/flush
```

---

## 🎓 Beginner vs Senior Explanations

- **Beginner Summary**: Python handles whole numbers (`int`), decimals (`float`), and complex numbers (`complex`). Modern Python 3 uses `/` for exact division (e.g. 5/2 = 2.5), `//` to chop off decimals (5//2 = 2), and `%` for remainders (5 % 2 = 1). Truthiness evaluates `0`, `0.0`, `None`, and `[]` as `False`, while non-zero numbers are `True`.
- **Senior Summary**: CPython 3 uses `PyLongObject` with digit arrays for arbitrary-precision integers, eliminating integer overflow. Floats adhere to 64-bit double-precision IEEE 754 semantics. Python 3's `round()` implements standard IEEE 754 Banker's Rounding (round-half-to-even) to minimize cumulative statistical bias. Prime checking algorithms progress from $O(N)$ to $O(\sqrt{N})$ and $O(\frac{\sqrt{N}}{2})$ with explicit `int(math.floor(...))` conversions to preserve step ranges across bytecodes.

---

## 🧪 Running the Unit Tests

Execute the test runner directly from the terminal:
```bash
python -m unittest discover -s ~/PycharmProjects/Devel/Python/2.Numbers -p "test_*.py"
```
