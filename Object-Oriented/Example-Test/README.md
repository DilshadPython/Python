# Example-Test Module

Welcome to the **Example-Test Module**, demonstrating container class design, bounded capacity (`MaxSizeList`), and state encapsulation.

---

## Directory Structure & Module Catalog

```text
Example-Test/
├── README.md                   # Documentation and execution guide
├── max_size_list.py            # Bounded list container with eviction logic
├── test_example_test.py        # Unit test suite
└── [legacy wrappers]           # Refactored entry points (add_data_from_assign.py, etc.)
```

---

## How to Run

```bash
# Run max size list demonstration
python3 max_size_list.py

# Run unit tests
python3 -m unittest test_example_test.py
```
