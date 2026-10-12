# 🐍 Anaconda & Conda Environment Management (`anaconda`) Pedagogical Module

Welcome to the **`anaconda` Conda Environment Management Module**. This module provides a complete 3-tier pedagogical architecture for mastering Conda environment creation, package management (`conda install`, `pip`), channel priorities (`conda-forge`, `pytorch`), YAML export/import (`environment.yml`), range-driven package batch pagination, $O(1)$ memory benchmarking, `dir(range)` runtime introspection, and historical version evolution notes from Python 2.7 (`env27`) to 3.13.

---

## 📂 Module Architecture

```
anaconda/
├── 01_fundamentals/
│   ├── conda_basics.py                  # CondaEnvironment dataclass, activation, package install/remove
│   └── test_fundamentals.py             # Unittest suite for environment creation & package operations
├── 02_advanced_environment_management/
│   ├── conda_advanced.py                # YAML export/import, channel priorities, conflict resolution
│   └── test_advanced.py                 # Unittest suite for YAML export & conflict validation
├── 03_range_evolution_and_performance/
│   ├── range_conda_performance.py      # Package list range pagination, O(1) memory benchmarking, dir(range) matrix
│   └── test_range_evolution.py        # Unittest suite for range batch generator & reflection
├── test_anaconda_master.py              # Master unittest runner executing all 3 sub-tier test suites
└── README.md                            # Module documentation & usage guide
```

---

## 🚀 Execution & Usage Guide

### 1. Basic Conda Environments (`01_fundamentals`)

Run basic environment creation and package installation demo:

```bash
python3 anaconda/01_fundamentals/conda_basics.py
```

### 2. Advanced Environment Export (`02_advanced_environment_management`)

Generate `environment.yml` dictionary specs and manage channel priorities:

```bash
python3 anaconda/02_advanced_environment_management/conda_advanced.py
```

### 3. Range Package Pagination & Benchmarks (`03_range_evolution_and_performance`)

Simulate range offset batch pagination and memory benchmarks:

```bash
python3 anaconda/03_range_evolution_and_performance/range_conda_performance.py
```

---

## 🧪 Unit Test Execution

Run the master test runner from the root repository directory:

```bash
python3 anaconda/test_anaconda_master.py
```

Or execute individual test suites:

```bash
python3 -m unittest discover -s anaconda/01_fundamentals -p "test_*.py"
python3 -m unittest discover -s anaconda/02_advanced_environment_management -p "test_*.py"
python3 -m unittest discover -s anaconda/03_range_evolution_and_performance -p "test_*.py"
```

---

## 📊 Summary of Pedagogical Features

| Sub-Tier | Primary Features Covered | Code File | Unit Test File |
| :--- | :--- | :--- | :--- |
| **01_fundamentals** | Environment creation, activation/deactivation, `conda install`, package list formatting | [`conda_basics.py`](01_fundamentals/conda_basics.py) | [`test_fundamentals.py`](01_fundamentals/test_fundamentals.py) |
| **02_advanced** | `environment.yml` spec export, channel ordering (`conda-forge`), conflict validation | [`conda_advanced.py`](02_advanced_environment_management/conda_advanced.py) | [`test_advanced.py`](02_advanced_environment_management/test_advanced.py) |
| **03_range & evolution** | Package offset range pagination, $O(1)$ memory footprint, `dir(range)` matrix, Py 2.7 to 3.13 history | [`range_conda_performance.py`](03_range_evolution_and_performance/range_conda_performance.py) | [`test_range_evolution.py`](03_range_evolution_and_performance/test_range_evolution.py) |