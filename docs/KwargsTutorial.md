# Master Guide: Python `*args` and `**kwargs`

> **Module**: `kwargs/`  
> **Topic**: Variadic function arguments (`*args`), arbitrary keyword arguments (`**kwargs`), parameter unpacking, and modern Python signature conventions.

---

## Table of Contents
1. [Core Principles](#1-core-principles)
2. [Function Definition & Calling Syntax](#2-function-definition--calling-syntax)
3. [Parameter Ordering Rules](#3-parameter-ordering-rules)
4. [Unpacking Operators (* and **)](#4-unpacking-operators--and-)
5. [Introspection with dir()](#5-introspection-with-dir)
6. [Python Version Evolution (2.7 to 3.13)](#6-python-version-evolution-27-to-313)
7. [Unit Testing and Verification](#7-unit-testing-and-verification)

---

## 1. Core Principles

Python functions can accept dynamic numbers of arguments using the unpacking prefix operators:
- `*args` packs extra positional arguments into an immutable `tuple`.
- `**kwargs` packs extra named arguments into a mutable `dict`.

```python
def example(*args, **kwargs):
    print(type(args))    # <class 'tuple'>
    print(type(kwargs))  # <class 'dict'>
```

---

## 2. Function Definition & Calling Syntax

### 2.1 Positional Aggregation with `*args`
```python
def average_score(*scores: float) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

print(average_score(80, 90, 100))  # 90.0
```

### 2.2 Arbitrary Keyword Aggregation with `**kwargs`
```python
def register_customer(name: str, **attributes):
    print(f"Customer: {name}")
    for key, value in attributes.items():
        print(f"  {key}: {value}")

register_customer("Alice", tier="Gold", city="London", discount=0.15)
```

---

## 3. Parameter Ordering Rules

Python strictly enforces the order in which parameters are defined:

```text
def func(
    pos_only_1, pos_only_2, /,   # PEP 570 Positional-only (Python 3.8+)
    standard_pos_or_kw,          # Standard positional or keyword
    *args,                       # Variadic positional (tuple)
    kw_only_1, kw_only_2=None,   # PEP 3102 Keyword-only (Python 3.0+)
    **kwargs                     # Variadic keyword (dict)
):
    ...
```

---

## 4. Unpacking Operators (`*` and `**`)

Beyond function signatures, `*` and `**` unpack data structures into function calls:

```python
numbers = [10, 20, 30]
average_score(*numbers)  # Unpacks list into positional arguments

config = {"brand": "Jack Daniels", "in_stock": True}
drinks_type("Whisky", 25.99, **config)  # Unpacks dict into keyword arguments
```

---

## 5. Introspection with `dir()`

Because `args` is a `tuple` and `kwargs` is a `dict`, standard container methods are available:

- `args`: `args.count(x)`, `args.index(x)`, `len(args)`
- `kwargs`: `kwargs.keys()`, `kwargs.values()`, `kwargs.items()`, `kwargs.get(k, default)`

```python
def inspect_containers(*args, **kwargs):
    print("Tuple methods:", [m for m in dir(args) if not m.startswith("_")])
    print("Dict methods: ", [m for m in dir(kwargs) if not m.startswith("_")])
```

---

## 6. Python Version Evolution (2.7 to 3.13)

| Version | Enhancement | Notes |
| :--- | :--- | :--- |
| **Python 2.7** | Classic unpacking | Keyword-only arguments required manually popping from `**kwargs`. |
| **Python 3.0** | PEP 3102 | Bare `*` in parameter list creates explicit **Keyword-Only arguments**. |
| **Python 3.5** | PEP 448 | Generalized unpacking allows multiple `*args` and `**kwargs` in a single call. |
| **Python 3.8** | PEP 570 | Added positional-only argument marker (`/`). |
| **Python 3.12+**| Inlined bytecode | Function call overhead for variadic arguments optimized with specialized bytecode instructions. |

---

## 7. Unit Testing and Verification

Run the test suite in the repository root:
```bash
python3 -m unittest kwargs/test_kwargs.py
```
