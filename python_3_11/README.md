# Python 3.11 Overview & Features

**Release Date:** October 24, 2022  
**Key Focus:** Faster CPython (10-60% execution speedup), Exception Groups (`except*`), Native TOML Parser (`tomllib`), Enhanced Tracebacks with Fine-Grained Error Locations, and Typing `Self`.

---

## 🚀 Key Features & Syntax Additions

### 1. Faster CPython Project (PEP 659)
Python 3.11 is **10% to 60% faster** than Python 3.10, achieved through the Faster CPython initiative led by Mark Shannon and Guido van Rossum. Key architectural performance enhancements include:
- **Specialized Adaptive Interpreter**: Bytecode instructions specialize dynamically for specific operand types at runtime.
- **Faster Function Calls**: Inlined frame objects and call stack optimizations.
- **Zero-Cost Exceptions**: Exception handling overhead eliminated when no exception is raised.

### 2. Exception Groups & `except*` Syntax (PEP 654)
Introduced `ExceptionGroup` and `BaseExceptionGroup`, allowing multiple unrelated exceptions to be raised and handled simultaneously (essential for concurrent task runners).
- Added `except*` syntax to match specific exception types within an `ExceptionGroup`.

### 3. Native TOML Configuration Parser (`tomllib`) (PEP 680)
Added `tomllib` to the standard library, enabling fast, read-only parsing of TOML (Tom's Obvious Minimal Language) files without external dependencies.

### 4. Asynchronous Task Groups (`asyncio.TaskGroup`)
Introduced `asyncio.TaskGroup` as a modern, safer context-manager interface for running concurrent asynchronous tasks (replacing `asyncio.gather()` with structured concurrency semantics).

### 5. Self Type Annotation (`typing.Self`) (PEP 673)
Added `Self` to return the current class type dynamically, dramatically simplifying type hints for builder patterns, fluent interfaces, and class methods.

### 6. Fine-Grained Traceback Error Locations
Tracebacks now underline and point to the exact sub-expression or dictionary key that caused an error, rather than just pointing to the whole line.

### 7. String Enums (`enum.StrEnum`)
Added `StrEnum` to the `enum` standard module for enums whose members are also strings (`isinstance(val, str)` is `True`).

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 659** | Faster CPython | Specializing Adaptive Interpreter & frame memory layout |
| **PEP 654** | Exception Groups | `ExceptionGroup` and `except*` syntax |
| **PEP 680** | `tomllib` Module | Standard TOML format parser |
| **PEP 673** | `typing.Self` | Type hint returning the instance's own class type |
| **PEP 681** | `@dataclass_transform` | Class decorator for custom ORM / Dataclass generators |
| **PEP 655** | `Required` / `NotRequired` | Specify optional fields inside `TypedDict` |

---

## 💻 Pythonic Code Showcase

Check `main_3_11.py` in this directory for runnable code examples demonstrating:
- Handling concurrent exception groups using `try / except*`
- Parsing TOML configuration strings with `tomllib.loads()`
- Implementing fluent interface chaining using `Self` annotations
- Writing structured async code using `asyncio.TaskGroup`
- Creating string enums with `enum.StrEnum`
