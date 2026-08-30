# Abstract Base Classes (`abs_base_cls`) Module

Welcome to the **Abstract Base Classes (`abs_base_cls`) Module**, demonstrating interface contracts, `abc.ABC`, `@abc.abstractmethod`, and concrete subclass inheritance in Python.

---

## Directory Structure & Module Catalog

```text
abs_base_cls/
├── README.md                   # Module documentation and execution guide
├── abstract_base_class.py      # Core ABC definition, @abstractmethod, and concrete implementation
├── abstract_inheritance.py     # Advanced ABC inheritance: input validation & history tracking
├── test_abs_base_cls.py        # Comprehensive unit test suite
└── [legacy wrappers]           # Backward-compatible refactored entry points (abc.py, inheritance_abc.py)
```

---

## How to Run

```bash
# Run core ABC demonstration
python3 abstract_base_class.py

# Run advanced ABC inheritance demonstration
python3 abstract_inheritance.py

# Run unit tests
python3 -m unittest test_abs_base_cls.py
```

---

## Technical Summary & Version Changes

1. **Python 2.7 vs Python 3.4+ Syntax**:
   - **Python 2.7**: Required `__metaclass__ = abc.ABCMeta` inside the class body.
   - **Python 3.4+**: Inherits directly from helper class `abc.ABC` (`class MyABC(abc.ABC):`).

2. **Enforcement Mechanics**:
   - Classes with at least one `@abc.abstractmethod` cannot be instantiated directly; attempting to do so raises `TypeError`.
   - Subclasses must implement all abstract methods before they can be instantiated.
