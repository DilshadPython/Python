# Magic-Method Module

Welcome to the **Magic-Method Module**, demonstrating Python object protocols, dunder methods (`__repr__`, `__str__`, `__add__`, `__len__`, `__eq__`), and operator overloading.

---

## Directory Structure & Module Catalog

```text
Magic-Method/
├── README.md                           # Documentation and execution guide
├── builtin_dunder_emulation.py         # Built-in type dunder calls (int, float, str)
├── account_dunder_methods.py           # Custom class dunder protocol implementation
├── test_magic_method.py                # Unit test suite
└── [legacy wrappers]                   # Refactored entry points (dundder.py, magic_method.py, etc.)
```

---

## How to Run

```bash
# Run built-in dunder emulation
python3 builtin_dunder_emulation.py

# Run account dunder methods demonstration
python3 account_dunder_methods.py

# Run unit tests
python3 -m unittest test_magic_method.py
```
