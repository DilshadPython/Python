# 🧮 Python Operators Master Module

Welcome to the definitive master tutorial module for **Python Operators**. This directory features a **3-step sequential curriculum**—guiding students step-by-step from fundamental arithmetic and assignment operators to relational logic, bitwise manipulations, walrus assignment expressions, parameter boundary operators (`/` and `*`), and range sequence performance notes.

---

## 📌 Directory Architecture & Sequential Learning Path

```text
Operators/
├── 01-Arithmetic-and-Assignment/       # Step 1: Fundamental Math & Variable Binding
│   ├── arithmetic_operators.py        # +, -, *, /, //, %, **, @ (Matrix Multiplication)
│   ├── assignment_operators.py        # =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=, :=
│   ├── test_arithmetic_assignment.py  # Unit tests for Step 1
│   └── __init__.py
│
├── 02-Comparison-and-Logical/         # Step 2: Relational Tests, Truth Tables & Bitwise Operations
│   ├── comparison_operators.py        # ==, !=, >, <, >=, <=, is, is not, in, not in
│   ├── logical_bitwise_operators.py   # and, or, not, &, |, ^, ~, <<, >>
│   ├── test_comparison_logical.py     # Unit tests for Step 2
│   └── __init__.py
│
├── 03-Advanced-Operators-and-Range/   # Step 3: Special Operators, Signatures & Range Performance
│   ├── walrus_and_special_operators.py # operator.attrgetter, operator.itemgetter, / and * parameters
│   ├── range_operator_evolution.py    # Range containment O(1), memory efficiency & dir(range)
│   ├── test_advanced_range.py         # Unit tests for Step 3
│   └── __init__.py
│
├── README.md                          # Sequential study guide & roadmap
├── docs.md                            # Technical operator precedence matrix & architecture
├── operators.py                       # Master operator demonstration entrypoint
└── test_operators_master.py           # Master test runner executing all test suites
```

---

## 🚀 Sequential Roadmap

| Step | Subdirectory | Focus & Key Concepts Covered |
| :--- | :--- | :--- |
| **Step 1: Arithmetic & Assignment** | `01-Arithmetic-and-Assignment/` | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `@` (Matrix Multiplication), augmented assignment (`+=`, `-=`), Walrus Operator (`:=`). |
| **Step 2: Relational & Bitwise** | `02-Comparison-and-Logical/` | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is` / `is not` (Identity), `in` / `not in` (Membership), short-circuit `and` / `or`, bitwise `&`, `\|`, `^`, `~`, `<<`, `>>`. |
| **Step 3: Advanced & Range** | `03-Advanced-Operators-and-Range/` | `operator.itemgetter`, `operator.attrgetter`, positional-only `/` and keyword-only `*` parameter syntax, `range` $O(1)$ memory notes & `dir(range)` reflection. |

---

## 🧪 Running the Unit Test Suite

Execute all tests across all 3 steps using Python's built-in `unittest` runner or `pytest`:

```bash
# Run master test runner
python3 Operators/test_operators_master.py

# Or run via pytest
pytest Operators/
```

---

## ⚡ CPython Version Evolution Breakdown (Python 2.7 ➔ Python 3.13)

- **Python 2.7**: `5 / 2` performed integer division resulting in `2`. The inequality operator `<>` was allowed alongside `!=`. `range()` returned a full materialized list in memory; `xrange()` was used for generator iteration.
- **Python 3.0+**: `/` performs float division (`5 / 2 == 2.5`), while `//` performs floor division. `<>` operator was removed in favor of `!=`. `range()` replaced `xrange()`, operating as an immutable sequence object computing elements lazily in $O(1)$ RAM.
- **Python 3.5**: Introduced `@` matrix multiplication operator (PEP 465) via `__matmul__` and `__rmatmul__` hooks.
- **Python 3.8**: Introduced Walrus Operator `:=` for assignment expressions inside conditions/loops (PEP 572), and positional-only parameter syntax `/` (PEP 570).
- **Python 3.10**: Structural pattern matching (`match / case` PEP 634) over operator expressions.
- **Python 3.11–3.13**: Specialized Adaptive Interpreter (CPython PEP 659) accelerates binary operator dispatching by **10–25%**.
