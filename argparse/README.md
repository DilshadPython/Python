# 🛠️ Command-Line Argument Parsing (`argparse`) Pedagogical Module

Welcome to the **`argparse` Command-Line Argument Parsing Module**. This module provides a complete, modern 3-tier pedagogical architecture for mastering command-line argument parsing in Python.

It covers foundational argument parsing, positional vs optional parameters, subparsers (subcommands like `git` or `docker`), choices validation, mutually exclusive argument groups, custom type validators, range sequence integration, runtime introspection (`dir(range)`), and version evolution notes from Python 2.7 to 3.13.

---

## 📂 Module Architecture

```
argparse/
├── 01-Fundamentals/
│   ├── basic_argparse.py        # Positional args, optional flags, type conversion, defaults
│   └── test_fundamentals.py     # Unittest suite for fundamental parsing
├── 02-Advanced-Parsing-and-Subcommands/
│   ├── advanced_argparse.py     # Subparsers, choices, mutually exclusive groups, custom actions
│   └── test_advanced.py         # Unittest suite for advanced features & subcommands
├── 03-Range-Evolution-and-Performance/
│   ├── range_argparse.py        # Range CLI options, O(1) memory benchmarking, dir(range) matrix
│   └── test_range_evolution.py  # Unittest suite for range CLI & introspection
├── test_argparse_master.py      # Master unittest runner executing all 3 sub-tier test suites
└── README.md                    # Module documentation & usage guide
```

---

## 🚀 Execution & Usage Guide

### 1. Basic Argument Parser (`01-Fundamentals`)

Run basic parsing from the command line:

```bash
python3 argparse/01-Fundamentals/basic_argparse.py data.csv --count 3 --verbose
```

Output:
```text
[VERBOSE] Cycle 1/3: Processing file 'data.csv'
[VERBOSE] Cycle 2/3: Processing file 'data.csv'
[VERBOSE] Cycle 3/3: Processing file 'data.csv'
```

### 2. Advanced Subcommands Parser (`02-Advanced-Parsing-and-Subcommands`)

Execute multi-command CLI operations:

```bash
python3 argparse/02-Advanced-Parsing-and-Subcommands/advanced_argparse.py run --env prod --workers 4 --tag v1.0 --tag release -vv --json
```

Output:
```text
Parsed Advanced CLI Arguments:
  command: run
  env: prod
  workers: 4
  tags: ['v1.0', 'release']
  verbosity: 2
  json: True
  xml: False
```

### 3. Range CLI & Introspection (`03-Range-Evolution-and-Performance`)

Generate sequence objects via CLI parameters:

```bash
python3 argparse/03-Range-Evolution-and-Performance/range_argparse.py --start 10 --stop 100 --step 5
```

---

## 🧪 Unit Test Execution

Run the master test runner from the root repository directory:

```bash
python3 argparse/test_argparse_master.py
```

Or execute individual test suites:

```bash
python3 -m unittest discover -s argparse/01-Fundamentals -p "test_*.py"
python3 -m unittest discover -s argparse/02-Advanced-Parsing-and-Subcommands -p "test_*.py"
python3 -m unittest discover -s argparse/03-Range-Evolution-and-Performance -p "test_*.py"
```

---

## 📊 Summary of Pedagogical Features

| Sub-Tier | Primary Features Covered | Code File | Unit Test File |
| :--- | :--- | :--- | :--- |
| **01-Fundamentals** | Positional args, `--count`, `--verbose` flags, default parameters | [`basic_argparse.py`](01-Fundamentals/basic_argparse.py) | [`test_fundamentals.py`](01-Fundamentals/test_fundamentals.py) |
| **02-Advanced** | Subparsers (`run`/`config`), `--env` choices, `--json` vs `--xml` mutually exclusive group | [`advanced_argparse.py`](02-Advanced-Parsing-and-Subcommands/advanced_argparse.py) | [`test_advanced.py`](02-Advanced-Parsing-and-Subcommands/test_advanced.py) |
| **03-Range & Evolution** | Range CLI options, $O(1)$ memory benchmarking, `dir(range)` matrix, Py 2.7 to 3.13 history | [`range_argparse.py`](03-Range-Evolution-and-Performance/range_argparse.py) | [`test_range_evolution.py`](03-Range-Evolution-and-Performance/test_range_evolution.py) |
