# Python Object-Oriented Programming (OOP) Master Reference

Welcome to the **Python Object-Oriented Programming (OOP) Master Reference**, a standardized, production-grade educational and technical reference for understanding class definitions, object instantiation, attribute resolution chains, instance/class/static methods, property encapsulation, inheritance, method resolution order (MRO), magic (dunder) methods, and CPython OOP architecture.

---

## Directory Structure & Module Catalog

```text
Object-Oriented/
├── README.md                           # Overview, catalog, execution guide, & OOP concepts reference
├── docs.md                             # Technical reference detailing C3 linearization, descriptors, slots, & PEPs
├── class_definition_basics.py          # Class definitions, __init__ constructor, instance state, & dir()
├── class_and_instance_attributes.py    # Class attributes vs instance attributes & __dict__ variable shadowing
├── instance_class_static_methods.py    # Instance methods, @classmethod constructors, & @staticmethod utilities
├── property_getters_setters.py         # Encapsulation via @property, @setter, and @deleter
├── class_inheritance_and_mro.py        # Single/multiple inheritance, super(), isinstance(), & MRO
├── magic_dunder_methods.py             # Magic methods (__repr__, __str__, __add__, __len__, __eq__)
├── ice_cream_machine.py                # Domain modeling and combination generation
├── procedural_vs_oop.py                # Side-by-side comparative analysis: Procedural vs OOP paradigms
├── test_object_oriented.py             # Comprehensive unittest test suite (12 test cases)
└── [legacy wrappers]                   # Backward-compatible refactored entry points (basic_class_var.py, etc.)
```

---

## Core OOP Concepts Summary

### 1. `class_definition_basics.py`
Demonstrates creating custom classes (`Employee`, `Car`), initializing instance attributes inside `__init__`, defining instance methods (`get_details()`), and inspecting public attributes using `dir()`.

### 2. `class_and_instance_attributes.py`
Details the attribute resolution order:
1. Check instance dictionary (`self.__dict__`).
2. Check class dictionary (`Class.__dict__`).
3. Check base class hierarchy (`MRO`).

Illustrates how setting an attribute on an instance creates a local shadow copy in `self.__dict__` without modifying the class attribute.

### 3. `instance_class_static_methods.py`
Distinguishes the 3 method types:
- **Instance Method**: Takes implicit `self`. Accesses instance state.
- **Class Method (`@classmethod`)**: Takes implicit `cls`. Serves as alternative constructor factory (`from_string()`) and modifies class state.
- **Static Method (`@staticmethod`)**: Unbound utility function contained within class scope (`is_workday()`).

### 4. `property_getters_setters.py`
Implements Pythonic encapsulation using properties:
- `@property`: Computes read-only managed attributes (`email`, `full_name`).
- `@full_name.setter`: Validates and parses assigned values (`emp.full_name = "First Last"`).
- `@full_name.deleter`: Handles attribute cleanup (`del emp.full_name`).

### 5. `class_inheritance_and_mro.py`
Demonstrates single inheritance (`Developer` and `Manager` inheriting from `Employee`), forwarding arguments via `super().__init__()`, overriding default parameters, inspecting inheritance chains using `isinstance()` and `issubclass()`, and inspecting Method Resolution Order (`Class.__mro__`).

### 6. `magic_dunder_methods.py`
Covers operator overloading and object protocol dunders:
- `__repr__`: Unambiguous developer string (`EmployeeRecord('Name', ...)`).
- `__str__`: User-friendly string representation.
- `__add__`: Overloading addition (`+`) operator for combining object values.
- `__len__`: Custom length measurement using `len(obj)`.
- `__eq__`: Equality comparison using `==`.

### 7. `ice_cream_machine.py`
Provides real-world domain modeling by generating combinations of ice cream flavors and toppings.

### 8. `procedural_vs_oop.py`
Compares global variable mutation in procedural programming against state encapsulation inside class instances in OOP.

---

## How to Run the Code

### Running Individual Python Modules

```bash
# Basic class definition and dir() introspection
python3 class_definition_basics.py

# Class attributes vs instance attributes and __dict__
python3 class_and_instance_attributes.py

# Instance, class, and static methods
python3 instance_class_static_methods.py

# Property getters, setters, and deleters
python3 property_getters_setters.py

# Class inheritance, super(), and MRO
python3 class_inheritance_and_mro.py

# Magic dunder methods and operator overloading
python3 magic_dunder_methods.py

# Ice Cream Machine domain modeling
python3 ice_cream_machine.py

# Procedural vs OOP comparison
python3 procedural_vs_oop.py
```

### Running the Unit Test Suite

Execute the `unittest` framework from the terminal:

```bash
python3 -m unittest test_object_oriented.py
```

Or run with verbose output:

```bash
python3 -m unittest -v test_object_oriented.py
```

---

## OOP Paradigm Comparison Table

| Dimension | Class Attribute | Instance Attribute | Property (`@property`) |
| :--- | :--- | :--- | :--- |
| **Storage Location** | `Class.__dict__` | `instance.__dict__` | `Class.__dict__` (as Descriptor) |
| **Scope / Sharing** | Shared across all instances | Unique to each object instance | Computed per instance read/write |
| **Invocation Syntax** | `Class.attr` or `inst.attr` | `inst.attr` | `inst.attr` (syntax looks like attribute) |
| **Best Used For** | Constants, counters, defaults | State specific to an object instance | Validation, computed fields, encapsulation |
