# Python Library & `pathlib` Operations Master Module

Welcome to the **Python Library & Pathlib Module**, a production-grade educational reference detailing object-oriented filesystem path manipulation using Python's standard **`pathlib`** library (PEP 428), unit testing, and Python version evolutions from **Python 2.7 to Python 3.13**.

---

## 📌 Table of Contents

1. [Overview & Technical Architecture](#-overview--technical-architecture)
2. [Directory Structure & Module Overview](#-directory-structure--module-overview)
3. [How to Run the Code](#-how-to-run-the-code)
4. [Running Unit Tests](#-running-unit-tests)
5. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
6. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 📂 Overview & Technical Architecture

### Legacy `os.path` vs Modern Object-Oriented `pathlib.Path`

Prior to Python 3.4, filesystem paths were treated as raw strings manipulated via functions in `os` and `os.path`. This resulted in platform-dependent separator bugs (`/` vs `\`) and messy nested string calls.

**PEP 428 (`pathlib`, Python 3.4+)** introduced strongly-typed, object-oriented path abstractions:

```python
# ❌ UNSAFE Legacy Python Approach (String concatenation & platform split issues):
import os
file_path = os.path.join(os.path.dirname(__file__), "subfolder", "data.txt")
file_exists = os.path.exists(file_path)

# ✅ SECURE Modern Python Approach (Object-Oriented Path Abstraction):
from pathlib import Path
file_path = Path(__file__).parent / "subfolder" / "data.txt"
file_exists = file_path.exists()
```

---

## 📁 Directory Structure & Module Overview

```text
python_library/
├── README.md                 # Master documentation and evolution guide
├── pathlib_tutorial.py       # Object-oriented pathlib.Path functions & file I/O
├── path_lib.py               # Backward-compatible wrapper for path inspection
├── required.txt              # Sample configuration / requirement file fixture
└── test_pathlib_tutorial.py  # Unit test suite verifying path operations
```

| File Name | Purpose & Functionality | Key Functions |
| :--- | :--- | :--- |
| `pathlib_tutorial.py` | Object-oriented path manipulation & file I/O | `get_current_directory_info()`, `decompose_path()`, `list_directory_contents()`, `write_and_read_text_file()` |
| `path_lib.py` | Backward-compatible wrapper | `run_path_demo()` |
| `test_pathlib_tutorial.py` | Unit test suite (unittest framework) | `TestPathlibTutorial` |

---

## 🚀 How to Run the Code

```bash
# Run object-oriented pathlib tutorial
python3 pathlib_tutorial.py

# Run legacy wrapper script
python3 path_lib.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_pathlib_tutorial.py

# Run with pytest from repository root
pytest python_library/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Language Features & Syntax Additions | Standard Library & Path Handling Changes | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Legacy baseline syntax | `os.path.join()`, `os.path.exists()` string functions | Strings used for paths; platform backslash errors common. |
| **Python 3.3** | `yield from` (PEP 380), `u'str'` syntax | `sys.implementation`, improved file I/O errors | OS path strings defaulted to Unicode (`str`). |
| **Python 3.4** | `pathlib.Path` introduced (PEP 428) | Standardized `Path` objects, `.mkdir()`, `.iterdir()` | Replaced raw string manipulation with `Path` classes. |
| **Python 3.5** | Type Hints (`typing`), `async`/`await` | Type annotations for path functions | Static analysis support for path inputs (`path: Path`). |
| **Python 3.6** | F-strings `f"{var}"`, Path protocol | `os.PathLike` interface (PEP 519) for standard functions | Built-in functions (`open()`, `os.stat()`) accept `Path`. |
| **Python 3.7** | `@dataclass`, `breakpoint()` built-in | `Path.is_gaps()`, improved resolution handling | Order-preserving dictionary metadata for paths. |
| **Python 3.8** | Walrus operator `:=`, Positional-only `/` | `Path.unlink(missing_ok=True)` parameter | Concise path checks: `if (p := Path("data.txt")).exists():`. |
| **Python 3.9** | Dict Union `|`, Built-in generics `list[str]` | `Path.read_text()` / `Path.write_text()` encoding defaults | Simplified file read/write methods without explicit open context. |
| **Python 3.10**| Pattern Matching `match/case` (PEP 634) | Union operator `X \| Y` for path types | Match statement support for checking extension suffixes. |
| **Python 3.11**| Faster CPython (10-60% runtime speedup) | Performance optimizations for `Path.glob()` and `Path.stat()` | Fast path traversal with cached file attributes. |
| **Python 3.12**| Syntactic `type` statements, `@override` | `Path.walk()` method introduced (replacing `os.walk`) | `Path.walk()` yields `(dirpath, dirnames, filenames)` as Path objects. |
| **Python 3.13**| Free-threaded GIL-free CPython, Tier 2 JIT | `TypeIs`, `ReadOnly`, GIL-free parallel path scanning | High-performance parallel directory tree traversal. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Path index iteration and directory chunking often utilize `range()` sequence objects:

```python
# Iterating directory paths using range()
paths = list(Path(".").glob("*.py"))
for i in range(len(paths)):
    print(f"File {i+1}: {paths[i].name}")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects (~8 MB RAM).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Querying `500 in range(1_000_000)` evaluates using arithmetic bounds in $O(1)$ constant time.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` shows standard sequence methods:

```python
r = range(1, 10, 2)
print(r.start)  # Output: 1
print(r.stop)   # Output: 10
print(r.step)   # Output: 2

print(r.index(5))  # Output: 2
print(r.count(3))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Sequence boundary attributes.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
