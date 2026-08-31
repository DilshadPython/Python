# 🐍 Object-Oriented Programming (OOP) Master Module

Welcome to the definitive master tutorial module for **Object-Oriented Programming (OOP)** in Python. This directory features a **4-step sequential curriculum**—guiding students step-by-step from core fundamentals to advanced design patterns and practical exercises.

---

## 📌 Directory Architecture & Sequential Learning Path

```text
Object-Oriented/
├── 01-Fundamentals/              # Step 1: Beginner OOP Concepts
│   ├── class_definition_basics.py# Class definition, __init__ constructor, self
│   ├── class_and_instance_attributes.py # Class variables vs. instance variables
│   ├── basic_inheritance.py      # Single inheritance, method overriding, super()
│   └── test_fundamentals.py      # Unit tests for Step 1
│
├── 02-Advanced/                  # Step 2: Advanced Method Decorators & Properties
│   ├── class_methods_factory.py  # @classmethod factories & shared state
│   ├── static_utility_methods.py # @staticmethod date & utility functions
│   ├── property_encapsulation.py # @property getters, setters, and deleters
│   └── test_advanced.py          # Unit tests for Step 2
│
├── 03-Design-Patterns/           # Step 3: Metaprogramming & Architecture
│   ├── abstract_base_classes.py  # Interfaces using abc.ABC & @abstractmethod
│   ├── builtin_subclassing.py    # Subclassing native dict and list containers
│   ├── magic_dunder_methods.py   # Special dunder methods (__getitem__, __add__)
│   ├── mixins_and_descriptors.py # Descriptor protocol, Mixins & __init_subclass__
│   ├── range_version_evolution.py# Range sequence memory efficiency & dir()
│   └── test_design_patterns.py   # Unit tests for Step 3
│
├── 04-Exercises/                 # Step 4: Real-World Practice Projects
│   ├── bank_account_exercise.py  # BankAccount & SavingsAccount hierarchy
│   ├── vehicle_fleet_exercise.py # Vehicle & ElectricCar fleet management
│   └── test_exercises.py         # Unit tests for Step 4
│
├── README.md                     # Sequential study guide & roadmap
├── docs.md                       # Technical CPython object model documentation
└── test_oop_master.py            # Master test runner executing all 4 steps
```

---

## 🚀 Sequential Roadmap

| Step | Subdirectory | Focus & Key Concepts Covered |
| :--- | :--- | :--- |
| **Step 1: Beginner** | `01-Fundamentals/` | `class`, `object`, `self`, `__init__`, instance attributes, instance methods, single inheritance (`super()`). |
| **Step 2: Method Types** | `02-Advanced/` | `@classmethod` factories, `@staticmethod` utilities, `@property` getters/setters/deleters, encapsulation. |
| **Step 3: Patterns** | `03-Design-Patterns/` | Abstract Base Classes (`abc.ABC`), container subclassing (`dict`, `list`), special dunder methods, `range` O(1) memory notes. |
| **Step 4: Exercises** | `04-Exercises/` | Real-world projects combining fundamentals, inheritance, and defensive validation guard clauses. |

---

## 🧪 Running the Unit Test Suite

Execute all tests across all 4 steps:

```bash
# Run master test runner
python3 Object-Oriented/test_oop_master.py
```

---

## ⚡ CPython 3.13 & Version Evolution (2.7 ➔ 3.13)

- **Python 2.7**: Required explicit `class Foo(object):` for new-style classes. `super()` required explicit arguments `super(Child, self).__init__()`.
- **Python 3.0+**: All classes implicitly inherit from `object`. `super()` supports clean argumentless syntax.
- **Python 3.13**: Specialized vectorcall slot dispatching and inline attribute caches accelerate `@property` getters and method execution by **~15–20%**.
