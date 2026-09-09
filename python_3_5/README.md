# Python 3.5 Overview & Features

**Release Date:** September 13, 2015  
**Key Focus:** Native Async Syntax (`async`/`await`), Type Annotations Standard (`typing`), Generalized Unpacking, and Matrix Multiplication (`@`).

---

## 🚀 Key Features & Syntax Additions

### 1. Dedicated `async` & `await` Syntax (PEP 492)
Replaced generator-based coroutines with native, first-class language keywords `async def` and `await`, making asynchronous code far more readable and structured.

### 2. Type Hints Standardized (`typing` module) (PEP 484)
Introduced type annotations as part of the language runtime via the `typing` module (`List`, `Dict`, `Tuple`, `Optional`, `Union`, `Callable`), establishing the foundation for modern static type checkers like Mypy and IDE autocompletion.

### 3. Additional Unpacking Operators (PEP 448)
Allowed using `*` (iterable unpacking) and `**` (dictionary unpacking) in arbitrary contexts:
- Unpacking multiple iterables in lists/tuples/sets: `[*list1, *list2]`
- Unpacking multiple dictionaries in single literals: `{**dict1, **dict2}`

### 4. Matrix Multiplication Operator `@` (PEP 465)
Introduced a dedicated infix operator `@` (`__matmul__`, `__rmatmul__`, `__imatmul__`) specifically designed for matrix multiplication in linear algebra libraries (like NumPy).

### 5. High-Level Process Execution (`subprocess.run`) (PEP 489 / Stdlib)
Added `subprocess.run()` as the recommended, high-level standard interface for running subprocess commands safely and concisely.

### 6. Faster Directory Traversal (`os.scandir`) (PEP 471)
`os.scandir()` produces `DirEntry` objects containing file metadata during directory iteration, avoiding thousands of additional `stat()` calls and accelerating file system operations by 2x to 20x.

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 492** | `async` / `await` | Dedicated syntax for coroutines and async I/O |
| **PEP 484** | Type Hints | Type hints standard library (`typing`) |
| **PEP 448** | Generalized Unpacking | Extended `*` and `**` unpacking in literals and calls |
| **PEP 465** | `@` Operator | Infix binary operator for matrix multiplication |
| **PEP 471** | `os.scandir()` | High-performance directory iterator |

---

## 💻 Pythonic Code Showcase

Check `main_3_5.py` and `annotation.py` in this directory for runnable code examples demonstrating:
- Native `async def` and `await` with `asyncio`
- Generalized unpacking in lists, sets, and dictionary literals
- Defining and executing matrix operations using `@`
- Fast filesystem inspection with `os.scandir()`
- Type annotations with `typing.List`, `typing.Optional`, and `typing.Dict`
