# Python Decorators Master Guide

Welcome to the **Python Decorators Tutorial Module**. This guide explains higher-order functions, closures, syntax sugar (`@decorator`), function metadata preservation (`functools.wraps`), and common real-world decorator applications.

---

## 1. What is a Decorator?

In Python, a **decorator** is a design pattern and language feature that allows you to modify or extend the behavior of a function or method without altering its actual source code.

Functions in Python are **first-class citizens**, meaning they can be:
1. Passed as arguments to other functions.
2. Returned as values from functions.
3. Assigned to variables.

A decorator is simply a function that takes another function as input, extends its behavior within a wrapper closure, and returns the wrapper function.

```python
# The @decorator syntax is syntactic sugar for:
def greet():
    print("Hello")

greet = decorator(greet)

# Which is identical to:
@decorator
def greet():
    print("Hello")
```

---

## 2. Why Use `functools.wraps`?

When a function is wrapped by a decorator, its metadata (`__name__`, `__doc__`, annotations) is replaced by the wrapper function's metadata unless preserved. 

Using `@functools.wraps(func)` copies over the original function's name and docstring:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves func.__name__ and func.__doc__
    def wrapper(*args, **kwargs):
        """Wrapper docstring."""
        return func(*args, **kwargs)
    return wrapper
```

---

## 3. Module Overview

| File | Description | Core Concept |
| :--- | :--- | :--- |
| `calculate_time.py` | Accurate benchmark decorator using `time.perf_counter` | Performance timing & wrapper returns |
| `collect_time.py` | Wall-clock timestamp logging (`time.strftime`) | Entry and exit event logging |
| `deco.py` | Baseline manual timing code | Why decorators reduce repetition |
| `make_chocolate.py` | Beverage timing with `datetime` and `timedelta` | Time arithmetic inside decorated calls |
| `make_coffe.py` | Parameterized beverage brewing decorator | Forwarding typed arguments |
| `make_tea.py` | Steeping timer and future timestamp reporting | Combining closures with return values |
| `test_decorator.py` | Automated unit test suite (`unittest`) | Testing wrappers, metadata, and closures |

---

## 4. Parameterized Decorators (Decorators Taking Arguments)

To pass parameters to the decorator itself (e.g., `@repeat(num_times=3)`), add an outer factory function:

```python
import functools

def repeat(num_times: int = 2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def ping():
    print("Ping!")
```

---

## 5. Python Version History for Decorators

| Version | Feature | Impact |
| :--- | :--- | :--- |
| **Python 2.4** | PEP 318 | Function decorators introduced using the `@` prefix syntax. |
| **Python 2.5** | `functools.wraps` | Standard library helper added to automate metadata copying. |
| **Python 2.6 / 3.0** | PEP 3129 | Class decorators introduced: `@decorator` above `class MyClass: ...`. |
| **Python 3.9** | PEP 614 | Relaxed decorator grammar: allows any valid expression (e.g. `buttons[0].clicked(func)`). |

---

## 6. Running the Unit Tests

Execute the test suite from the repository root:

```bash
python3 -m unittest decorator/test_decorator.py
```
Expected output:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.050s

OK
```
