# Python 3.12 Overview & Features

**Release Date:** October 2, 2023  
**Key Focus:** Formalized Type Parameter Syntax (`type` statement), Formalized F-String Syntax (PEP 701), Per-Interpreter GIL (PEP 684), `@override` Decorator, and Improved Error Diagnostics.

---

## 🚀 Key Features & Syntax Additions

### 1. Syntactic Support for Type Parameter Lists (`type` statement) (PEP 695)
Introduced clean, first-class syntax for generic classes, generic functions, and type aliases without needing explicit `TypeVar` instantiations:
- **Generic Type Alias**: `type Matrix[T] = list[list[T]]`
- **Generic Function**: `def max_item[T: Comparable](items: list[T]) -> T:`
- **Generic Class**: `class Stack[T]: ...`

### 2. Formalized F-String Syntax (PEP 701)
Lifted all historical syntactic restrictions on F-strings:
- **Quote Reuse**: Quotes used inside expressions can now match outer quotes: `f"User: {data['name']}"`
- **Backslashes Inside Expressions**: Backslashes and inline escape sequences are allowed: `f"Joined: {'\n'.join(lines)}"`
- **Arbitrary Nesting**: F-strings can be nested inside other f-strings without limits.
- **Multi-line Inline Expressions & Comments**: Comments (`#`) can be included inside expressions inside f-strings.

### 3. Per-Interpreter GIL / Isolated Sub-interpreters (PEP 684)
CPython can now create multiple sub-interpreters with individual, isolated Global Interpreter Locks (GILs). This enables true multi-core CPU parallelism in CPython when running across multiple sub-interpreters.

### 4. `@override` Decorator in `typing` (PEP 698)
Added `@override` decorator to explicitly signal that a method in a subclass is intended to override a parent class method. Static type checkers (like Mypy) will flag an error if the method does NOT actually override anything.

### 5. Immortal Objects (PEP 683)
Objects can now be marked as "immortal", bypassing reference counting and garbage collection passes (e.g. `None`, `True`, `False`, small integers, static code objects). This reduces cache line invalidation and accelerates multi-process memory sharing.

### 6. Cleaned Batteries / Deprecations (PEP 594)
Removed legacy modules including `distutils`, `imp`, `asynchat`, `asyncore`, `smtpd`, `nntplib`, and `telnetlib`.

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 695** | `type` Syntax | First-class generic parameter lists & type alias syntax |
| **PEP 701** | Formalized F-Strings | Quotes reuse, backslashes, arbitrary nesting, inline comments |
| **PEP 684** | Per-Interpreter GIL | Isolated GIL per sub-interpreter for parallel execution |
| **PEP 698** | `@override` Decorator | Static type checking for overridden methods |
| **PEP 683** | Immortal Objects | Bypasses reference counts for static core runtime objects |

---

## 💻 Pythonic Code Showcase

Check `main_3_12.py` in this directory for runnable code examples demonstrating:
- Defining generic type aliases using the `type` statement
- Writing nested f-strings with quote reuse and backslashes
- Using `@override` for clean object-oriented class inheritance
- Leveraging improved error diagnostics
