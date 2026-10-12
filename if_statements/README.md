# Python Conditional Execution & Control Flow (`If-Statement`)

A comprehensive, production-grade guide to conditional execution, boolean branching, truthiness evaluation, structural pattern matching (`match-case`), and cross-version compatibility across Python releases (**Python 2.7**, **Python 3.3** through **Python 3.13**).

---

## 📋 Directory File Index

| Script / Document | Core Topic / Feature | Key Functions & Concepts |
| :--- | :--- | :--- |
| [`LOGICALOP.md`](LOGICALOP.md) | Logical Operator Reference | Truth tables for `and`, `or`, and `not` operators. |
| [`if.py`](if.py) | Basic `in` Conditionals | `classify_day_type()`: Accessing list elements by index and checking set/list membership. |
| [`if_1.py`](if_1.py) | Relational Inequality | `compare_numbers()`: Magnitude comparison (`<`, `>`, `==`). |
| [`if_2.py`](if_2.py) | String Equality | `verify_string_match()`: Evaluating string literal value matching with `==`. |
| [`if_3.py`](if_3.py) | Integer Equality | `check_integer_equality()`: Numeric equality checks. |
| [`if_else.py`](if_else.py) | Dual-Branching | `verify_technology()`: Basic binary decision path (`if-else`). |
| [`if_else_1.py`](if_else_1.py) | String Length Validation | `validate_password_strength()`: Boundary length checks using `len()`. |
| [`if_elif.py`](if_elif.py) | Life Stage Categorization | `categorize_age_stage()`: Sequential age range evaluation (`Minor`, `Adult`, `Senior`). |
| [`elif.py`](elif.py) | Multi-Branch Grading & Temp | `evaluate_grade()`, `classify_temperature()`: Grade percentages and weather ranges. |
| [`check_number.py`](check_number.py) | Sign & Parity Analysis | `classify_number_sign()`, `check_parity()`, `analyze_number()`: Arithmetic modulo `% 2`. |
| [`if_and.py`](if_and.py) | Logical `and` Operator | `verify_user_access()`: Compound boolean requirements and short-circuit logic. |
| [`if_or.py`](if_or.py) | Logical `or` Operator | `verify_any_permission()`: Dual authorization checks. |
| [`if_not.py`](if_not.py) | Logical `not` Inversion | `check_registration_status()`: Inverting truth values. |
| [`if_advance.py`](if_advance.py) | Compound Expressions | `evaluate_compound_conditions()`: Combining `and`, `or`, `not` with parenthetical grouping. |
| [`if_then.py`](if_then.py) | Multi-Divisibility | `evaluate_number_properties()`: Evaluating divisibility by multiple factors (3 and 5). |
| [`if_what.py`](if_what.py) | Literal Booleans | `evaluate_literal_condition()`: Direct evaluation of `if True:` and `if False:`. |
| [`if_for.py`](if_for.py) | Iteration Filtering | `filter_numbers_above_threshold()`: Filtering numbers inside a loop context. |
| [`if_nesting.py`](if_nesting.py) | Nested vs Flat Conditions | `evaluate_housing_option()`, `evaluate_housing_flat()`: Refactoring deep nesting into `and`. |
| [`if_options.py`](if_options.py) | Truth Value Matrix | `evaluate_truthiness()`, `get_falsy_examples()`: Evaluating Falsy objects in Python. |
| [`more_if.py`](more_if.py) | Dynamic Registration Truth | `is_user_registered()`: Truthy evaluation of non-empty collections and non-zero scalars. |
| [`if_is.py`](if_is.py) | Identity vs Equality | `compare_value_and_identity()`: Memory reference `is` vs value equality `==`. |
| [`advance_if.py`](advance_if.py) | Ternary Expressions | `get_minimum_value()`, `classify_number_ternary()`: Compact `x if cond else y`. |
| [`triangle.py`](triangle.py) | Geometry Validation | `is_valid_triangle()`, `classify_triangle()`: Triangle Inequality Theorem enforcement. |
| [`match.py`](match.py) | Pattern Matching | `match_team_country()`: Python 3.10+ `match-case` structural pattern matching. |
| [`not_match.py`](not_match.py) | Wildcard Fallback | `classify_team_with_fallback()`: Wildcard `case _:` default fallback handling. |
| [`test_if_statements.py`](test_if_statements.py) | Comprehensive Test Suite | 35 automated `unittest` test cases covering all functions in this directory. |

---

## 📦 Understanding Python Import Statements (`import` vs `from ... import ...`)

Python provides two primary mechanisms for importing modules from the standard library or third-party packages:

### 1. `import module_name`
* **Syntax**: `import sys`
* **Behavior**: Loads the entire module object into memory and assigns it to the name `sys` in the current namespace.
* **Access Pattern**: Functions and attributes must be prefixed with the module name (e.g., `sys.version_info`, `sys.path`).
* **Advantages**: Prevents namespace pollution and name collisions (e.g., avoiding custom function names overwriting standard functions).

### 2. `from module_name import symbol_name`
* **Syntax**: `from typing import List, Tuple, Dict, Any, Union`
* **Behavior**: Imports specific classes, functions, or constants directly into the current namespace.
* **Access Pattern**: Symbols can be referenced directly without module prefixing (e.g., `List[int]` instead of `typing.List[int]`).
* **Advantages**: Concise, readable code when using type hints or frequently called utility functions.

---

## 🔍 Truthiness and Falsiness in Python

In Python, every object has an implicit truth value. When passed to an `if` statement or wrapped in `bool()`, objects evaluate to either `True` (Truthy) or `False` (Falsy).

### The Canonical Falsy Matrix

| Object Category | Falsy Values | Truthy Counterparts |
| :--- | :--- | :--- |
| **Booleans & Constants** | `False`, `None` | `True` |
| **Numeric Zeroes** | `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)` | `1`, `-5`, `3.14`, `1j` |
| **Empty Sequences** | `""` (empty str), `()` (empty tuple), `[]` (empty list) | `"hello"`, `(1,)`, `[0]` |
| **Empty Collections** | `{}` (empty dict), `set()` (empty set) | `{"a": 1}`, `{42}` |
| **Empty Ranges** | `range(0)` | `range(1, 10)` |

---

## 🔄 Python Version Evolution (Python 3.3 to Python 3.13) & Python 2.7 Comparison

### Python 2.7 Legacy Comparison

In Python 2.7 (deprecated December 31, 2019):
1. `print` was a statement, not a function (`print "Hello"` instead of `print("Hello")`).
2. Integer division performed floor truncation (`5 / 2` evaluated to `2`, whereas in Python 3 it evaluates to `2.5`).
3. User input used `raw_input()` for strings, whereas `input()` attempted to evaluate the entered string as code.

```python
# ==============================================================================
# Python 2.7 Legacy Sample
# ==============================================================================
# In Python 2.7:
user_age = raw_input("Enter your age: ")
age_num = int(user_age)

if age_num >= 18:
    print "Access Granted: Adult"
else:
    print "Access Denied: Minor"

# Integer division comparison in Py2 vs Py3:
val = 5 / 2
if val == 2:
    print "Python 2 integer division truncated result to 2"
```

---

### Code Evolution: Python 3.3 to Python 3.13

#### 1. Python 3.3 – Standard `if-elif-else`
```python
def check_status(score):
    if score >= 50:
        return "Passed"
    else:
        return "Failed"
```

#### 2. Python 3.8 – Assignment Expressions (The Walrus Operator `:=`)
PEP 572 introduced assignment expressions inside conditional statements, allowing values to be computed, assigned, and tested in a single expression:
```python
# Python 3.8+ Syntax:
sample_data = [10, 20, 30, 40, 50]

if (data_length := len(sample_data)) > 3:
    print(f"List is large ({data_length} elements)")
```

#### 3. Python 3.10 – Structural Pattern Matching (`match-case`)
PEP 634 introduced `match` and `case` statements, replacing long `if-elif-else` chains with clean pattern matching:
```python
# Python 3.10+ Syntax:
def classify_command(command: str) -> str:
    match command.split():
        case ["quit"]:
            return "Exiting system..."
        case ["load", filename]:
            return f"Loading file: {filename}"
        case ["save", filename]:
            return f"Saving file: {filename}"
        case _:
            return "Unknown command"
```

#### 4. Python 3.11 – Enhanced Tracebacks for Multi-Branch Expressions
Python 3.11 introduced fine-grained error location reporting in tracebacks, highlighting the exact sub-expression in compound `if` statements that caused an exception.

#### 5. Python 3.12 & 3.13 – Adaptive Bytecode & Truthiness Performance
Python 3.12 and 3.13 optimized boolean evaluation in `if` statements by introducing adaptive bytecode instructions like `TO_BOOL` and `POP_JUMP_IF_FALSE`, reducing CPU cycles required for truthiness checks during interpreter execution.

---

## ⚡ Documentation & Performance Notes

### 1. Short-Circuit Evaluation
In compound conditions:
- `A and B`: If `A` is `False`, Python immediately returns `False` without evaluating `B`.
- `A or B`: If `A` is `True`, Python immediately returns `True` without evaluating `B`.

*Optimization Tip*: Place lighter, faster checks or conditions most likely to fail first in `and` chains (or conditions most likely to succeed first in `or` chains).

### 2. Identity (`is`) vs Equality (`==`)
- `==` calls the `__eq__()` magic method to check if values match.
- `is` checks memory address equality (`id(a) == id(b)`).

*Performance Tip*: Testing identity (`if obj is None:`) executes in a single CPU instruction because it compares raw pointers, whereas `==` requires method lookup.

---

## 🧪 Executing Unit Tests

To run the full automated unit test suite across all 24 scripts:

```bash
python3 -m unittest discover -s If-Statement
```

Or run the test script directly:

```bash
python3 If-Statement/test_if_statements.py
```
