# Object-Oriented Programming (OOP) Advanced Documentation

## 1. Version Evolution & Technical Overview

### Python 2.7 vs Python 3.3 vs Python 3.13

| Feature / Behavior | Python 2.7 | Python 3.3 | Python 3.13 |
| :--- | :--- | :--- | :--- |
| **Class Hierarchy Model** | Classic (`class Old:`) vs New-Style (`class New(object):`) | Unified New-Style Class Model (all inherit from `object`) | Unified New-Style Model with C-optimized descriptor resolution |
| **`range` Sequence** | `range()` allocated full memory list; `xrange()` was lazy generator | `range` replaced `xrange()` as an immutable sequence | `range` features $O(1)$ containment checks, arbitrary precision bounds, & C-level iterator speeds |
| **`super()` Syntax** | Required explicit class and self parameters: `super(Child, self).__init__()` | Zero-argument `super()` introduced | Zero-argument `super()` with optimized compiler cell closure |
| **Type Annotations** | Not natively supported (docstrings or comments only) | Introduced function annotations (PEP 3107) | Full type system with generics, `ParamSpec`, and `TypeVarTuple` |
| **Dictionary Ordering** | Unordered hash table | Unordered hash table | Insertion-ordered dictionary guaranteed by language specification |

---

## 2. Deep Dive: `range` Object Evolution & Performance Notes

### Historical Context & Changes
1. **Python 2.7**:
   - `range(start, stop, step)` eagerly generated and allocated a full `list` of integers in memory.
   - `xrange(start, stop, step)` returned a custom lazy iterator object to avoid huge memory allocations.
2. **Python 3.3**:
   - `range` absorbed `xrange` behavior, returning an immutable sequence type.
   - Introduced $O(1)$ time complexity for containment checks (`x in range_obj`) using arithmetic bounds calculation rather than linear scans.
3. **Python 3.13**:
   - Highly optimized C-level implementation supporting slicing, negative stepping, arbitrary precision integer bounds, and full container protocol emulation.

### Introspection & Available Attributes (`dir(range)`)
Evaluating `dir(range(10))` reveals public attributes and dunder methods:
- **Public Attributes**: `start`, `stop`, `step`, `count()`, `index()`.
- **Dunder Protocols**: `__getitem__`, `__len__`, `__contains__`, `__iter__`, `__reversed__`, `__eq__`.

---

## 3. Core OOP Patterns Covered in `OOP-Advance`

1. **Class Instantiation & Constructor Methods** (`class_definition_init.py`):
   - Constructor parameter initialization (`__init__`) and instance attribute assignment.
2. **Class Methods & Alternative Constructors** (`class_method_factory.py`):
   - Using `@classmethod` with `cls` to modify class state or implement factory constructors (`from_string`).
3. **Encapsulation & Access Modifiers** (`encapsulation_attributes.py`):
   - Public attributes, protected attributes (`_var`), private name mangling (`__var`), and managed properties (`@property`, `@setter`, `@deleter`).
4. **Static Utility Methods** (`utility_static_method.py`):
   - `@staticmethod` for grouping utility functions inside class namespaces.
5. **Built-in Class Subclassing** (`Assignment/config_dict_file_persistence.py`, `Inheritance-built-in/one_based_list.py`):
   - Extending `dict` and `list` while properly invoking superclass methods (`dict.__setitem__`, `super().__getitem__`) to avoid recursion loops.
