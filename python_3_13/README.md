# Python 3.13 Overview & Features

**Release Date:** October 7, 2024  
**Key Focus:** Free-Threaded CPython (Experimental GIL Removal), Experimental JIT Compiler, Improved Interactive REPL, Type Narrowing (`TypeIs`), `ReadOnly`, and Default Type Parameters.

---

## 🚀 Key Features & Syntax Additions

### 1. Free-Threaded CPython / Experimental GIL Removal (PEP 703)
Introduced experimental support for building CPython with the Global Interpreter Lock (GIL) disabled (`--disable-gil`). This allows threads to run in true multi-threaded CPU parallel fashion across multiple CPU cores within the same interpreter process.

### 2. Copy-and-Patch Just-In-Time (JIT) Compiler (PEP 744)
Added an experimental JIT compiler to CPython. When enabled (`--enable-experimental-jit`), CPython compiles bytecode into machine code at runtime using a lightweight copy-and-patch JIT mechanism, yielding further performance speedups.

### 3. Modernized Interactive REPL
Replaced Python's standard interactive prompt with an enhanced terminal REPL based on PyPy's CLI interface:
- Multi-line code editing with syntax highlighting.
- Colorized tracebacks and interactive help menus.
- Dedicated paste mode (`F3` / `%paste`).
- Shell command navigation and improved history inspection.

### 4. Precise Type Narrowing (`typing.TypeIs`) (PEP 742)
Introduced `TypeIs` to replace `TypeGuard` for type narrowing predicate functions. `TypeIs` allows static type checkers to narrow types in both `if` (True) and `else` (False) branches symmetrically.

### 5. `TypeVar` Default Values (PEP 696)
Type variables and type parameters can now specify default types:
`type Vector[T = float] = list[T]` or `T = TypeVar("T", default=str)`.

### 6. Read-Only TypedDict Fields (`typing.ReadOnly`)
Added `ReadOnly[]` modifier to `TypedDict` key definitions to mark keys that cannot be modified or updated after dictionary creation.

### 7. SQLite3 DBM Backend (`dbm.sqlite3`)
Added `dbm.sqlite3` as a standard portable key-value storage backend built on top of SQLite3.

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 703** | Free-Threaded CPython | Experimental build option to run without the GIL |
| **PEP 744** | JIT Compiler | Experimental copy-and-patch JIT compiler for CPython |
| **PEP 742** | `typing.TypeIs` | Precise symmetric type narrowing predicates |
| **PEP 696** | TypeVar Defaults | Default types for generic type parameters |
| **PEP 702** | `@warnings.deprecated` | Standard decorator to mark functions/classes as deprecated |

---

## 💻 Pythonic Code Showcase

Check `main_3_13.py` in this directory for runnable code examples demonstrating:
- Precise type narrowing predicates using `TypeIs`
- Generic type parameter defaults (`TypeVar` defaults)
- Read-only schema definitions using `TypedDict` and `ReadOnly`
- Deprecation warnings using `@warnings.deprecated`
- Free-threading and JIT architecture overview
