# Python Reserved & Soft Keywords Master Module

Welcome to the **Python Keywords Master Guide**, a production-grade educational reference detailing CPython reserved keywords (`keyword.kwlist`), soft keywords (`keyword.softkwlist`), language syntax evolution from **Python 2.7 to Python 3.13**, unit testing, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Technical Architecture](#-overview--technical-architecture)
2. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
3. [Directory Structure & Module Overview](#-directory-structure--module-overview)
4. [Hard Keywords vs Soft Keywords](#-hard-keywords-vs-soft-keywords)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Keyword Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-keyword-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 🔑 Overview & Technical Architecture

Keywords are special reserved words in Python that have predefined syntax meanings to the CPython compiler and parser. Identifiers cannot match hard reserved keywords.

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_keywords.py`](file:///home/monika/PycharmProjects/Devel/Python/keywords/beginner_keywords.py))
Focuses on fundamental control flow, loop mechanics, boolean logic, and basic error handling:
- **Control Flow**: `if`, `elif`, `else`, `return`.
- **Iteration**: `for`, `while`, `in`.
- **Boolean Operators**: `and`, `or`, `not`, `is`.
- **Exception Handling**: `try`, `except`.

```python
# Beginner Example: Control flow and error handling
try:
    if age >= 18 and is_registered is True:
        return "Access Granted"
    else:
        return "Access Denied"
except TypeError:
    return "Invalid Age Data"
```

---

### 🚀 Intermediate Level ([`intermediate_keywords.py`](file:///home/monika/PycharmProjects/Devel/Python/keywords/intermediate_keywords.py))
Focuses on resource management, sequence generators, functional concepts, scope modification, and assertions:
- **Resource Management**: `with`, `as`, `finally`.
- **Generators & Iterators**: `yield`, `yield from`.
- **Functional & Loop Control**: `lambda`, `assert`, `break`, `continue`, `pass`, `raise`.
- **Scope Control**: `nonlocal`, `global`.

```python
# Intermediate Example: Generator delegation and context management
def generate_even_numbers(limit: int):
    yield from (i for i in range(limit) if i % 2 == 0)

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Resource managed safely")
```

---

### 🔥 Senior Level ([`senior_keywords.py`](file:///home/monika/PycharmProjects/Devel/Python/keywords/senior_keywords.py))
Focuses on high-concurrency async coroutines, structural pattern matching, CPython AST parsing, and soft keyword type statements:
- **Asynchronous I/O**: `async`, `await`.
- **Structural Pattern Matching**: `match`, `case`, `_` (CPython 3.10+).
- **CPython Introspection**: `ast.parse()`, `ast.walk()` node inspection.
- **Type Statements & Soft Keywords**: `type` alias statements (CPython 3.12+).

```python
# Senior Example: Async coroutines and structural pattern matching
async def process_command(cmd: str) -> str:
    await asyncio.sleep(0.01)
    match cmd.split():
        case ["start", service]:
            return f"Started {service}"
        case _:
            return "Unknown"
```

---

## 📁 Directory Structure & Module Overview

```text
keywords/
├── README.md                 # Master documentation and multi-tier guide
├── beginner_keywords.py      # Beginner level keyword examples (if/else/for/try)
├── intermediate_keywords.py  # Intermediate level keyword examples (with/yield/lambda/nonlocal)
├── senior_keywords.py        # Senior level keyword examples (async/match/case/ast)
├── python_keywords.py        # Programmatic reserved/soft keyword inspector
├── print_keywords.py         # Formatted grid & line-by-line keyword printer
├── keyword_list.py           # Backward-compatible wrapper for keyword list
├── print_kwd.py              # Backward-compatible wrapper for line printing
└── test_keywords.py          # Comprehensive multi-tier unit test suite
```

| File Name | Developer Tier | Key Concepts & Keywords |
| :--- | :--- | :--- |
| `beginner_keywords.py` | 🌱 Beginner | `if`, `else`, `for`, `while`, `try`, `except`, `and`, `or`, `not` |
| `intermediate_keywords.py` | 🚀 Intermediate | `with`, `yield`, `yield from`, `lambda`, `assert`, `nonlocal`, `global` |
| `senior_keywords.py` | 🔥 Senior | `async`, `await`, `match`, `case`, `_`, `type`, `ast.parse` |
| `python_keywords.py` | All Tiers | `keyword.kwlist`, `keyword.softkwlist`, `iskeyword()` |
| `print_keywords.py` | All Tiers | `print_keywords_grid()`, `print_keywords_line_by_line()` |
| `test_keywords.py` | All Tiers | `unittest` suite covering all 3 developer tiers |

---

## 🚀 How to Run the Code

```bash
# Run beginner tier examples
python3 beginner_keywords.py

# Run intermediate tier examples
python3 intermediate_keywords.py

# Run senior tier examples
python3 senior_keywords.py

# Run programmatic keyword inspection
python3 python_keywords.py

# Run formatted grid printer
python3 print_keywords.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_keywords.py

# Run with pytest from repository root
pytest keywords/
```

---

## ⚡ Python 3.3 to 3.13 Keyword Evolution Matrix (with Python 2.7 Context)

| Python Version | Keyword Additions / Modifications | Syntax & Compiler Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | `print`, `exec`, `raise`, `yield` | `print` and `exec` were statement keywords. | `print "Hello"` was a statement; `print` was not a function. |
| **Python 3.0** | Added `nonlocal`; Removed `print`, `exec` | `print()` became a function; `True`, `False`, `None` became keywords. | Reassigned `True = 0` was allowed in Python 2.7; forbidden in 3.0+. |
| **Python 3.3** | `yield from` (PEP 380) | Generator delegation syntax using `yield from`. | Handled via explicit `for item in gen: yield item` in 2.7/3.2. |
| **Python 3.4** | `pathlib.Path`, `enum.Enum` | Standardized `asyncio` keywords preparation. | Core keyword list static at 33 keywords. |
| **Python 3.5** | Added `async`, `await` (PEP 492) | Coroutine syntax introduced; parsed as context keywords. | Async coroutines written with `@asyncio.coroutine` decorator in 3.4. |
| **Python 3.7** | Reserved `async` & `await` | `async` and `await` promoted to hard reserved keywords (`SyntaxError` on variable use). | Variables named `async` broken when migrating to 3.7+. |
| **Python 3.8** | Added `/` positional-only parameter syntax | Positional-only parameter delimiter syntax. | Core hard keyword list stood at 35 keywords. |
| **Python 3.9** | Generic type hints (`list[str]`) | Built-in collection generics syntax without `typing`. | `kwlist` returned 35 reserved keyword strings. |
| **Python 3.10**| Added Soft Keywords: `match`, `case`, `_` | Structural Pattern Matching (PEP 634); `keyword.softkwlist` added. | Contextual keywords enabled pattern matching without breaking existing code. |
| **Python 3.11**| Exception Groups (`except*`) | `except*` added for multi-exception handling (PEP 654). | Extended exception syntax handling in async task groups. |
| **Python 3.12**| Added Soft Keyword `type` | Type alias syntax `type Point = tuple[float, float]` (PEP 695). | `type` operates as soft keyword in type alias definitions. |
| **Python 3.13**| Free-threaded CPython (GIL-free) | `TypeIs`, `ReadOnly`, GIL-free thread execution. | Concurrent keyword validation across threads. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Keyword iteration and index traversal frequently utilize `range()` sequence objects:

```python
# Iterating keywords in grid chunks using range()
keywords = get_all_python_keywords()
for i in range(0, len(keywords), 5):
    chunk = keywords[i : i + 5]
    print(f"Row {i//5 + 1}: {chunk}")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Querying `"def" in keywords` requires list linear search ($O(N)$), while numerical sequence containment `500 in range(1_000_000)` evaluates in $O(1)$ arithmetic time.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` shows standard sequence methods:

```python
r = range(0, 35, 5)
print(r.start)  # Output: 0
print(r.stop)   # Output: 35
print(r.step)   # Output: 5

print(r.index(15))  # Output: 3
print(r.count(10))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
