# 🐍 Comprehensive Python Methods & Object Architecture Master Guide

Welcome to the definitive pedagogical guide on **Python Methods**. This document provides an end-to-end learning path—from fundamental instance methods and decorators (`@classmethod`, `@staticmethod`, `@property`) to special dunder methods, the descriptor protocol, Method Resolution Order (MRO), and version-specific CPython behaviors (Python 2.7 through Python 3.13).

---

## 📌 Table of Contents
1. [Introduction to Methods vs. Standalone Functions](#1-introduction-to-methods-vs-standalone-functions)
2. [Instance Methods & `self` Binding](#2-instance-methods--self-binding)
3. [Class Methods (`@classmethod`) & Factory Pattern](#3-class-methods-classmethod--factory-pattern)
4. [Static Methods (`@staticmethod`) & Utility Isolation](#4-static-methods-staticmethod--utility-isolation)
5. [Property Methods (`@property`, `@setter`, `@deleter`)](#5-property-methods-property-setter-deleter)
6. [Special Dunder Methods & Operator Overloading](#6-special-dunder-methods--operator-overloading)
7. [The Descriptor Protocol (`__get__`, `__set__`, `__delete__`)](#7-the-descriptor-protocol-__get__-__set__-__delete__)
8. [Method Resolution Order (MRO) & C3 Linearization](#8-method-resolution-order-mro--c3-linearization)
9. [Runtime Method Introspection (`dir()`, `getattr()`, `inspect`)](#9-runtime-method-introspection-dir-getattr-inspect)
10. [Cross-Version Behavioral Analysis (Python 2.7 to 3.13)](#10-cross-version-behavioral-analysis-python-27-to-313)
11. [10 Practical Implementation Examples](#11-10-practical-implementation-examples)
12. [Common Method Pitfalls & How to Avoid Them](#12-common-method-pitfalls--how-to-avoid-them)
13. [Comparative Matrix: Functions vs. Method Types](#13-comparative-matrix-functions-vs-method-types)

---

## 1. Introduction to Methods vs. Standalone Functions

### What is a Method in Python?
A **method** is a function bound to a class or an instance of a class. Unlike standalone functions defined at module scope, methods implicitly receive the bound object or class reference as their first argument (`self` or `cls`) when invoked via dot notation (`instance.method()`).

### Key Differences: Standalone Functions vs. Methods

| Feature | Standalone Function | Instance Method | Class Method | Static Method |
| :--- | :--- | :--- | :--- | :--- |
| **First Implicit Arg** | None | `self` (Instance) | `cls` (Class) | None |
| **Decorator** | None | None | `@classmethod` | `@staticmethod` |
| **Access Scope** | Global / Module | Instance & Class State | Class State Only | No Bound State |
| **Descriptor Mechanism** | Standard Function | Bound Method Descriptor | Class Method Descriptor | Static Method Descriptor |

---

## 2. Instance Methods & `self` Binding

Instance methods are the most common type of method in Python OOP. They accept `self` as their first parameter, granting access to instance attributes (`self.attr`) and other instance methods.

```python
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self._balance = float(initial_balance)

    def deposit(self, amount: float) -> float:
        """Instance method modifying instance balance state."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return self._balance
```

---

## 3. Class Methods (`@classmethod`) & Factory Pattern

Class methods take `cls` as their first argument instead of `self`. They are bound to the class itself and are frequently used for **alternative constructors** (factory patterns) or class-level state updates.

```python
class UserProfile:
    total_users = 0

    def __init__(self, username: str, role: str) -> None:
        self.username = username
        self.role = role
        UserProfile.total_users += 1

    @classmethod
    def from_csv(cls, csv_str: str) -> "UserProfile":
        """Class method alternative constructor."""
        username, role = csv_str.split(",")
        return cls(username=username.strip(), role=role.strip())
```

---

## 4. Static Methods (`@staticmethod`) & Utility Isolation

Static methods do not receive `self` or `cls`. They behave like regular functions, but live inside the class namespace for logical grouping.

```python
class UserProfile:
    @staticmethod
    def validate_username(username: str) -> bool:
        """Static method: No access to instance or class state."""
        return len(username.strip()) >= 3
```

---

## 5. Property Methods (`@property`, `@setter`, `@deleter`)

Properties convert methods into managed attributes with controlled getter, setter, and deleter behavior.

```python
class StudentGrade:
    def __init__(self, score: float = 0.0) -> None:
        self._score = 0.0
        self.score = score

    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, value: float) -> None:
        if not (0.0 <= value <= 100.0):
            raise ValueError("Score must be between 0 and 100")
        self._score = float(value)

    @score.deleter
    def score(self) -> None:
        self._score = 0.0
```

---

## 6. Special Dunder Methods & Operator Overloading

Special methods (surrounded by double underscores) enable object customization and operator overloading (`+`, `==`, `len()`, `repr()`, `call()`).

```python
class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y
```

---

## 7. The Descriptor Protocol (`__get__`, `__set__`, `__delete__`)

The **descriptor protocol** powers `@property`, `@classmethod`, and `@staticmethod` behind the scenes. Any object defining `__get__()`, `__set__()`, or `__delete__()` acts as a descriptor.

```python
class NonNegative:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance: object, owner: type) -> float:
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0.0)

    def __set__(self, instance: object, value: float) -> None:
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")
        instance.__dict__[self.name] = float(value)
```

---

## 8. Method Resolution Order (MRO) & C3 Linearization

When calling a method in Python inheritance hierarchies, CPython uses **C3 Linearization** to search classes in order (`Class.mro()` or `Class.__mro__`).

```python
class Base:
    def action(self): return "Base"

class MixinA(Base):
    def action(self): return "MixinA -> " + super().action()

class MixinB(Base):
    def action(self): return "MixinB -> " + super().action()

class Child(MixinA, MixinB):
    pass

print(Child.mro())
# Output: [Child, MixinA, MixinB, Base, object]
```

---

## 9. Runtime Method Introspection (`dir()`, `getattr()`, `inspect`)

Runtime introspection enables dynamic method discovery and invocation:

```python
import inspect

class Demo:
    def greet(self): return "Hello"

d = Demo()
print(callable(getattr(d, "greet")))  # True
print(inspect.ismethod(d.greet))     # True
print(inspect.isfunction(Demo.greet))# True (Python 3)
```

---

## 10. Cross-Version Behavioral Analysis (Python 2.7 to 3.13)

```
Python 2.7 ──────────────────► Python 3.3 - 3.8 ─────────► Python 3.11 - 3.13
Unbound Methods (instancemethod) Plain Functions in Class Dict   Vectorcall Protocol &
class Foo(object): required     Implicit super(), PEP 487       15-25% Method Call Speedup
```

- **Python 2.7**: Calling `Foo.bar` returned an `unbound method` object requiring `isinstance` checks against `Foo`. Classes had to explicitly inherit from `object` (`class Foo(object):`).
- **Python 3.3+**: Unbound methods eliminated; `Foo.bar` returns a standard `function`. Zero-argument `super()` introduced.
- **Python 3.8–3.13**: CPython introduced the **Vectorcall Protocol** (PEP 590), avoiding temporary tuple/dict allocations during method calls, resulting in **15–25% faster method execution**.

---

## 11. 10 Practical Implementation Examples

### Example 1: Bank Account Encapsulation
```python
class Account:
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self._balance = balance

    def deposit(self, amount: float) -> float:
        self._balance += amount
        return self._balance
```

### Example 2: Alternative Constructors with `@classmethod`
```python
class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_iso(cls, iso_str: str) -> "Date":
        y, m, d = map(int, iso_str.split("-"))
        return cls(y, m, d)
```

### Example 3: Static Utility Validation
```python
class Validator:
    @staticmethod
    def is_email(email: str) -> bool:
        return "@" in email and "." in email
```

### Example 4: Temperature Property Converter
```python
class Temperature:
    def __init__(self, celsius: float = 0.0) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32
```

### Example 5: Callable Instance with `__call__`
```python
class Multiplier:
    def __init__(self, factor: float) -> None:
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor
```

---

## 12. Common Method Pitfalls & How to Avoid Them

1. **Forgetting `self` or `cls` as First Parameter**:
   - *Error*: `TypeError: method() takes 0 positional arguments but 1 was given`
   - *Fix*: Always declare `self` for instance methods or `cls` for class methods.

2. **Using `@staticmethod` When `@classmethod` is Required**:
   - Static methods cannot construct new instances dynamically or access class attributes.

3. **Mutable Class Attributes Shared Across Instances**:
   - Class attributes like `roles = []` are shared across all instances. Initialize lists inside `__init__` for instance isolation.

---

## 13. Comparative Matrix: Functions vs. Method Types

| Metric | Standalone Function | Instance Method | Class Method | Static Method |
| :--- | :--- | :--- | :--- | :--- |
| Binding | Unbound | Bound to Instance | Bound to Class | Unbound |
| Memory Overhead | Minimal | Small (method wrapper) | Small (method wrapper) | Minimal |
| Primary Use Case | Independent Utilities | Encapsulated Logic | Factory / Class State | Grouped Utilities |
