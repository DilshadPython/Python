# OOP-Advance: Advanced Object-Oriented Programming in Python

Welcome to the **OOP-Advance** tutorial module. This project provides a comprehensive, hands-on, and pedagogical guide to advanced Object-Oriented Programming (OOP) concepts in Python, ranging from class initialization and property decorators to built-in sequence subclassing and version evolution.

---

## Project Structure & Module Directory

```text
OOP-Advance/
├── README.md                              # Master project documentation
├── docs.md                                # Pedagogical reference on version evolution & range
├── test_oop_advance.py                    # Root unit test runner
├── class_definition_init.py               # Constructor initialization & instance methods
├── class_init.py                          # Refactored legacy init module
├── class_method_factory.py                # @classmethod state mutation & factory constructors
├── class_method.py                        # Refactored legacy class method module
├── class_attributes_no_init.py            # Dynamic attribute assignment without constructor
├── class_no_init.py                       # Refactored legacy no-init module
├── encapsulation_attributes.py            # Public, protected (_var), private mangling (__var), & properties
├── public_private_attr.py                 # Refactored legacy attributes module
├── instance_regular_method.py             # Instance methods bound via self
├── regular_method.py                      # Refactored legacy regular method module
├── utility_static_method.py               # @staticmethod utility functions in class namespaces
├── static_method.py                       # Refactored legacy static method module
├── classic_vs_new_style_class.py          # Python 2 classic classes vs Python 3 unified model
├── style_class.py                         # Refactored legacy class style module
├── staff_management.py                    # Class state tracking & namespace introspection (__dict__)
├── users.py                               # Refactored legacy users module
├── range_version_evolution.py             # Range behavioral changes, O(1) containment, & dir() inspection
│
├── Assignment/                            # Container Subclassing & Persistence
│   ├── README.md                          # Sub-directory documentation
│   ├── dict_subclass_setitem.py           # Dict subclassing without infinite recursion
│   ├── ass_models.py                      # Legacy wrapper
│   ├── config_dict_file_persistence.py    # ConfigDict(dict) with text file disk sync
│   ├── assignments.py / solutions.py      # Legacy wrappers
│   ├── cli_config_parser.py               # CLI tool for configuration management
│   ├── test.py                            # Legacy CLI wrapper
│   └── test_assignment.py                 # Unit test suite
│
├── Encapsulation/                         # Property Decorators & Access Control
│   ├── README.md                          # Sub-directory documentation
│   ├── getter_setter_methods.py           # Explicit getter (get_val) & setter (set_val) methods
│   ├── encap_set_get.py                   # Legacy wrapper
│   ├── property_encapsulation.py          # Pythonic @property, @setter, @deleter
│   ├── encap_set_get_del.py               # Legacy wrapper
│   └── test_encapsulation.py              # Unit test suite
│
└── Inheritance-built-in/                  # Built-in Subclassing & Operator Overloading
    ├── README.md                          # Sub-directory documentation
    ├── vector_arithmetic_overloading.py   # Pairwise element addition/subtraction (__add__, __sub__)
    ├── add_func.py / add_sub_func.py      # Legacy wrappers
    ├── dictionary_subclassing.py          # Dict subclassing with custom assignment logging
    ├── inherit_builtin.py / func.py       # Legacy wrappers
    ├── one_based_list.py                  # 1-based indexing sequence subclassing list
    ├── inherit_list.py                    # Legacy wrapper
    ├── container_operator_overloading.py  # Dunder operator methods (__add__, __sub__) & dict **
    ├── list_oper.py / operators.py        # Legacy wrappers
    └── test_inheritance_builtin.py        # Unit test suite
```

---

## Key OOP Concepts & Best Practices

1. **Method Binding Protocols**:
   - **Instance Methods**: Receive instance as `self`. Access and mutate individual instance state.
   - **Class Methods (`@classmethod`)**: Receive class object as `cls`. Modify shared class variables or serve as alternative constructor factories.
   - **Static Methods (`@staticmethod`)**: Receive no implicit `self` or `cls` argument. Logically group utility functions within a class namespace.

2. **Encapsulation & Access Modifiers**:
   - **Public**: `var` — Unrestricted access.
   - **Protected**: `_var` — Non-public hint for internal/subclass use.
   - **Private Name Mangling**: `__var` — Automatically mangled by compiler to `_ClassName__var` to prevent name clashes in child classes.
   - **Properties (`@property`)**: Transparent accessor control for getting, setting (`@var.setter`), and deleting (`@var.deleter`) attributes.

3. **Subclassing Built-in Types & Avoiding Recursion**:
   - When subclassing `dict` or `list` and overriding `__setitem__`, calling `self[key] = val` causes an infinite recursion loop.
   - **Correct Practice**: Invoke `dict.__setitem__(self, key, val)` or `super().__setitem__(key, val)`.

---

## Python Version Evolution (Python 2.7 -> 3.3 -> 3.13)

### Class Model & Object Hierarchy
- **Python 2.7**: Distinguished between "Classic Classes" (`class Old:`) and "New-Style Classes" (`class New(object):`).
- **Python 3.3+**: Unified class model. All classes implicitly inherit from `object` and share a single type system.

### `range` Object Evolution & Performance Notes
- **Python 2.7**: `range()` eagerly created a full `list` in memory. `xrange()` was a lazy generator.
- **Python 3.3+**: `range` replaced `xrange()` as an immutable sequence object. Containment testing (`x in range_obj`) operates in $O(1)$ time using arithmetic bounds calculation rather than linear scans.
- **Python 3.13**: Highly optimized C-level iterator with minimal memory overhead, supporting arbitrary precision integer bounds, negative steps, and sequence slicing.

#### `dir(range)` Attribute Introspection Example
```python
r = range(0, 10, 2)
# Public sequence attributes and methods:
# ['start', 'stop', 'step', 'count', 'index']
# Key dunder protocols:
# ['__contains__', '__getitem__', '__iter__', '__len__', '__reversed__']
```

---

## Running Unit Tests

Execute the unit test suites across all folders:

```bash
# 1. Root OOP-Advance tests
python3 -m unittest test_oop_advance.py

# 2. Assignment folder tests
cd Assignment && python3 -m unittest test_assignment.py && cd ..

# 3. Encapsulation folder tests
cd Encapsulation && python3 -m unittest test_encapsulation.py && cd ..

# 4. Inheritance-built-in folder tests
cd Inheritance-built-in && python3 -m unittest test_inheritance_builtin.py && cd ..
```
