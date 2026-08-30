# Class and Instance Attributes Module

Welcome to the **Class and Instance Attributes Module**, demonstrating how Python resolves variable lookups across class and instance namespaces.

---

## Directory Structure & Module Catalog

```text
Class-and-Instance-Attribute/
├── README.md                                   # Documentation and execution guide
├── class_vs_instance_attributes.py             # Class defaults vs instance configuration
├── attribute_encapsulation_and_deletion.py     # Attribute shadowing and del instance.attr fallback
├── test_class_instance_attribute.py            # Unit test suite
└── [legacy wrappers]                           # Refactored entry points (cls_attrib_and_instance_attrib.py, etc.)
```

---

## How to Run

```bash
# Run class vs instance attributes demonstration
python3 class_vs_instance_attributes.py

# Run attribute shadowing and deletion demonstration
python3 attribute_encapsulation_and_deletion.py

# Run unit tests
python3 -m unittest test_class_instance_attribute.py
```