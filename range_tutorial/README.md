# Python Range Tutorial & Reference Module

Welcome to the **Python `range` Master Module**, a standardized, production-grade educational and reference resource for understanding sequence generation, numerical formatting, datetime styling, 3D ASCII graphics, and internal range mechanics in Python.

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Module Summaries](#module-summaries)
4. [How to Run the Code](#how-to-run-the-code)
5. [Running Unit Tests](#running-unit-tests)
6. [Python Version & Performance Evolution Summary](#python-version--performance-evolution-summary)

---

## 🌟 Overview

The `range` type is one of Python's most fundamental built-in sequence structures. Rather than constructing lists of integers in memory, a `range` object generates numbers lazily on-demand using $O(1)$ constant memory overhead regardless of sequence length.

This project refactors legacy range scripts into modern, PEP 8-compliant, fully type-annotated Python code equipped with defensive guard clauses, detailed inline comments, and a comprehensive test suite.

---

## 📁 Directory Structure

```text
Range/
├── README.md                 # Master project guide and usage documentation
├── docs.md                   # Pedagogical reference & Python version evolution (2.7 - 3.13)
├── range_basics.py           # Core sequence generation, range parameters & grid loops
├── range_formatting.py       # Zero-padded formatted string iteration with range()
├── number_formatting.py      # Float precision formatting & large integer thousand separators
├── datetime_formatting.py    # Datetime formatting specifiers (strftime, %B, %d, %j, %A)
├── graphics_3d.py            # ASCII visual patterns (pyramids, single-sided, decreasing spaces)
├── range_vs_xrange.py        # Python 2 vs Python 3 comparison, O(1) memory, dir(range)
├── xrange.py                 # Historical backward-compatible re-export module
└── test_range.py             # Comprehensive unittest suite (21 unit tests)
```

---

## 🛠️ Module Summaries

| Module File | Purpose & Focus | Key Functions |
| :--- | :--- | :--- |
| `range_basics.py` | Fundamental `range(start, stop, step)` operations and nested grid loops | `generate_sequence()`, `format_grid()`, `format_horizontal_sequence()` |
| `range_formatting.py` | Zero-padded string formatting driven by range loops | `format_range_numbers()`, `print_formatted_ranges()` |
| `number_formatting.py` | Precision float control and comma-separated byte calculations | `format_float_precision()`, `format_large_number()` |
| `datetime_formatting.py` | Timestamp styling using strftime specifiers and f-strings | `format_datetime_standard()`, `format_datetime_detailed()` |
| `graphics_3d.py` | ASCII visual pattern generators using range level calculations | `generate_ascii_pyramid()`, `generate_single_sided_pyramid()` |
| `range_vs_xrange.py` | Memory footprint analysis, sequence methods, `dir()` introspection | `compare_range_memory_and_type()`, `demonstrate_range_sequence_methods()` |
| `xrange.py` | Legacy compatibility adapter & historical deprecation notice | Imports and re-exports `range_vs_xrange.py` |
| `test_range.py` | Unit test suite covering all modules, inputs, and guard clauses | `TestRangeBasics`, `TestRangeVsXRange`, etc. |

---

## 🚀 How to Run the Code

Execute any module directly from the terminal to view formatted demonstrations:

```bash
# Run range fundamentals demonstration
python3 range_basics.py

# Run zero-padded number formatting demo
python3 range_formatting.py

# Run precision & large number formatting demo
python3 number_formatting.py

# Run datetime formatting demo
python3 datetime_formatting.py

# Run 3D ASCII graphics generator
python3 graphics_3d.py

# Run Python 2 vs Python 3 range analysis & dir(range) introspection
python3 range_vs_xrange.py
```

---

## 🧪 Running Unit Tests

Run the full suite of unit tests using Python's standard `unittest` test runner:

```bash
python3 -m unittest test_range.py
```

Expected Output:
```text
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.001s

OK
```

---

## ⚡ Python Version & Performance Evolution Summary

- **Python 2.7**: `range()` created an eager `list` of integer objects ($O(N)$ memory). `xrange()` was a separate generator-like type used to reduce memory consumption.
- **Python 3.0**: `xrange()` was removed, and `range()` was converted into an immutable sequence object ($O(1)$ constant memory overhead).
- **Python 3.2**: Containment testing (`val in range(...)`) was optimized from $O(N)$ linear scanning to $O(1)$ constant-time arithmetic evaluation.
- **Python 3.3**: Range objects gained `.index()` and `.count()` sequence methods, as well as full equality comparison (`range(0) == range(2, 1, 3)`).
- **Python 3.10**: Full support for structural pattern matching (`match ... case`).
- **Python 3.13**: Modern CPython internal optimizations guarantee range instances maintain a fixed overhead of 48 bytes regardless of step size or boundary range.

For full technical details, performance benchmarks, and `dir(range)` attribute references, see [`docs.md`](docs.md).
