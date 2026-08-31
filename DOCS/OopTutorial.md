# Python Object-Oriented Programming (OOP) & Architecture Guide

Welcome to the **Python Object-Oriented Programming (OOP) Master Guide**, a comprehensive, production-grade technical and pedagogical reference. This document covers fundamental and advanced OOP concepts, CPython internal mechanics, design patterns, performance optimizations, all OOP attribute and method types, and version-by-version behavioral evolutions from Python 2.7 to Python 3.13.

---

## Table of Contents

1. [Overview & Core OOP Principles](#1-overview--core-oop-principles)
2. [Class vs. Instance Attributes & Namespace Mechanics](#2-class-vs-instance-attributes--namespace-mechanics)
3. [Attributes & Reflection APIs (`dir`, `getattr`, `setattr`, `hasattr`, `delattr`)](#3-attributes--reflection-apis-dir-getattr-setattr-hasattr-delattr)
4. [Method Types & Decorators (`self`, `@classmethod`, `@staticmethod`, `@property`, `@abstractmethod`)](#4-method-types--decorators-self-classmethod-staticmethod-property-abstractmethod)
5. [Constructors, Object Creation (`__new__` vs `__init__`)](#5-constructors-object-creation-__new__-vs-__init__)
6. [Encapsulation, Name Mangling & Property Descriptors](#6-encapsulation-name-mangling--property-descriptors)
7. [Inheritance Hierarchy & `super()` Delegation](#7-inheritance-hierarchy--super-delegation)
8. [Multiple Inheritance & Method Resolution Order (MRO)](#8-multiple-inheritance--method-resolution-order-mro)
9. [Polymorphism & Duck Typing Interfaces](#9-polymorphism--duck-typing-interfaces)
10. [Composition vs. Inheritance ("Has-A" vs. "Is-A")](#10-composition-vs-inheritance-has-a-vs-is-a)
11. [Special Dunder Methods & Operator Overloading](#11-special-dunder-methods--operator-overloading)
12. [Abstract Base Classes (`abc.ABC`) & Structural Subtyping](#12-abstract-base-classes-abc--structural-subtyping)
13. [Memory Optimization with `__slots__`](#13-memory-optimization-with-__slots__)
14. [Python Version Evolution Breakdown (Python 2.7 & Python 3.3 ➔ Python 3.13)](#14-python-version-evolution-breakdown-python-27--python-33--python-313)
15. [Range Sequence Performance & Reflection (`dir(range)`)](#15-range-sequence-performance--reflection-dirrange)

---

## 1. Overview & Core OOP Principles

Object-Oriented Programming in Python centers on modeling real-world entities through **Classes** (blueprints defining attributes and methods) and **Instances** (concrete objects created from blueprints). 

The 4 core pillars of OOP in Python are:
- **Encapsulation**: Hiding internal implementation state and exposing controlled interfaces (`@property`, private attributes `__balance`).
- **Abstraction**: Concealing complex reality behind simple abstract contracts (`abc.ABC`, `@abstractmethod`).
- **Inheritance**: Deriving new classes from existing parent classes to promote code reuse (`class Dog(Mammal)`).
- **Polymorphism**: Interfacing with different underlying object types through a uniform method signature (Duck Typing).

---

## 2. Class vs. Instance Attributes & Namespace Mechanics

Attributes in Python reside inside namespace dictionaries (`__dict__`):
- **Class Attributes**: Defined directly inside the class body. Shared across all instances of that class (`CompanyEmployee.total_employees`).
- **Instance Attributes**: Bound to specific object instances inside `__init__` via `self.attr`.

```python
class CompanyEmployee:
    company_name = "TechCorp Solutions"  # Shared Class Attribute
    total_employees = 0

    def __init__(self, name: str, salary: float):
        self.name = name                 # Instance Attribute
        self.salary = salary             # Instance Attribute
        CompanyEmployee.total_employees += 1
```

> [!NOTE]
> When accessing `instance.attr`, Python first searches `instance.__dict__`. If not found, it traverses `Class.__dict__` and then parent classes via MRO. Shadowing occurs if an instance assigns to a class attribute name (`emp.company_name = "New Co"`), creating a new local key in `instance.__dict__`.

---

## 3. Attributes & Reflection APIs (`dir`, `getattr`, `setattr`, `hasattr`, `delattr`)

Python provides dynamic attribute reflection and manipulation APIs for inspecting and altering class and instance namespaces at runtime:

| API Function | Description & Syntax | Usage Example |
| :--- | :--- | :--- |
| `dir(obj)` | Returns list of all valid attribute names, methods, and dunders on `obj` | `attrs = [a for a in dir(emp) if not a.startswith("__")]` |
| `getattr(obj, name, default)` | Dynamically fetches attribute value by string name | `salary = getattr(emp, "salary", 0.0)` |
| `setattr(obj, name, val)` | Dynamically assigns attribute value by string name | `setattr(emp, "department", "Engineering")` |
| `hasattr(obj, name)` | Checks if attribute string exists on instance or class | `if hasattr(emp, "salary"): print("Has Salary")` |
| `delattr(obj, name)` | Dynamically removes attribute from instance `__dict__` | `delattr(emp, "temporary_tag")` |
| `vars(obj)` / `obj.__dict__` | Accesses raw namespace dictionary mapping attributes to values | `print(vars(emp))` |

---

## 4. Method Types & Decorators (`self`, `@classmethod`, `@staticmethod`, `@property`, `@abstractmethod`)

Python OOP supports 5 distinct method types depending on parameter binding and scope:

1. **Instance Methods (`self`)**: Bound to instance objects. Receives `self` as first argument to access/modify instance state.
2. **Class Methods (`@classmethod`)**: Bound to class objects. Receives `cls` as first argument; used for factory constructors (`cls.from_dict(...)`).
3. **Static Methods (`@staticmethod`)**: Unbound utility functions grouped inside class namespace; receives neither `self` nor `cls`.
4. **Property Descriptors (`@property`)**: Encapsulates getter, setter, and deleter methods with validation guards.
5. **Abstract Methods (`@abstractmethod`)**: Enforces implementation contracts across subclasses.

```python
import abc
from typing import Dict, Any

class TemperatureConverter(abc.ABC):
    unit_system: str = "Metric / Imperial"

    def __init__(self, celsius: float):
        self._celsius = float(celsius)

    # 1. Property Getter & Setter
    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible")
        self._celsius = float(value)

    # 2. Class Method Factory Constructor
    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "TemperatureConverter":
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    # 3. Static Method Utility
    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        return celsius + 273.15

    # 4. Abstract Method Interface
    @abc.abstractmethod
    def format_display(self) -> str:
        pass
```

---

## 5. Constructors, Object Creation (`__new__` vs `__init__`)

Object creation in Python is a two-step process:
1. **`__new__(cls, ...)`**: The static allocator method that creates and returns a new instance of `cls`.
2. **`__init__(self, ...)`**: The initializer method that populates instance state after creation.

```python
class Vehicle:
    def __init__(self, make: str, model: str, year: int, odometer: float = 0.0):
        if year < 1886:
            raise ValueError("Invalid vehicle manufacturing year")
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def drive(self, distance: float) -> float:
        self.odometer += distance
        return self.odometer
```

---

## 6. Encapsulation, Name Mangling & Property Descriptors

Python relies on naming conventions and language mechanisms for encapsulation:

- **Public**: `self.name` (Accessible everywhere)
- **Protected**: `self._account_type` (Convention indicating internal implementation detail)
- **Private**: `self.__balance` (Triggers CPython **Name Mangling** to `_ClassName__balance`)

```python
class BankAccountSecure:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance  # Mangled to _BankAccountSecure__balance

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
```

---

## 7. Inheritance Hierarchy & `super()` Delegation

Inheritance allows a child class to inherit attributes and methods from parent classes. Using `super()` ensures cooperative method calls and proper parent initialization.

```python
class Animal:
    def __init__(self, species: str):
        self.species = species

class Mammal(Animal):
    def __init__(self, species: str, fur_color: str):
        super().__init__(species)
        self.fur_color = fur_color

class Dog(Mammal):
    def __init__(self, name: str, breed: str, fur_color: str):
        super().__init__("Canine", fur_color)
        self.name = name
        self.breed = breed
```

---

## 8. Multiple Inheritance & Method Resolution Order (MRO)

Python supports multiple inheritance using the **C3 Linearization Algorithm** to construct the Method Resolution Order (MRO). This eliminates ambiguity in diamond-shaped inheritance graphs.

```python
class Device:
    def turn_on(self): return "Device powering on"

class Camera(Device):
    def turn_on(self): return f"Camera lens opening -> {super().turn_on()}"

class Phone(Device):
    def turn_on(self): return f"Phone screen lighting -> {super().turn_on()}"

class SmartPhone(Camera, Phone):
    def turn_on(self): return f"SmartPhone Booting: [{super().turn_on()}]"

print(SmartPhone.mro())
# [<class 'SmartPhone'>, <class 'Camera'>, <class 'Phone'>, <class 'Device'>, <class 'object'>]
```

---

## 9. Polymorphism & Duck Typing Interfaces

Python embraces **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."* Functions accept any object implementing the required interface method without requiring explicit inheritance.

```python
class PDFReport:
    def render(self) -> str: return "Rendering PDF Layout"

class HTMLReport:
    def render(self) -> str: return "Rendering HTML Layout"

class JSONReport:
    def render(self) -> str: return '{"type": "JSONReport"}'

def render_document(report_object) -> str:
    return report_object.render()  # Polymorphic dispatch
```

---

## 10. Composition vs. Inheritance ("Has-A" vs. "Is-A")

- **Inheritance ("Is-A")**: Tightly couples child and parent classes.
- **Composition ("Has-A")**: Builds complex objects by combining independent, modular components (e.g. `Car` has an `Engine`).

```python
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
    
    def start(self) -> str:
        return f"Engine ({self.horsepower} HP) vrooming"

class Car:
    def __init__(self, model: str, horsepower: int):
        self.model = model
        self.engine = Engine(horsepower)  # Composition

    def start_car(self) -> str:
        return f"Car {self.model}: {self.engine.start()}"
```

---

## 11. Special Dunder Methods & Operator Overloading

Dunder (double underscore) methods allow custom classes to hook into Python built-in operations and operator overloading:

| Dunder Category | Method Name | Trigger / Purpose |
| :--- | :--- | :--- |
| **Object Initialization** | `__init__(self, ...)` / `__new__(cls, ...)` | Instance initialization / allocation |
| **String Representation** | `__str__(self)` / `__repr__(self)` | `str(obj)` (user display) / `repr(obj)` (unambiguous code) |
| **Container Behavior** | `__len__(self)` / `__getitem__(self, idx)` | `len(obj)` / indexing `obj[idx]` |
| **Callable Instance** | `__call__(self, *args, **kwargs)` | Enables invoking object as function `obj()` |
| **Operator Overloading** | `__add__(self, other)` / `__eq__(self, other)` | Addition `a + b` / Equality `a == b` |
| **Context Manager** | `__enter__(self)` / `__exit__(self, ...)` | `with` block resource management |
| **Descriptor Hooks** | `__get__`, `__set__`, `__delete__`, `__set_name__` | Managed attribute access descriptors |

```python
class CustomContainer:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = list(items)

    def __str__(self) -> str:
        return f"Container '{self.name}' with {len(self.items)} items"

    def __repr__(self) -> str:
        return f"CustomContainer(name='{self.name}', items={self.items})"

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int):
        return self.items[index]

    def __call__(self) -> list:
        return self.items * 2
```

---

## 12. Abstract Base Classes (`abc.ABC`) & Structural Subtyping

`abc.ABC` enforces class contracts by preventing direct instantiation of abstract classes and requiring subclasses to implement `@abstractmethod` definitions.

```python
import abc

class DatabaseConnector(abc.ABC):
    @abc.abstractmethod
    def connect(self) -> str:
        pass

    @abc.abstractmethod
    def query(self, sql: str) -> Dict[str, Any]:
        pass

class PostgresConnector(DatabaseConnector):
    def connect(self) -> str:
        return "Connected to PostgreSQL database"

    def query(self, sql: str) -> Dict[str, Any]:
        return {"db": "PostgreSQL", "query": sql, "status": "SUCCESS"}
```

---

## 13. Memory Optimization with `__slots__`

By default, Python instances store attributes in a dynamic `__dict__`, consuming ~156-288 bytes per instance. Defining `__slots__` replaces `__dict__` with a fixed C-array descriptor, reducing per-instance memory by **60–70%**.

| Class Model | Attribute Storage | Per-Instance RAM | Dynamic Attributes? | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Class** | Dynamic `instance.__dict__` | ~156 – 288 Bytes | Yes (`obj.new_attr = 5`) | General OOP domain models |
| **Slots Class (`__slots__`)** | Fixed C Descriptor Array | ~48 – 64 Bytes | No (Raises `AttributeError`) | High-throughput data points (millions of objects) |

---

## 14. Python Version Evolution Breakdown (Python 2.7 & Python 3.3 ➔ Python 3.13)

### Comprehensive Version Matrix (Python 2.7 to Python 3.13)

| Python Version | Core OOP Enhancements & Behavioral Changes | Architectural & Performance Impact |
| :--- | :--- | :--- |
| **Python 2.7 (Legacy)** | Classic classes (without `object`) vs New-Style classes (`class Foo(object)`). Mandatory explicit `super(Child, self)`. `__nonzero__` method instead of `__bool__`. Metaclass syntax `__metaclass__ = Meta`. | Legacy object model; classic classes used old depth-first MRO causing lookup bugs; unbound method objects `<unbound method>`. |
| **Python 3.3** | Zero-argument `super()`, implicit `object` base class inheritance, `__qualname__` attribute introduced on classes and functions (PEP 3155), PEP 393 flexible string representation. | Modernized class object representation; simplified inheritance boilerplate (`super().__init__()`); nested class tracing. |
| **Python 3.4** | `abc.ABC` subclass helper introduced to simplify abstract base classes (replacing `metaclass=abc.ABCMeta`), Enum module (`enum.Enum`), `__weakref__` slot improvements. | Simplified ABC syntax without metaclass boilerplate; standardized enumeration classes. |
| **Python 3.5** | Type hinting annotations (`PEP 484`) for class attribute and method parameter typing, `@` matrix multiplication dunder methods (`__matmul__`, `__rmatmul__`, `__imatmul__`). | Foundation for static type checkers (Mypy) in OOP codebases; custom numerical matrix class operator overloading. |
| **Python 3.6** | Class variable type annotations (`PEP 526`), `__init_subclass__()` subclass initialization hook (`PEP 487`), `__set_name__()` descriptor protocol hook, insertion-ordered class `__dict__`. | Replaced complex metaclasses with clean `__init_subclass__` hooks; automatic descriptor attribute naming (`__set_name__`). |
| **Python 3.7** | Dataclasses introduced (`@dataclass` via PEP 557) auto-generating `__init__`, `__repr__`, `__eq__`; module `__getattr__` and `__dir__` hooks; postponed type evaluation (`from __future__ import annotations`). | Eliminates boilerplate `__init__` code; fast data container class creation. |
| **Python 3.8** | Positional-only parameter syntax (`/` PEP 570) in method signatures, `@cached_property` introduced in `functools`, assignment expressions (`:=` walrus operator) inside OOP method conditions. | Enforces strict method API boundaries; caches expensive property computations on instance `__dict__`. |
| **Python 3.9** | Built-in Generic Types in standard collections (`list[str]`, `dict[str, Any]` PEP 585) in class attribute type hints, `str.removeprefix()`/`str.removesuffix()` string methods for attribute cleaning. | Removed need to import `typing.List` / `typing.Dict` for class type annotations. |
| **Python 3.10** | Explicit Type Union operator (`X \| Y` PEP 604) for OOP method parameters, Structural Pattern Matching (`match / case` PEP 634) on class instances via `__match_args__`, precise error locations in tracebacks. | Enables pattern matching over class objects; cleaner type union annotations (`str \| None`). |
| **Python 3.11** | Specializing Adaptive Interpreter (CPython PEP 659) accelerates OOP method calls by **10–25%**, `@override` decorator (`typing.override` PEP 698) for static verification of inherited method overrides, Zero-cost exception handling. | Major CPython runtime performance boost for method dispatching and attribute lookup; static override safety. |
| **Python 3.12** | PEP 695 Type Parameter Syntax for Generic Classes (`class Stack[T]: ...`), isolated subinterpreters (`per-interpreter GIL`), CPython inline method cache speedups. | Simplified generic class syntax; clean subinterpreter isolation. |
| **Python 3.13** | Free-threaded CPython (PEP 703 - optional no-GIL build) accelerating multi-threaded parallel execution of OOP instances, Tier 2 JIT compiler, enhanced interactive REPL & class introspection. | True parallel multi-threading for OOP instance execution; next-generation CPython speed optimizations. |

---

## 15. Range Sequence Performance & Reflection (`dir(range)`)

### Range Evolution Across Python Versions
- **Python 2.7**: `range()` generated a full materialized `list` in memory. `xrange()` was a custom generator type for memory-friendly iteration.
- **Python 3.0+**: `range()` replaced `xrange()` entirely, becoming an immutable sequence object that computes elements lazily in $O(1)$ memory.

### Range Memory & Performance Benchmark
```python
import sys

r = range(1_000_000)
lst = list(r[:1000])

print(f"range(1_000_000) RAM footprint: {sys.getsizeof(r)} bytes")  # ~48 bytes (O(1))
print(f"list(1_000) RAM footprint:       {sys.getsizeof(lst)} bytes") # ~8000+ bytes (O(N))
```

### Introspection Matrix (`dir(range)`)
```python
r = range(10, 100, 5)
print("Start:", r.start) # 10
print("Stop:",  r.stop)  # 100
print("Step:",  r.step)  # 5
print("Attributes:", [a for a in dir(r) if not a.startswith("__")])
# ['count', 'index', 'start', 'step', 'stop']
```

