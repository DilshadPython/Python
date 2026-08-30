# Encapsulation Module

Welcome to the **Encapsulation Module**, demonstrating state hiding, property getters/setters, and defensive type validation.

---

## Directory Structure & Module Catalog

```text
Encapsulation/
├── README.md                           # Documentation and execution guide
├── book_instance.py                    # Book attribute initialization & summary
├── house_price_encapsulation.py        # Managed properties with setter validation
├── validated_integer.py                # Safe integer parsing & increment operations
├── test_encapsulation.py               # Unit test suite
└── [legacy wrappers]                   # Refactored entry points (books.py, set_and_get.py, etc.)
```

---

## How to Run

```bash
# Run book instance demonstration
python3 book_instance.py

# Run house price encapsulation demonstration
python3 house_price_encapsulation.py

# Run validated integer demonstration
python3 validated_integer.py

# Run unit tests
python3 -m unittest test_encapsulation.py
```