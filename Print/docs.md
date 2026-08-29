# Python `print` Definition & Version Evolution (Python 2.7 to Python 3.13)

This document defines the exact specification, formal signatures, and behavioral changes of `print` across Python versions from Python 2.7 to Python 3.13.

Versions with identical definitions and signatures are **grouped together**, and separated only where functional or syntactic changes occurred.

---

### Quick Comparison Matrix

| Version Group | Type | Formal Signature / Syntax | Key Changes |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Statement / Keyword | `print [>> file,] [expr1, expr2, ... [',']]`<br>*(Future: `print(*objects, sep=' ', end='\n', file=sys.stdout)`)* | • Language statement keyword<br>• Trailing comma suppresses newline<br>• `>>` stream redirection<br>• `from __future__ import print_function` (PEP 3105) |
| **Python 3.0 – 3.2**<br>*(Grouped Identical)* | Built-in Function | `print(*objects, sep=' ', end='\n', file=sys.stdout)` | • Replaced statement with built-in function (PEP 3105)<br>• Added `sep=' '` and `end='\n'` parameters<br>• Added `file` parameter replacing `>>`<br>• First-class function (can be passed to higher-order functions) |
| **Python 3.3 – 3.13**<br>*(Grouped Identical)* | Built-in Function | `print(*objects, sep=' ', end='\n', file=None, flush=False)` | • Added `flush=False` keyword argument (PEP 3105)<br>• `file=None` explicitly defaults to `sys.stdout`<br>• Signature identical across all 11 versions (3.3 – 3.13)<br>• Modern f-string integration (3.6+, 3.8+, 3.12+) |

---

### Group 1: Python 2.7 (and Python 2.x Legacy)

#### Definition & Syntax:
```python
print [>> file,] [expression (',' expression)* [',']]
```

#### Code Examples:
```python
# Standard print with newline
print "Hello", "Python"

# Trailing comma suppresses newline (adds a space)
print "Hello", 

# Stream redirection using >> operator
print >> sys.stderr, "Fatal error occurred"

# Forward compatibility via PEP 3105:
from __future__ import print_function
print("Hello", "Python", sep=" ", end="\n", file=sys.stdout)
```

> **Notice for Python 2.7:**
> 1. In Python 2.7, `print` is a statement keyword in the grammar, **not** a built-in function.
> 2. Parentheses are treated as expression grouping: `print("A", "B")` prints a tuple `('A', 'B')` instead of `A B`.
> 3. No `sep`, `end`, or `flush` parameters exist without `from __future__ import print_function`.
> 4. Cannot be passed as a first-class function (e.g. `map(print, items)` produces a `SyntaxError`).

---

### Group 2: Python 3.0 – Python 3.2 (Grouped Identical)

#### Formal Signature:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout)
```

#### Parameters:
- `*objects`: Any positional arguments to print (each converted via `str()`).
- `sep`: String inserted between objects (default: `' '`).
- `end`: String appended at the end (default: `'\n'`).
- `file`: Stream object with `.write()` method (default: `sys.stdout`).

#### Code Examples:
```python
# Custom separator and terminator
print("2026", "08", "16", sep="-", end=" | ")
print("Done")  # Output: 2026-08-16 | Done

# Redirection to in-memory buffer or file
import io
buf = io.StringIO()
print("Captured log", file=buf)
```

> **Notice for Python 3.0 – 3.2:**
> 1. Python **3.0, 3.1, and 3.2** share the **exact same** definition and signature.
> 2. `print()` is a first-class function object (can be passed as a callback or assigned to variables).
> 3. The `flush` keyword parameter did **not** exist in 3.0–3.2; flushing output required calling `sys.stdout.flush()`.

---

### Group 3: Python 3.3 – Python 3.13 (Grouped Identical)

#### Formal Signature:
```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

#### Parameters:
- `*objects`: Positional values to be printed.
- `sep`: String separator between values (default: `' '`).
- `end`: String terminator appended at the end (default: `'\n'`).
- `file`: Stream object (default: `None`, which defaults to `sys.stdout`).
- `flush`: Boolean. If `True`, forcibly flushes the output stream immediately.

#### Code Examples:
```python
# Immediate buffer flush without calling sys.stdout.flush()
print("Connecting...", end="", flush=True)

# Python 3.6+ f-string formatting
name = "Developer"
print(f"Welcome, {name}!")

# Python 3.8+ self-documenting debug specifier
status_code = 200
print(f"{status_code=}")  # Output: status_code=200

# Python 3.12+ nested expressions & quotes (PEP 701)
print(f"Users: {', '.join(['Alice', 'Bob'])}")
```

> **Notice for Python 3.3 – 3.13:**
> 1. **Identical Signature**: Across all 11 minor releases (**Python 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, and 3.13**), the formal definition and CPython C-level signature of `print()` remained **100% identical and unchanged**.
> 2. **`flush=False`**: Added in Python 3.3 to eliminate manual `sys.stdout.flush()` calls when printing real-time status/progress bars.
> 3. **Formatting Evolution (3.3–3.13)**:
>    - **3.6+**: Formatted string literals (`f"..."`, PEP 498).
>    - **3.8+**: Debug specifier (`f"{var=}"`).
>    - **3.11+**: Enhanced traceback pinpointing on print expressions.
>    - **3.12+**: Syntactic formalization allowing quotes and backslashes inside f-strings (PEP 701).
>    - **3.13+**: Interactive REPL with colorized error traces.

---

### Files in `1.Print/` Directory

- `python_version.py`: Inspects active interpreter version and displays grouped print definitions.
- `print_definition.py`: Executable demonstration of print definitions and signatures across all 3 version groups.
- `print.py`: Demonstrates `end` parameter, data types (`int`, `float`), and type comparisons.
- `example.py`: Demonstrates `strip()`, `capitalize()`, `title()`, and modern f-strings.
- `name.py`: Demonstrates name formatting and whitespace cleaning.
- `rounds.py`: Demonstrates `round()` behavior and float formatting specifiers.
- `split_name.py`: Demonstrates `split()` and name unpacking.
- `stripe.py`: Demonstrates string stripping and print end parameter.
- `stripe_title.py`: Demonstrates `strip()`, `title()`, and `count()`.
- `test_example.py`: Unit test suite covering all module transformations and print operations.