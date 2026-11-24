# Python 3.10 Overview & Features

**Release Date:** October 4, 2021  
**Key Focus:** Structural Pattern Matching (`match`/`case`), Union Type Operator (`X | Y`), Precise Error Locations in Tracebacks, and `zip(..., strict=True)`.

---

## 🚀 Key Features & Syntax Additions

### 1. Structural Pattern Matching (`match` / `case`) (PEPs 634, 635, 636)
Introduced pattern matching via `match` and `case` statements, bringing robust pattern matching capabilities to Python:
- **Literal Matching**: `case 200:`
- **Sequence Unpacking**: `case [first, *rest]:`
- **Mapping Matching**: `case {"type": "user", "id": uid}:`
- **Class Pattern Matching**: `case Point(x=x, y=y):`
- **Guards**: `case val if val > 0:`
- **Wildcards & Or-patterns**: `case 401 | 403 | 404:`, `case _:`

### 2. Union Type Operator (`X | Y`) (PEP 604)
Allowed writing union types using the infix pipe operator `|` instead of `typing.Union`:
- `int | float` instead of `Union[int, float]`
- `str | None` instead of `Optional[str]`
- Works in both type annotations and `isinstance()` / `issubclass()` checks (`isinstance(x, int | str)`).

### 3. Parenthesized Context Managers (PEP 617 / Syntax)
Supported using enclosing parentheses across multi-line context manager statements, enabling cleaner multi-resource management without needing line continuation backslashes (`\`).

```python
with (
    open("input.txt") as input_file,
    open("output.txt", "w") as output_file,
):
    output_file.write(input_file.read())
```

### 4. Strict Length Verification for `zip()` (`strict=True`)
Added the `strict=True` keyword argument to `zip()`, raising a `ValueError` if the iterables being zipped are not of equal length.

### 5. Enhanced Error Messages & Precise Tracebacks
CPython 3.10 vastly improved syntax error reporting. Missing brackets, unclosed quotes, invalid keywords, or misspelled variable names now show pinpoint locations and helpful hints (e.g. *"Did you mean...?"*).

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 634/635/636** | `match` / `case` | Structural pattern matching specifications and tutorial |
| **PEP 604** | `X | Y` Union Operator | Alternative syntax for `typing.Union` & `isinstance` |
| **PEP 612** | `ParamSpec` | Parameter specification variables for callables |
| **PEP 613** | `TypeAlias` | Explicit type alias declarations |
| **PEP 604** | Pipe in `isinstance` | `isinstance(val, int | str)` runtime evaluation |

---

## 💻 Pythonic Code Showcase

Check `main_3_10.py` in this directory for runnable code examples demonstrating:
- Pattern matching HTTP response codes, commands, and data classes with `match`/`case`
- Using `int | str | None` in type annotations and `isinstance` checks
- Enforcing strict length checks using `zip(..., strict=True)`
- Utilizing explicit `TypeAlias` declarations
