# 🐍 Object-Oriented Programming (OOP) Master Module

Welcome to the definitive master tutorial module for **Object-Oriented Programming (OOP)** in Python. This directory features a 3-tier structured curriculum—from core fundamentals (`01-Fundamentals`) to advanced design patterns (`02-Advanced`) and practical exercises (`03-Exercises`).

---

## 📌 Directory Architecture

```text
Object-Oriented/
├── 01-Fundamentals/              # Tier 1: Beginner OOP Concepts
│   ├── class_definition_basics.py# Class definition, __init__ constructor, self
│   ├── class_and_instance_attributes.py # Class variables vs. instance variables
│   ├── basic_inheritance.py      # Inheritance, method overriding, super()
│   └── test_fundamentals.py      # Unit tests for basic OOP fundamentals
│
├── 02-Advanced/                  # Tier 2: Advanced OOP Design Patterns
│   ├── class_methods_factory.py  # @classmethod factories & shared state
│   ├── static_utility_methods.py # @staticmethod date & utility functions
│   ├── property_encapsulation.py # @property getters, setters, and deleters
│   ├── abstract_base_classes.py  # Abstract base classes (abc.ABC) & @abstractmethod
│   ├── builtin_subclassing.py    # Subclassing native dict and list containers
│   ├── magic_dunder_methods.py   # Dunder methods (__getitem__, __add__, __repr__)
│   └── test_advanced.py          # Unit tests for advanced OOP features
│
├── 03-Exercises/                 # Tier 3: Practical Hands-On Exercises
│   ├── bank_account_exercise.py  # BankAccount & SavingsAccount hierarchy
│   ├── vehicle_fleet_exercise.py # Vehicle & ElectricCar fleet management
│   └── test_exercises.py         # Unit tests for practical exercises
│
├── README.md                     # Master module guide and learning roadmap
├── docs.md                       # Technical documentation & CPython object model notes
└── test_oop_master.py            # Master test runner executing all unit tests
```

---

## 🚀 Learning Roadmap

| Tier | Folder | Focus & Key Concepts Covered |
| :--- | :--- | :--- |
| **Tier 1: Beginner** | `01-Fundamentals/` | `class`, `object`, `self`, `__init__`, instance attributes, instance methods, single inheritance (`super()`). |
| **Tier 2: Advanced** | `02-Advanced/` | `@classmethod` factories, `@staticmethod` utilities, `@property` accessors, `abc.ABC`, operator overloading (`__add__`), built-in subclassing. |
| **Tier 3: Exercises** | `03-Exercises/` | Practical real-world projects combining fundamentals, inheritance, and defensive validation guard clauses. |

---

## 🧪 Running the Unit Test Suite

Execute all tests from the repository root:

```bash
# Discover and run all tests in Object-Oriented/
python3 -m unittest discover -s Object-Oriented -p "test_*.py"
```

---

## ⚡ CPython 3.13 & Version Evolution (2.7 ➔ 3.13)

- **Python 2.7**: Required explicit `class Foo(object):` for new-style classes. `super()` required arguments `super(Child, self).__init__()`.
- **Python 3.0+**: All classes implicitly inherit from `object`. `super()` supports clean argumentless syntax.
- **Python 3.13**: Specialized vectorcall slot dispatching and inline attribute caches accelerate `@property` getters and method execution by **~15–20%**.
