# Technical Documentation: Python List & Dictionary Comprehensions (`9.List-comprehensions`)

## 1. Overview & Syntax Architecture
List comprehensions provide a concise syntax to create lists derived from existing iterables. They replace verbose `for` loop patterns with single-line expressions that are faster, more readable, and idiomatically Pythonic.

### Syntax Forms:
1. **Basic Mapping**: `[expression for item in iterable]`
2. **Filtered Mapping**: `[expression for item in iterable if condition]`
3. **Multi-Condition Filtering**: `[expression for item in iterable if cond1 and cond2]`
4. **Ternary Value Transformation**: `[val_if_true if condition else val_if_false for item in iterable]`
5. **Nested Comprehensions**: `[expr for row in matrix for item in row]` (e.g. Cartesian product)
6. **Dictionary Comprehensions**: `{key_expr: value_expr for item in iterable if condition}`
7. **Generator Expressions**: `(expression for item in iterable)` (Memory-efficient $O(1)$ lazy evaluation)

---

## 2. Python Version Evolution (Python 3.3 – Python 3.13 & Python 2.7 Comparison)

### A. Evolution across Python 3.3 to Python 3.13
1. **Python 3.0 Scope Isolation (PEP 3104 / PEP 3000)**:
   - In Python 2.7, loop variables in list comprehensions leaked into the surrounding function/global scope. In Python 3.0+, list comprehensions execute in their own isolated function scope, preventing variable shadowing or leakage.
2. **Python 3.6+**:
   - Dictionary comprehensions preserve insertion ordering as part of the language specification (PEP 468 / CPython 3.6+).
3. **Python 3.12 (PEP 709 - Inlined Comprehensions)**:
   - Python 3.12 eliminates frame creation overhead for list, set, and dictionary comprehensions by inlining bytecode generation into the enclosing function. Comprehensions execute up to **2x faster** in Python 3.12+ compared to Python 3.11 and earlier.

### B. Python 2.7 Legacy Comparison
- **Variable Leakage**:
  - Python 2.7: `[x for x in range(5)]; print x` printed `4` (variable `x` modified surrounding scope).
  - Python 3.x: `NameError: name 'x' is not defined` (proper lexical scope isolation).
- **`map` and `filter` Returns**:
  - In Python 2.7, `map()` and `filter()` returned concrete lists. In Python 3, they return lazy iterators, making `[expr for item in iterable]` or `list(map(...))` mandatory for list output.

---

## 3. Method Breakdown & Performance Benefits
- **Memory Efficiency**: Generator expressions `(x for x in data)` use $O(1)$ memory, avoiding allocating full lists in RAM.
- **File I/O Parsing**: `[line.rstrip() for line in open('file.txt')]` cleanly strips newline trailing whitespace during line iteration.
- **Cartesian Product**: Nested comprehensions `[(a, b) for a in A for b in B]` replace nested loops.
