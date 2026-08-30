# Inheritance from Built-in Types & Operator Overloading

This directory demonstrates extending Python built-in types (`dict`, `list`) and overloading standard dunder operators (`__add__`, `__sub__`, `__repr__`).

## Core Topics Covered

1. **Vector Arithmetic Operator Overloading (`vector_arithmetic_overloading.py`)**:
   - Overloading `+` (`__add__`) and `-` (`__sub__`) operators on custom sequence classes (`SumList`) to perform pairwise element arithmetic.

2. **Subclassing Built-in Dict (`dictionary_subclassing.py`)**:
   - Subclassing `dict` to intercept and log item assignment (`__setitem__`).

3. **1-Based Indexing Sequence (`one_based_list.py`)**:
   - Subclassing `list` to implement custom 1-based index access, translating 1-indexed queries (`obj[1]`) to internal 0-indexed positions.

4. **Container Operator Methods (`container_operator_overloading.py`)**:
   - Examining explicit dunder method calls (`__add__`, `__sub__`) on Python primitive types.

## Running Tests

To run unit tests for this subfolder:
```bash
python3 -m unittest test_inheritance_builtin.py
```
