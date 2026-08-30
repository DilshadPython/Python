# Encapsulation Patterns in Python

This directory demonstrates attribute access control and property encapsulation in Python OOP.

## Core Topics Covered

1. **Explicit Method Encapsulation (`getter_setter_methods.py`)**:
   - Traditional OOP encapsulation using `get_val()` and `set_val()` methods to protect object internal state.

2. **Pythonic Property Decorators (`property_encapsulation.py`)**:
   - Using `@property` for attribute access getters.
   - Using `@var.setter` for value assignment validation.
   - Using `@var.deleter` for custom deletion logic.

## Running Tests

To run unit tests for Encapsulation:
```bash
python3 -m unittest test_encapsulation.py
```
