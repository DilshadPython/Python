# Inheritance Module

Welcome to the **Inheritance Module**, demonstrating single inheritance, `super()`, subclass method overriding, polymorphism, and class extensions.

---

## Directory Structure & Module Catalog

```text
Inheritance/
├── README.md                   # Documentation and execution guide
├── animal_hierarchy.py         # Animal base class & Cat/Pigeon polymorphism
├── company_hierarchy.py        # CompanyEmployee base class & Staff/Manager subclasses
├── date_time_extension.py      # Subclassing standard library datetime.date
├── test_inheritance.py         # Unit test suite
└── [legacy wrappers]           # Refactored entry points (animals.py, company.py, etc.)
```

---

## How to Run

```bash
# Run animal hierarchy demonstration
python3 animal_hierarchy.py

# Run company hierarchy demonstration
python3 company_hierarchy.py

# Run date time extension demonstration
python3 date_time_extension.py

# Run unit tests
python3 -m unittest test_inheritance.py
```