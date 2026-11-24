# Python `*args` and `**kwargs` Master Guide

Welcome to the **`*args` and `**kwargs` Tutorial Module**. This guide comprehensively explains variable positional arguments, variable keyword arguments, dictionary unpacking, parameter ordering rules, and version evolution across Python releases.

---

## 1. What are `*args` and `**kwargs`?

In Python:
* **`*args`** (*Arbitrary Positional Arguments*): Allows a function to accept any number of positional arguments. Inside the function, `args` is received as a **`tuple`**.
* **`**kwargs`** (*Arbitrary Keyword Arguments*): Allows a function to accept any number of keyword (named) arguments. Inside the function, `kwargs` is received as a **`dict`**.

> The names `args` and `kwargs` are conventions; the asterisks (`*` and `**`) are what actually perform the unpacking / packing.

---

## 2. Parameter Ordering Rules

When defining functions that take multiple types of arguments, Python enforces a strict declaration order:

$$\text{Standard Positional} \longrightarrow \text{*args} \longrightarrow \text{Keyword-Only} \longrightarrow \text{**kwargs}$$

```python
def example(required_pos, *args, keyword_only="default", **kwargs):
    pass
```

### Unpacking at Call-Time
You can also unpack iterables into positional arguments and dictionaries into keyword arguments:
```python
numbers = [10, 20, 30]
average_score(*numbers)  # Unpacks list into positional arguments

details = {"brand": "Jack Daniels", "in_stock": True}
drinks_type("Whisky", 25.99, **details)  # Unpacks dictionary into kwargs
```

---

## 3. Module Overview

| File | Description | Core Concept |
| :--- | :--- | :--- |
| `ava_score.py` | Arithmetic mean calculation for variable inputs | `*args` numerical aggregation |
| `clients_plus_args.py` | Required parameters combined with extra tags | Fixed parameters + `*args` |
| `customer_kwargs.py` | Flexible customer metadata logging | Combined `*args` and `**kwargs` |
| `drink_type.py` | Mandatory parameters + arbitrary attributes | Fixed parameters + `**kwargs` |
| `alcohols.py` | Categorizing item names and properties | Flexible packing and iteration |
| `students.py` | Clean parameter naming and default arguments | Readability & keyword arguments |
| `test_kwargs.py` | Automated unit test suite (`unittest`) | Comprehensive test verification |

---

## 4. Introspection with `dir()`

Because `args` is a `tuple` and `kwargs` is a `dict`, you can inspect their available methods using `dir()`:

```python
def inspect_types(*args, **kwargs):
    print("Methods available on args (tuple):")
    print([m for m in dir(args) if not m.startswith("__")])
    # Output: ['count', 'index']

    print("Methods available on kwargs (dict):")
    print([m for m in dir(kwargs) if not m.startswith("__")])
    # Output: ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

---

## 5. Python Version Evolution

| Feature | Introduced / Changed In | Description |
| :--- | :--- | :--- |
| **Python 2.7** | Legacy | `*args` and `**kwargs` supported, but keyword-only parameters were not available without manual dictionary popping. |
| **Python 3.0+** | PEP 3102 | Added **Keyword-Only arguments** following a bare `*` or `*args`. |
| **Python 3.5** | PEP 448 | Additional Unpacking Generalizations — allow multiple `*args` and `**kwargs` in function calls: `func(*list1, *list2, **dict1, **dict2)`. |
| **Python 3.8** | PEP 570 | Added **Positional-Only arguments** syntax (`/`): `def func(pos_only, /, standard, *, kw_only): ...`. |
| **Python 3.12+** | Performance Tuning | Comprehensions and unpacking operations inlined at bytecode level for faster function calls and lower memory overhead. |

---

## 6. Running the Unit Tests

Execute the test suite from the repository root:

```bash
python3 -m unittest kwargs/test_kwargs.py
```
Expected output:
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
