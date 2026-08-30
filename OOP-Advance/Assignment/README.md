# Assignment: Subclassing Built-in Containers & File Persistence

This directory demonstrates advanced container subclassing techniques in Python.

## Core Concepts Covered

1. **Dictionary Subclassing (`dict_subclass_setitem.py`)**:
   - Overriding `__setitem__` on `dict` subclasses.
   - Calling `dict.__setitem__(self, key, value)` or `super().__setitem__(key, value)` directly to prevent infinite recursive loops (`self[key] = value`).

2. **Persistent Configuration Dictionary (`config_dict_file_persistence.py`)**:
   - Subclassing `dict` to load settings from a text file during `__init__`.
   - Automatically synchronizing key-value additions and updates back to disk on item assignment (`__setitem__`).

3. **Command Line Utility (`cli_config_parser.py`)**:
   - Command line parsing tool reading and updating persistent configuration parameters.

## Running Tests

To execute unit tests for this subfolder:
```bash
python3 -m unittest test_assignment.py
```
