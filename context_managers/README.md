# Context Managers Tutorial Module

Welcome to the **Context Managers Tutorial Module** in Python. This directory provides clear, pedagogical demonstrations of class-based context managers, generator-based context managers (`@contextmanager`), directory switching patterns, and comprehensive unit tests.

---

## 📋 Table of Contents

1. [Overview & Architecture](#overview--architecture)
2. [Module Index](#module-index)
3. [`import` vs `from ... import ...` Namespace Mechanics](#import-vs-from--import--namespace-mechanics)
4. [Cross-Version Evolution (Python 2.7 to Python 3.13)](#cross-version-evolution-python-27-to-python-313)
5. [Range Sequence Iterators & Performance Notes](#range-sequence-iterators--performance-notes)
6. [`dir(range)` Reflection Matrix](#dirrange-reflection-matrix)
7. [Running Unit Tests](#running-unit-tests)

---

## 1. Overview & Architecture

Context managers handle resource setup and teardown automatically using Python's `with` statement:

```python
with EXPRESSION as TARGET:
    SUITE
```

### Protocol Lifecycle

- **`__enter__(self)`**: Initializes the resource (e.g., opening a file or changing working directory) and returns a reference.
- **`__exit__(self, exc_type, exc_val, exc_tb)`**: Guarantees resource release (e.g., closing file stream or restoring working directory), even when runtime errors occur.

---

## 2. Module Index

| Module Filename | Description & Purpose |
| :--- | :--- |
| `class_context_manager.py` | Class-based context manager (`OpenTextFile`) implementing `__enter__` and `__exit__`. |
| `generator_context_manager.py` | Generator context manager (`open_text_file`) using `contextlib.contextmanager`. |
| `context_manager_directory_change.py` | Directory switching context manager (`change_directory`) preserving CWD state. |
| `dir_first/` | Single-resource context management, stream safety, and unit test suite. |
| `dir_second/` | Multi-resource dynamic `ExitStack` context management and unit test suite. |
| `test_context_managers.py` | Automated `unittest` suite covering all context manager modules in this directory. |

---

## 3. `import` vs `from ... import ...` Namespace Mechanics

- `import os`: Imports the entire `os` module object into the current namespace. Functions are called with explicit namespace qualification: `os.getcwd()`.
- `from contextlib import contextmanager`: Imports specific symbols (`contextmanager`) directly into the local namespace, enabling direct call syntax `@contextmanager`.

---

## 4. Cross-Version Evolution (Python 2.7 to Python 3.13)

### Version Features & Syntax Evolution

| Python Release | Context Manager & Syntax Feature | Architectural Difference |
| :--- | :--- | :--- |
| **Python 2.7** | Manual `try...finally` resource cleanup | Requires explicit `fh.close()` in `finally` blocks; `range()` evaluates full lists in memory. |
| **Python 3.3** | `contextlib.ExitStack` introduced | Dynamic resource management introduced. `range` converted to $O(1)$ lazy sequence. |
| **Python 3.10** | Parenthesized context managers | `with (A() as a, B() as b):` syntax introduced. |
| **Python 3.13** | Zero-cost inline exception handling | Specialized CPython bytecode (`BEFORE_WITH`, `WITH_EXCEPT_START`). |

#### Legacy Python 2.7 vs Modern Python 3.13

```python
# Legacy Python 2.7 (Manual cleanup):
fh = open("myfile.txt", "w")
try:
    fh.write("Legacy write\n")
finally:
    fh.close()

# Modern Python 3.13 (Context Manager):
with open("myfile.txt", "w", encoding="utf-8") as fh:
    fh.write("Modern write\n")
```

---

## 5. Range Sequence Iterators & Performance Notes

In Python 3.3+, `range()` generates numbers on demand with $O(1)$ constant space complexity (~48 bytes), compared to Python 2.7's $O(N)$ list allocation.

```python
import sys

# O(1) Memory footprint:
r_iter = iter(range(1_000_000))
print(f"range iterator memory: {sys.getsizeof(r_iter)} bytes")  # ~48 bytes

# O(N) Materialized list memory:
r_list = list(range(1_000_000))
print(f"Materialized list memory: {sys.getsizeof(r_list)} bytes")  # ~8 MB
```

---

## 6. `dir(range)` Reflection Matrix

Inspecting `dir(range)` displays the sequence attributes and public methods:

```python
r = range(10, 100, 5)
print("Start:", r.start)  # 10
print("Stop :", r.stop)   # 100
print("Step :", r.step)   # 5
print("Index of 25:", r.index(25))  # 3
print("Public Members:", [m for m in dir(r) if not m.startswith("__")])
# ['count', 'index', 'start', 'step', 'stop']
```

---

## 7. Running Unit Tests

Execute the unit test suite from the repository root:

```bash
python3 -m unittest discover -s context_managers -p "test_*.py"
```
