# ⚠️ Python Exception Handling (`exception_handling`) Pedagogical Module

Welcome to the **`exception_handling` Pedagogical Module**. This module provides a complete reference architecture for mastering runtime error handling, custom exception hierarchies, stack propagation, traceback introspection, resource management, and Python 3 exception chaining.

---

## 📂 Module Architecture

```
exception_handling/
├── basic_try_except.py                   # Core try-except blocks (ZeroDivisionError, ValueError, KeyError, IndexError)
├── multiple_exceptions.py                # Multi-exception handling (tuples & multi-branch clauses)
├── try_else_finally.py                   # Full 4-clause lifecycle (try, except, else, finally)
├── exception_objects_and_traceback.py    # Exception instances (as err), err.args, & traceback formatting
├── raising_and_custom_exceptions.py      # Custom exceptions (ApplicationError) & chaining (raise ... from ...)
├── exception_propagation_and_stack.py    # Call stack unwinding & multi-tier error bubbling
├── file_and_resource_handling.py         # File I/O exceptions (FileNotFoundError, PermissionError, with open)
├── config_file.txt                       # Sample configuration file for file I/O operations
├── test_exception_handling.py            # Unittest suite validating all 7 exception handling modules
├── requirements.txt                      # Dependency specification (Standard library footprint)
└── README.md                             # Module documentation and usage guide
```

---

## 🌟 What is New in This Module Update

1. **Consolidation of 43 Legacy Files**: Replaced 43 fragmented, misspelled, and duplicated scripts (`catchign.py`, `try_1.py`, `tryexcept.py`, `main_exception.py`, etc.) with a clean 7-part pedagogical progression.
2. **Standardized Python Naming**: All module filenames are valid Python identifiers enabling clean imports (`from exception_handling.basic_try_except import ...`).
3. **Explicit Exception Chaining (`raise ... from ...`)**: Added explicit demonstration of Python 3 exception chaining preserving underlying causal exceptions (`err.__cause__`).
4. **PEP 8 Compliance & Type Annotations**: Modernized code with standard Pythonic conventions, complete type hints (`Optional`, `Union`, `Tuple`, `Dict`), docstrings, and `if __name__ == "__main__":` entry points.
5. **Comprehensive Unittest Suite**: Introduced `test_exception_handling.py` covering all exception scenarios and custom exception classes using Python's `unittest` framework.

---

## 🏗️ Python Built-in Exception Hierarchy

All built-in exceptions inherit from `BaseException`. User-defined custom exceptions must inherit from `Exception`.

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception (Root for user & runtime exceptions)
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── NameError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── TimeoutError
      └── RuntimeException
```

---

## 🔍 Modules, Attributes & Methods Reference

### 1. `basic_try_except.py` — Fundamental Exception Trapping

Monitors risky code inside `try` blocks and catches specific runtime errors with fallback values.

#### Handled Exception Types & Methods

- **`ZeroDivisionError`**: Raised when a division or modulo operation denominator is zero.
- **`ValueError`**: Raised when a function receives an argument of right type but inappropriate value.
- **`KeyError`**: Raised when a mapping (dictionary) key is not found.
- **`IndexError`**: Raised when a sequence subscript is out of range.

```python
from exception_handling.basic_try_except import safe_divide, safe_parse_int

# 1. Safe Division
res = safe_divide(10.0, 0.0)  # Returns None, prints error

# 2. Safe Parsing
parsed = safe_parse_int("abc")  # Returns None, prints error
```

---

### 2. `multiple_exceptions.py` — Multiple Clauses & Tuple Handlers

Demonstrates grouping related exception types into tuples and creating distinct multi-branch `except` blocks.

#### Methods & Syntax

- **`except (IndexError, ValueError) as err:`**: Traps either `IndexError` OR `ValueError` in a single handler block.
- **Sequential `except` branches**: Evaluated top-to-bottom; executes the first matching handler.

```python
from exception_handling.multiple_exceptions import process_command_args

# Traps both IndexError and ValueError in one tuple block
status, message = process_command_args([])
print(status, message)  # False, "InputError (IndexError)..."
```

---

### 3. `try_else_finally.py` — The 4-Clause Control Flow

Illustrates the complete execution order of Python's 4 exception clauses.

#### Clause Semantics

- **`try`**: Code block executed first.
- **`except`**: Executed if an exception occurs in `try`.
- **`else`**: Executed ONLY if NO exception occurred in `try`.
- **`finally`**: ALWAYS executed at the end, regardless of exceptions or returns.

```python
from exception_handling.try_else_finally import execute_transaction

# Triggers try -> else -> finally
success, balance, logs = execute_transaction(50.0, 200.0)
```

---

### 4. `exception_objects_and_traceback.py` — Introspection & Tracebacks

Demonstrates capturing exception instances and formatting tracebacks programmatically.

#### Attributes & Methods

- **`err.args`** *(tuple)*: Positional arguments passed to the exception constructor.
- **`type(err).__name__`** *(str)*: Name of the exception class.
- **`traceback.format_exc()`** *(str)*: Returns full formatted stack trace string.

```python
from exception_handling.exception_objects_and_traceback import inspect_exception_details

info = inspect_exception_details("zero")
print(info["type_name"])             # 'ZeroDivisionError'
print(info["formatted_traceback"])   # Full traceback string
```

---

### 5. `raising_and_custom_exceptions.py` — Custom Exceptions & Chaining

Demonstrates domain-specific exception classes and exception chaining.

#### Attributes & Syntax

- **`class CustomError(Exception):`**: Subclassing `Exception` to build domain hierarchies.
- **`raise NewError() from cause`**: Explicit exception chaining populating `__cause__`.
- **`err.__cause__`**: Reference to the underlying cause exception.

```python
from exception_handling.raising_and_custom_exceptions import ValidationError, register_user

try:
    register_user({"username": "john", "age": 12})
except ValidationError as err:
    print(err.field)  # 'age'
    print(err.code)   # 400
```

---

### 6. `exception_propagation_and_stack.py` — Call Stack Unwinding

Demonstrates how uncaught exceptions bubble up nested function calls until trapped.

```python
from exception_handling.exception_propagation_and_stack import CalculationService

service = CalculationService()
try:
    # Error originates in divide_numbers(), bubbles through process_data()
    service.process_data([10.0, 0.0])
except ZeroDivisionError as err:
    print("Caught at top-level caller:", err)
```

---

### 7. `file_and_resource_handling.py` — Resource Cleanup & Context Managers

Demonstrates safe File I/O exception handling.

#### Exception Types & Context Managers

- **`FileNotFoundError`**: Raised when opening a non-existent file path.
- **`PermissionError`**: Raised when file permissions are denied.
- **`with open(...) as f:`**: Ensures automatic resource closure even if exceptions occur.

```python
from exception_handling.file_and_resource_handling import read_config_file_context_manager

content = read_config_file_context_manager("config_file.txt")
```

---

## 🚀 Execution & Testing Guide

### 1. Run Individual Demonstration Scripts

Execute any script directly using `python3`:

```bash
python3 exception_handling/basic_try_except.py
python3 exception_handling/multiple_exceptions.py
python3 exception_handling/try_else_finally.py
python3 exception_handling/exception_objects_and_traceback.py
python3 exception_handling/raising_and_custom_exceptions.py
python3 exception_handling/exception_propagation_and_stack.py
python3 exception_handling/file_and_resource_handling.py
```

### 2. Run the Unittest Suite

Execute the complete test suite:

```bash
python3 -m unittest exception_handling/test_exception_handling.py
```

Or using `pytest`:

```bash
pytest exception_handling/test_exception_handling.py
```
