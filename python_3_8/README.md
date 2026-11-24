# Python 3.8 Overview & Features

**Release Date:** October 14, 2019  
**Key Focus:** Assignment Expressions (Walrus Operator `:=`), Positional-Only Parameters (`/`), F-String Debugging (`f"{var=}"`), Typing Extensions (`TypedDict`, `Literal`, `Final`, `Protocol`), and Math Utilities.

---

## 🚀 Key Features & Syntax Additions

### 1. Assignment Expressions / Walrus Operator (`:=`) (PEP 572)
Introduced the `:=` operator ("walrus operator"), allowing assignment of values to variables inside expressions (e.g. in `if` conditions, `while` loops, and list comprehensions), avoiding duplicate evaluations.

### 2. Positional-Only Parameters (`/`) (PEP 570)
Added `/` syntax in function definitions to specify parameters that MUST be passed positionally and cannot be used as keyword arguments.
- Example: `def func(p1, p2, /, positional_or_keyword, *, keyword_only): ...`

### 3. F-String Debugging Specifier `f"{expr=}"`
F-strings now support the `=` specifier, expanding an expression to its text representation followed by its evaluated value.
- `f"{x=}"` produces `'x=42'`
- Greatly simplifies logging and interactive print debugging.

### 4. Advanced Type System Enhancements
- **`TypedDict` (PEP 589)**: Specify fixed key-value type structures for regular dictionaries.
- **`Literal` Types (PEP 586)**: Restrict variables or function arguments to specific literal values (e.g. `Literal['r', 'w', 'a']`).
- **`Final` & `@final` (PEP 591)**: Declare constants or prevent class inheritance / method overriding.
- **`Protocol` (PEP 544)**: Structural subtyping (duck typing) support for static type checkers.

### 5. Mathematical & Standard Library Updates
- **`math.prod()`**: Compute the product of elements in an iterable.
- **`math.isqrt()`**: Integer square root calculation.
- **`shutil.copytree()`**: Added `dirs_exist_ok=True` parameter to allow merging directories without errors.
- **`multiprocessing.shared_memory`**: Shared memory support across independent processes.

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 572** | Walrus Operator (`:=`) | In-expression variable assignment |
| **PEP 570** | Positional-Only Parameters (`/`) | Function parameter enforcement |
| **PEP 589** | `TypedDict` | Type hints for dictionary structures |
| **PEP 586** | `Literal` Types | Restrict values to explicit literals |
| **PEP 591** | `Final` / `@final` | Prevent re-assignment, subclassing, or overriding |
| **PEP 544** | `Protocol` | Structural subtyping (duck typing type hints) |

---

## 💻 Pythonic Code Showcase

Check `main_3_8.py`, `walrus.py`, and `walrus_list.py` in this directory for runnable code examples demonstrating:
- In-expression filtering and looping using the Walrus operator (`:=`)
- Positional-only parameter enforcement using `/`
- Quick debugging prints with `f"{variable=}"`
- Defining structured schema types with `TypedDict` and `Protocol`
- Efficient product computation using `math.prod()`
