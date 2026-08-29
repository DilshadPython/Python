# Technical Documentation: Python Dictionaries (`12.Dictionary`)

## 1. Overview & Hash Table Architecture
A **dictionary** in Python is a mutable mapping association of key-value pairs. Python dictionaries utilize compact hash tables guaranteeing $O(1)$ average time complexity for insertion, retrieval, and deletion operations.

### Key Characteristics:
- **Keys**: Must be unique and hashable (immutable objects like `str`, `int`, `tuple`).
- **Values**: Any arbitrary Python object.
- **Insertion Order**: Guaranteed to preserve key insertion order in Python 3.7+ (CPython 3.6+).

---

## 2. Python Version Evolution (Python 3.3 – Python 3.13 & Python 2.7 Comparison)

### A. Evolution across Python 3.3 to Python 3.13
1. **Python 3.6 / 3.7 Insertion Order Preservation (PEP 468)**:
   - In Python 3.6+, CPython refactored dictionaries into compact hash tables with sparse indices and dense key-value arrays. This reduced memory consumption by 20% to 25% while preserving insertion order.
2. **Python 3.9 Union Operators (PEP 584)**:
   - Introduced dict merge (`|`) and dict update (`|=`) operators:
     ```python
     d1 = {'a': 1}
     d2 = {'b': 2}
     merged = d1 | d2  # {'a': 1, 'b': 2}
     ```
3. **Python 3.10 Pattern Matching (PEP 634)**:
   - Structural pattern matching supported key matching on mapping objects:
     ```python
     match user_record:
         case {'role': 'admin', 'name': name}: print(f"Admin: {name}")
     ```

### B. Python 2.7 Legacy Comparison
- **`dict.keys()`, `values()`, `items()` Returns**:
  - Python 2.7: Returned full standard lists (allocated immediately in RAM).
  - Python 3.x: Return dynamic view objects (`dict_keys`, `dict_values`, `dict_items`) providing $O(1)$ set operations without dynamic memory allocation.
- **Dictionary Unordered Behavior**:
  - Python 2.7 dictionaries were strictly unordered. Iterating over keys produced non-deterministic pseudo-random order. `collections.OrderedDict` was required for order preservation.

---

## 3. Sorting Dictionaries by Value
Sorting dictionaries by value requires `sorted()` over `dict.items()` using key functions:
1. **Lambda Function**: `sorted(d.items(), key=lambda item: item[1])`
2. **`operator.itemgetter`**: `sorted(d.items(), key=operator.itemgetter(1))` (Recommended for peak C performance).
