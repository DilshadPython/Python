# Class and Instance Data Module

Welcome to the **Class and Instance Data Module**, demonstrating reflection, `dir()` introspection, custom attribute deletion (`__delattr__`), and instance tracking.

---

## Directory Structure & Module Catalog

```text
Class-and-Instance-Data/
├── README.md                           # Documentation and execution guide
├── class_reflection_and_dir.py         # Introspection via dir(), __dict__, and __class__
├── custom_attribute_deleter.py         # Intercepting attribute deletion via __delattr__
├── instance_counter.py                 # Tracking instance counts with class attributes
├── test_class_instance_data.py         # Unit test suite
└── [legacy wrappers]                   # Refactored entry points (class_dir_func.py, etc.)
```

---

## How to Run

```bash
# Run reflection demonstration
python3 class_reflection_and_dir.py

# Run attribute deletion interception
python3 custom_attribute_deleter.py

# Run instance counter demonstration
python3 instance_counter.py

# Run unit tests
python3 -m unittest test_class_instance_data.py
```
