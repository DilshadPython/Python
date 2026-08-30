# Test-Example2 Module

Welcome to the **Test-Example2 Module**, demonstrating strategy/formatter patterns (`CSVFormatter`, `LogFormatter`), file stream lifetime management, and abstract file writers.

---

## Directory Structure & Module Catalog

```text
Test-Example2/
├── README.md                   # Documentation and execution guide
├── file_formatters.py          # CSV/Log formatters & composite FileWriter
├── abstract_file_writers.py    # ABC WriteFile with DelimFile & LogFile
├── test_example2.py            # Unit test suite
└── [legacy wrappers]           # Refactored entry points (assign2.py, files.py, etc.)
```

---

## How to Run

```bash
# Run file formatters demonstration
python3 file_formatters.py

# Run abstract file writers demonstration
python3 abstract_file_writers.py

# Run unit tests
python3 -m unittest test_example2.py
```
