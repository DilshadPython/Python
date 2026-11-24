# Master Guide: Python Decorators

> **Module**: `decorator/`  
> **Topic**: Higher-order functions, closures, syntax sugar (`@`), metadata preservation (`functools.wraps`), and parameterized decorators.

---

## Table of Contents
1. [Core Principles](#1-core-principles)
2. [Anatomy of a Decorator](#2-anatomy-of-a-decorator)
3. [Preserving Function Metadata with functools.wraps](#3-preserving-function-metadata-with-functoolswraps)
4. [Parameterized Decorators (Decorator Factories)](#4-parameterized-decorators-decorator-factories)
5. [Class Decorators and __call__](#5-class-decorators-and-__call__)
6. [Python Version Evolution](#6-python-version-evolution)
7. [Unit Testing and Verification](#7-unit-testing-and-verification)

---

## 1. Core Principles

Decorators wrap a target function to extend its behavior without modifying the function itself. They leverage two fundamental Python features:
1. **First-class functions**: Functions can be passed as arguments, assigned to variables, and returned from other functions.
2. **Closures**: Inner functions retain access to variables in their enclosing outer scope even after the outer function finishes executing.

---

## 2. Anatomy of a Decorator

```python
import functools
import time

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)  # Call original function
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] took {elapsed:.4f}s")
        return result                  # Return original result
    return wrapper

@timing_decorator
def process_data(items):
    return sum(items)
```

---

## 3. Preserving Function Metadata with `functools.wraps`

Without `@functools.wraps(func)`, the decorated function loses its identity:
- `func.__name__` becomes `"wrapper"`
- `func.__doc__` becomes the wrapper's docstring
- Type hints and introspection (`inspect.signature`) are replaced

Always use `@functools.wraps(func)` inside the decorator definition.

---

## 4. Parameterized Decorators (Decorator Factories)

When a decorator needs arguments, define a 3-level nested structure:

```python
import functools

def retry(max_attempts: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    if attempt == max_attempts:
                        raise exc
                    print(f"Attempt {attempt} failed, retrying...")
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_network_call():
    ...
```

---

## 5. Class Decorators and `__call__`

Classes can also act as decorators by implementing the `__call__` dunder method:

```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)
```

---

## 6. Python Version Evolution

| Version | Enhancement | Notes |
| :--- | :--- | :--- |
| **Python 2.4** | PEP 318 | Function decorators introduced (`@` syntax). |
| **Python 2.5** | `functools.wraps` | Standard library helper added to automate wrapper metadata copying. |
| **Python 2.6 / 3.0** | PEP 3129 | Class decorators introduced (`@decorator` above `class MyClass:`). |
| **Python 3.9** | PEP 614 | Relaxed decorator syntax: any valid expression can be used as a decorator. |

---

## 7. Unit Testing and Verification

Run the test suite in the repository root:
```bash
python3 -m unittest decorator/test_decorator.py
```
