# Python Attributes & Methods Master Guide (`attribut_and_methods`)

Welcome to the **Python Attributes & Methods Master Guide**, a production-grade educational tutorial and reference detailing instance attributes, class attributes, instance/class/static methods, `@property` getters/setters, custom descriptors (`__get__`, `__set__`, `__set_name__`), attribute access interception (`__getattribute__`, `__getattr__`, `__setattr__`), memory optimization (`__slots__`), unit testing via `unittest`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Attribute Lookup Resolution Order](#-overview--attribute-lookup-resolution-order)
2. [Attribute & Method Classification Matrix](#-attribute--method-classification-matrix)
3. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
4. [Directory Structure & Module Overview](#-directory-structure--module-overview)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 📁 Overview & Attribute Lookup Resolution Order

In Python, **everything is an object**. Attributes store state (variables), while methods represent behavior (functions bound to objects).

### The Attribute Lookup Resolution Algorithm

When evaluating `obj.attribute_name`, Python executes the following 6-step resolution order:

```text
1. obj.__getattribute__('attribute_name') is invoked.
2. Check Class MRO for a Data Descriptor (defines __get__ AND __set__).
3. Check Instance __dict__ for 'attribute_name'.
4. Check Class MRO for a Non-Data Descriptor (defines ONLY __get__).
5. Check Class __dict__ across MRO for raw attribute or function.
6. Fallback to obj.__getattr__('attribute_name') if not found.
```

---

## 📊 Attribute & Method Classification Matrix

| Category | Decorator / Syntax | First Parameter | Scope & Use Case |
| :--- | :--- | :--- | :--- |
| **Instance Attribute** | `self.attr = value` | N/A | Unique state bound to specific instance object |
| **Class Attribute** | `CLASS_ATTR = value` | N/A | Shared state bound across all class instances |
| **Instance Method** | `def method(self):` | `self` | Operates on specific instance data and state |
| **Class Method** | `@classmethod` | `cls` | Operates on class namespace; factory constructors |
| **Static Method** | `@staticmethod` | None | Utility functions bound to class namespace |
| **Property Descriptor**| `@property` | `self` | Managed attribute access via getters/setters |
| **Custom Descriptor** | `__get__` / `__set__` | `self, instance, owner` | Reusable attribute validation & storage engines |

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_attributes_methods.py`](file:///home/monika/PycharmProjects/Devel/Python/attribut_and_methods/beginner_attributes_methods.py))
Focuses on fundamental instance attributes, instance methods, built-in type methods, and basic dunders:
- **Instance Attributes**: `self.title`, `self.author`.
- **Instance Methods**: `def get_summary(self):`.
- **Built-in Type Methods**: `str.strip()`, `list.append()`, `dict.get()`.
- **Basic Dunders**: `__init__`, `__str__`, `__len__`.

```python
# Beginner Example: Instance attributes & methods
class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages
```

---

### 🚀 Intermediate Level ([`intermediate_attributes_methods.py`](file:///home/monika/PycharmProjects/Devel/Python/attribut_and_methods/intermediate_attributes_methods.py))
Focuses on classmethods, staticmethods, property getters/setters, and dynamic reflection built-in functions:
- **Classmethods**: `@classmethod` factory methods.
- **Staticmethods**: `@staticmethod` utility functions.
- **Property Descriptors**: `@property` and `@balance.setter`.
- **Dynamic Reflection**: `getattr()`, `setattr()`, `hasattr()`, `delattr()`, `dir()`.

```python
# Intermediate Example: Property getter & setter
@property
def balance(self) -> float:
    return self._balance

@balance.setter
def balance(self, value: float) -> None:
    if value < 0:
        raise ValueError("Balance cannot be negative")
    self._balance = value
```

---

### 🔥 Senior Level ([`senior_attributes_methods.py`](file:///home/monika/PycharmProjects/Devel/Python/attribut_and_methods/senior_attributes_methods.py))
Focuses on custom Data Descriptors (PEP 487), attribute access interception hooks, memory optimization via `__slots__`, and callable objects (`__call__`):
- **Custom Descriptors**: Class implementing `__get__`, `__set__`, `__set_name__`.
- **Attribute Interception**: `__getattribute__` and `__getattr__` fallback.
- **Memory Optimization**: `__slots__ = ('attr1', 'attr2')` to prevent `__dict__` overhead.
- **Callable Objects**: `__call__` allowing objects to be invoked like functions.

```python
# Senior Example: Custom Descriptor with PEP 487 __set_name__
class ValidatedString:
    def __set_name__(self, owner, name):
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name, "")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Must be string")
        setattr(instance, self.storage_name, value)
```

---

## 📁 Directory Structure & Module Overview

```text
attribut_and_methods/
├── README.md                           # Master tutorial documentation and multi-tier guide
├── test_attributes_methods.py          # Multi-tier unit test suite
├── attribute_method_inspector.py       # Core inspector engine class
├── beginner_attributes_methods.py      # Beginner tier (instance attrs, methods, str/len dunders)
├── intermediate_attributes_methods.py  # Intermediate tier (classmethod, staticmethod, properties)
└── senior_attributes_methods.py        # Senior tier (descriptors, __slots__, __getattr__, __call__)
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_attributes_methods.py` | 🌱 Beginner | `self.attr`, instance methods, `str.strip()`, `__init__`, `__str__`, `__len__` |
| `intermediate_attributes_methods.py` | 🚀 Intermediate | `@classmethod`, `@staticmethod`, `@property`, `getattr()`, `setattr()` |
| `senior_attributes_methods.py` | 🔥 Senior | Data Descriptors (`__set_name__`), `__slots__`, `__getattr__`, `__call__` |
| `attribute_method_inspector.py` | All Tiers | `AttributeMethodInspector.inspect_object()`, resolution path lookup |
| `test_attributes_methods.py` | All Tiers | `unittest` suite verifying attributes and methods across all tiers |

---

## 🚀 How to Run the Code

```bash
# Run core attribute & method inspector engine
python3 attribut_and_methods/attribute_method_inspector.py

# Run beginner tier examples
python3 attribut_and_methods/beginner_attributes_methods.py

# Run intermediate tier examples
python3 attribut_and_methods/intermediate_attributes_methods.py

# Run senior tier examples
python3 attribut_and_methods/senior_attributes_methods.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_attributes_methods.py

# Run with pytest from repository root
pytest attribut_and_methods/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Attributes & Methods Evolution | Syntax & System Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Unbound method objects vs bound methods | Class method lookup returned `unbound method` objects; required inheriting `(object)`. | Old-style classes lacked descriptors and property support. |
| **Python 3.0** | Unbound methods removed | Method lookup on class returns plain function objects. | Classes inherit from `object` implicitly by default. |
| **Python 3.3** | Added `__qualname__` attribute | Class and method objects gain `__qualname__` for nested class path reflection. | Previously only `.func_name` / `__name__` existed. |
| **Python 3.6** | PEP 487 `__set_name__` descriptor hook | Descriptors automatically receive attribute name via `__set_name__(owner, name)`. | Required explicit string naming in descriptor `__init__`. |
| **Python 3.8** | Positional-only parameter `/` syntax | Method signatures support positional-only arguments `def func(a, /, b):`. | Required manual parameter checking in Python 2.7-3.7. |
| **Python 3.10**| Pattern matching on class attributes | Structural pattern matching evaluates class attribute instances (`match obj:`). | Required nested `isinstance()` checks in Python 2.7-3.9. |
| **Python 3.12**| Generic type parameters (`__type_params__`) | Classes and methods expose type parameter generics via `__type_params__`. | Typing annotations introduced in 3.5 lacked runtime reflection. |
| **Python 3.13**| Free-threaded GIL-free attribute lookup | Optimized atomic attribute lock-free lookups across threads. | GIL lock guarded attribute dict modifications in 2.7-3.12. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Inspecting methods and attributes on `range()` objects demonstrates Python method introspection:

```python
# Inspecting range attributes using dir(range)
r = range(0, 10, 2)
print("Attributes & Methods on range():", [m for m in dir(r) if not m.startswith("__")])
print(f"start={r.start}, stop={r.stop}, step={r.step}")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Evaluating sequence containment `500 in range(0, 1000, 5)` computes in constant-time arithmetic evaluation without allocating memory arrays.

### Attributes and Methods Inspection (`dir(range)`)

Public methods and attributes available on `range`:
- **`start`**: Integer start value of range sequence.
- **`stop`**: Integer stop boundary of range sequence.
- **`step`**: Step increment integer.
- **`index(x)`**: Returns zero-based index of item $x$ in range ($O(1)$ computation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
