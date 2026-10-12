# 🚀 Python `if __name__ == '__main__'` Entry Point Studio

Welcome to the **Python `if __name__ == '__main__'` Entry Point Studio**, a production-grade pedagogical curriculum designed to master runtime execution context, script vs module import mechanics, CLI argument parsing, local scope performance optimization (`LOAD_FAST`), and Python version evolutions from Python 3.3 to Python 3.13.

---

## 📌 Table of Contents

1. [Overview & Project Architecture](#1-overview--project-architecture)
2. [3-Step Pedagogical Curriculum](#2-3-step-pedagogical-curriculum)
   - [Step 1: 01-Fundamentals](#step-1-01-fundamentals)
   - [Step 2: 02-Advanced-Math-and-Operators](#step-2-02-advanced-math-and-operators)
   - [Step 3: 03-Range-Evolution-and-Performance](#step-3-03-range-evolution-and-performance)
3. [Runtime Module Metadata Attributes Matrix](#3-runtime-module-metadata-attributes-matrix)
4. [Python 3.3 to Python 3.13 Evolution Matrix](#4-python-33-to-python-313-evolution-matrix)
5. [Execution & Test Suite Instructions](#5-execution--test-suite-instructions)

---

## 1. Overview & Project Architecture

In Python, `__name__` is a special built-in variable automatically set by the interpreter:
- When a file is executed directly (e.g. `python script.py`), Python sets `__name__ = "__main__"`.
- When a file is imported as a module (e.g. `import script`), Python sets `__name__ = "script"`.

Using the `if __name__ == "__main__":` idiom allows Python files to serve dual roles: executable standalone CLI applications and reusable library modules.

### Workspace Layout

```
name_main/
├── 01-Fundamentals/
│   ├── __init__.py
│   ├── name_attribute_basics.py         # __name__ variable inspection & context
│   ├── main_entry_point_idiom.py        # def main() -> int entry point guard pattern
│   └── test_fundamentals.py             # Unit tests for fundamentals
├── 02-Advanced-Math-and-Operators/
│   ├── __init__.py
│   ├── module_import_vs_execution.py    # Import side-effects vs execution analysis
│   ├── cli_args_and_execution_context.py# sys.argv parsing & os.environ context
│   └── test_advanced_operations.py      # Unit tests for import vs CLI operations
├── 03-Range-Evolution-and-Performance/
│   ├── __init__.py
│   ├── range_iteration_and_entry_points.py  # Local scope range processing
│   ├── execution_performance_and_evolution.py # LOAD_FAST vs LOAD_GLOBAL speedups & matrix
│   ├── reflection_and_introspection.py  # dir() module attributes & dir(range) reflection
│   └── test_range_performance.py       # Unit tests for performance & reflection
├── name_main_basics.py                 # Executable master curriculum runner
├── test_name_main_master.py             # Master test runner (12 unit tests)
└── README.md                           # Project documentation
```

---

## 2. 3-Step Pedagogical Curriculum

### Step 1: 01-Fundamentals
- **Variable Inspection**: Inspecting runtime values of `__name__` during execution.
- **Entry Point Guard**: Structuring code cleanly with `def main() -> int` and `if __name__ == "__main__": sys.exit(main())`.

### Step 2: 02-Advanced-Math-and-Operators
- **Import vs Execution Analysis**: Demonstrating how importing external functions dynamically sets `__name__` to the imported module name.
- **CLI Argument Handling**: Passing `sys.argv` arrays to `main(argv)` and reading system environment variables (`os.environ`).

### Step 3: 03-Range-Evolution-and-Performance
- **Local Scope Optimization**: Benchmarking local function scope execution (`LOAD_FAST` bytecode opcode) vs global top-level scope (`LOAD_GLOBAL`), demonstrating **~30% execution speedup**.
- **Runtime Reflection**: Introspecting module namespace using `dir()` and `dir(range)`.

---

## 3. Runtime Module Metadata Attributes Matrix

| Attribute | Description | Value (Direct Execution) | Value (Imported Module) |
| :--- | :--- | :--- | :--- |
| `__name__` | Name of current module namespace | `"__main__"` | `"module_name"` |
| `__file__` | Path to module source file | `/path/to/script.py` | `/path/to/script.py` |
| `__doc__` | Module-level docstring text | Text or `None` | Text or `None` |
| `__package__` | Enclosing package name | `""` or `None` | `"package_name"` |
| `__spec__` | PEP 451 module spec location | `ModuleSpec` object | `ModuleSpec` object |

---

## 4. Python 3.3 to Python 3.13 Evolution Matrix

| Python Version | Core Feature Updates & Behavioral Evolution | Entry Point & Module Execution Highlights |
| :--- | :--- | :--- |
| **Python 3.3** | `range` sequence slicing ($O(1)$ lazy ranges); `sys.implementation` object. | Enhanced module namespace inspection and interpreter details. |
| **Python 3.4** | PEP 451 module specs introduced (`__spec__`). | Standardized module loading and import metadata. |
| **Python 3.5** | PEP 484 type hints syntax. | Type-annotated main signatures: `def main(argv: list[str] \| None = None) -> int:`. |
| **Python 3.6** | F-strings & module attribute insertion order preservation. | Formatted logging inside entry points: `print(f"Running {__name__}")`. |
| **Python 3.7** | Execution of directory packages (`python directory/`). | Standardized `__main__.py` discovery in directory execution. |
| **Python 3.8** | Walrus operator (`:=`) & positional-only parameter syntax (`/`). | Concise CLI argument parsing: `if (arg_len := len(sys.argv)) > 1:`. |
| **Python 3.9** | Built-in generic type hints (`list[str]`). | Clean type annotations without importing `typing.List`. |
| **Python 3.10** | Structural Pattern Matching (`match / case`, PEP 634). | Pattern matching CLI flags: `match argv[1:]: case ["--help"]: ...`. |
| **Python 3.11** | Specializing Adaptive Interpreter (PEP 659). | Local variable bytecode dispatching inside `main()` accelerated by **10–25%**. |
| **Python 3.12** | Per-interpreter GIL & fine-grained traceback indicators. | Detailed error locations pointing directly to failing lines inside `main()`. |
| **Python 3.13** | Free-threaded CPython (PEP 703 - GIL removal) & Tier 2 JIT compiler. | Concurrent execution of entry points without GIL lock bottlenecks. |

---

## 5. Execution & Test Suite Instructions

### Running the Standalone Master Curriculum
To execute the interactive 3-step curriculum demonstration:
```bash
python3 name_main_basics.py
```

### Running the Master Unit Test Suite
To execute all 12 unit tests across all curriculum modules:
```bash
python3 test_name_main_master.py
```
