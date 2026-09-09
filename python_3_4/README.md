# Python 3.4 Overview & Features

**Release Date:** March 16, 2014  
**Key Focus:** Asynchronous I/O framework (`asyncio`), Object-oriented filesystem paths (`pathlib`), Enumerations (`enum`), and Standard Statistics (`statistics`).

---

## 🚀 Key Features & Syntax Additions

### 1. Object-Oriented File System Paths (`pathlib`) (PEP 428)
Introduced the `pathlib` module providing clean, object-oriented semantics for navigating, inspecting, and manipulating filesystem paths across different operating systems.

### 2. Enumeration Type (`enum`) (PEP 435)
Added `enum.Enum`, `enum.IntEnum`, and `enum.Flag` to the standard library, providing robust support for type-safe, iterable constant enumerations.

### 3. Asynchronous I/O Framework (`asyncio`) (PEP 3156)
Introduced `asyncio` (initially provisional, codenamed "Tulip"), introducing event loops, coroutines (`@asyncio.coroutine`), and futures into Python's core library.

### 4. Single-Dispatch Generic Functions (`functools.singledispatch`) (PEP 443)
Allows function overloading based on the type of the first argument, enabling elegant polymophic function implementations in pure Python.

### 5. Mathematical Statistics Module (`statistics`) (PEP 450)
Added built-in statistical functions such as `mean`, `median`, `mode`, `variance`, and `stdev`.

### 6. Standard Package Installer Included (`ensurepip`) (PEP 453)
`pip` is automatically installed with Python binary installers via `ensurepip`.

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 428** | `pathlib` module | Object-oriented filesystem paths |
| **PEP 435** | `enum` module | Standard implementation for enumerations |
| **PEP 3156**| `asyncio` module | Asynchronous I/O, event loops, and coroutines |
| **PEP 443** | `singledispatch` | Single-dispatch generic functions in `functools` |
| **PEP 450** | `statistics` module | Built-in statistical mathematical calculations |
| **PEP 454** | `tracemalloc` module | Trace memory allocations for debugging leaks |

---

## 💻 Pythonic Code Showcase

Check `main_3_4.py` in this directory for runnable code examples demonstrating:
- Object-oriented path operations with `pathlib.Path`
- Creating and using `enum.Enum` & `enum.auto`
- Polymorphic functions with `@singledispatch`
- Basic statistical operations with `statistics`
