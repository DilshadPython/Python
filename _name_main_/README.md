# Python `if __name__ == '__main__':` Master Guide

Welcome to the **`_name_main_` Tutorial Module**. This guide explains one of the most fundamental concepts in Python: the special built-in `__name__` variable and the `if __name__ == '__main__':` execution guard.

---

## 1. What is `__name__` in Python?

Every Python module has a built-in string variable named `__name__`. The Python interpreter automatically assigns its value depending on **how the file is being executed**:

| Execution Mode | Value of `__name__` | Description |
| :--- | :--- | :--- |
| **Direct Execution** (`python3 script.py`) | `"__main__"` | The file is the top-level script being run directly by the user. |
| **Imported as Module** (`import script`) | `"script"` (or package path) | The file is being imported by another Python file. |

---

## 2. Why Use `if __name__ == '__main__':`?

When a Python file is imported, the interpreter **executes all top-level statements** from top to bottom. 

Without the `if __name__ == '__main__':` guard:
* Any code, tests, or print statements sitting outside functions will **run automatically as soon as another file imports it**.
* Functions, classes, and variables cannot be cleanly reused in other scripts.

With the guard:
```python
def calculate_tax(amount: float) -> float:
    return amount * 0.20

# This block ONLY runs when executed directly: python3 tax.py
# If another script does: `from tax import calculate_tax`, this block is SKIPPED!
if __name__ == "__main__":
    print(f"Direct test: {calculate_tax(100.0)}")
```

---

## 3. Module Overview

| File | Description | Core Concept |
| :--- | :--- | :--- |
| `_name_.py` | Demonstrates reading `__name__` directly | Inspecting the special variable |
| `_main_.py` | Reusable function invoked under the main guard | Safe function execution pattern |
| `myfile.py` | Helper module designed to be imported | Demonstrating module-level `__name__` |
| `yourfile.py` | Imports `myfile.py` and compares `__name__` values | Contrasting imported vs direct names |
| `main.py` | Safe environment variable access via `os.getenv` | Script entry points and best practices |
| `test_name_main.py` | Automated unit test suite (`unittest`) | Validating import contexts and return values |

---

## 4. Practical Demonstration

### When running `myfile.py` directly:
```bash
python3 _name_main_/myfile.py
```
Output:
```text
This file is 'myfile'. Current __name__ is: '__main__'
```

### When running `yourfile.py` (which imports `myfile.py`):
```bash
python3 _name_main_/yourfile.py
```
Output:
```text
Running 'yourfile' as main script.
Current script __name__:         '__main__'
Imported myfile.__name__:        'myfile'
```

Notice that `myfile` retains its module name (`'myfile'`) when imported, while `yourfile` becomes `'__main__'` because it was the script passed to Python!

---

## 5. Running the Unit Tests

Execute the test suite from the repository root:

```bash
python3 -m unittest _name_main_/test_name_main.py
```
Expected output:
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
