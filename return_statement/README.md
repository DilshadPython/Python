# Python `return` Statement Master Module

Welcome to the **Python `return` Statement Master Module**, a standardized, production-grade educational and technical reference for understanding function return mechanics, implicit vs explicit returns, higher-order function closures, generator return values, guard clauses, and bytecode-level version evolution across Python 2.7 to Python 3.13.

---

## Directory Structure & Module Catalog

```text
Return/
├── README.md               # Overview, execution guide, file catalog, and usage reference
├── docs.md                 # Technical reference detailing bytecode, AST, PEPs, & version evolution
├── return_basics.py        # Fundamental return mechanics: implicit None, explicit values, tuple packing
├── return_advanced.py      # Advanced return patterns: closures, try-finally override, generators (PEP 380)
├── return_patterns.py      # Best practices: guard clauses, structured returns, dir() introspection
├── return_.py              # Refactored legacy script maintaining backward compatibility
└── test_return.py          # Comprehensive unittest suite (13 test cases)
```

---

## Module Summaries

### 1. `return_basics.py`
Demonstrates core return mechanics:
- **Implicit `None`**: What happens when a function omits a `return` statement.
- **Explicit Returns**: Returning computed primitive values (`int`, `float`, `str`).
- **Tuple Packing/Unpacking**: Returning multiple comma-separated values automatically wrapped in a tuple.
- **Conditional Branching**: Returning early based on boolean checks.

### 2. `return_advanced.py`
Demonstrates advanced language features and return behaviors:
- **Higher-Order Functions**: Returning internal functions (closures) with state binding.
- **`try...finally` Interaction**: How a `return` in a `finally` block overrides previous returns or uncaught exceptions.
- **Generator Returns (PEP 380)**: How `return value` inside a generator raises `StopIteration(value)` in Python 3.3+.
- **Type Annotations**: Utilizing `Callable`, `Optional`, and `NoReturn` (or `Never` in 3.11+).

### 3. `return_patterns.py`
Focuses on clean software engineering practices:
- **Guard Clauses**: Replacing deeply nested `if/else` ladders with early exit validation checks.
- **Structured Return Objects**: Returning clean, readable dictionary structures for status and payload reporting.
- **Object Introspection**: Examining methods available on returned values using `dir()`.

### 4. `return_.py`
The original legacy file updated to meet modern PEP 8 standards, proper type annotations, and descriptive docstrings while maintaining backward compatibility.

### 5. `test_return.py`
A comprehensive `unittest` test suite verifying functionality across all scripts, edge cases, exception handling, and return value integrity.

---

## How to Run the Code

### Running Individual Python Scripts

```bash
# Run basic return demonstrations
python3 return_basics.py

# Run advanced closure, try-finally, and generator demonstrations
python3 return_advanced.py

# Run return design patterns and introspection demonstrations
python3 return_patterns.py

# Run the refactored legacy demonstration script
python3 return_.py
```

### Running the Unit Test Suite

Execute the `unittest` framework from the command line:

```bash
python3 -m unittest test_return.py
```

Alternatively, run tests with verbose output:

```bash
python3 -m unittest -v test_return.py
```

---

## Quick Usage Examples

### Multiple Values Return (Tuple Packing & Unpacking)

```python
from return_basics import get_coordinate_3d

# Coordinates returned as a tuple: (1.0, 2.0, 3.0)
coords = get_coordinate_3d(1.0, 2.0, 3.0)

# Unpack tuple into individual variables
x, y, z = coords
print(f"X: {x}, Y: {y}, Z: {z}")
```

### Guard Clause Validation Pattern

```python
from return_patterns import validate_and_process_user

# Invalid user input returns early with error status
result = validate_and_process_user({"username": "", "age": 15})
print(result["status"])   # Output: 'error'
print(result["message"])  # Output: 'Missing required field: username'
```

---

## Summary of Python Version Evolution

| Feature / Behavior | Python 2.7 | Python 3.3 - 3.10 | Python 3.11 - 3.13 |
| :--- | :--- | :--- | :--- |
| **`return` in Generators** | `SyntaxError` if value attached | PEP 380: `return value` sets `StopIteration.value` | Enhanced `yield from` execution speed |
| **Return Type Annotations** | Not supported natively | PEP 484: `def f() -> str:` introduced in 3.5 | PEP 675 / 681 (`Never`, `Self`, `TypeVarTuple`) |
| **Bytecode Opcode** | `RETURN_VALUE` | `RETURN_VALUE` | `RETURN_CONST` introduced in 3.12 for constant returns |
| **`dir()` Introspection** | Returns attribute names as list of strings | Returns attribute names as list of strings | Optimized method caching and attribute lookup |

For a complete pedagogical breakdown of AST changes, bytecode disassembly, and performance comparisons, see [`docs.md`](docs.md).
