# 🐼 High-Performance Pandas Data Analysis & Range Evolution Studio

Welcome to the **Pandas Data Analysis & Range Evolution Studio**, a production-grade pedagogical curriculum designed to master tabular data manipulation, Series/DataFrame data structures, vectorized operations, time-series date sequences, memory optimization, and runtime performance analysis in Python.

---

## 📌 Table of Contents

1. [Overview & Project Architecture](#1-overview--project-architecture)
2. [3-Step Pedagogical Curriculum](#2-3-step-pedagogical-curriculum)
   - [Step 1: 01-Fundamentals](#step-1-01-fundamentals)
   - [Step 2: 02-Advanced-Math-and-Operators](#step-2-02-advanced-math-and-operators)
   - [Step 3: 03-Range-Evolution-and-Performance](#step-3-03-range-evolution-and-performance)
3. [Comprehensive Pandas Series & DataFrame Running Attributes & Methods](#3-comprehensive-pandas-series--dataframe-running-attributes--methods)
4. [Python 3.3 to Python 3.13 Evolution Matrix with Pandas](#4-python-33-to-python-313-evolution-matrix-with-pandas)
5. [Execution & Test Suite Instructions](#5-execution--test-suite-instructions)

---

## 1. Overview & Project Architecture

Pandas is Python's leading data analysis library, built on top of NumPy to provide fast, flexible, and expressive data structures (`Series` for 1D sequences, `DataFrame` for 2D tabular data).

### Workspace Layout

```
pandas_tutorial/
├── 01-Fundamentals/
│   ├── __init__.py
│   ├── series_creation_and_indexing.py     # Series from lists, dicts, custom labels
│   ├── dataframe_creation_and_metadata.py  # DataFrames, column types, .info(), .describe()
│   └── test_fundamentals.py                # Unit tests for fundamentals
├── 02-Advanced-Math-and-Operators/
│   ├── __init__.py
│   ├── dataframe_slicing_and_indexing.py   # .head, .tail, .loc, .iloc, query filtering
│   ├── vector_math_and_string_methods.py   # Column math, .str accessors, .groupby aggregations
│   ├── dataframe_io_and_persistence.py     # CSV, JSON, and Pickle I/O routines
│   └── test_advanced_operations.py         # Unit tests for slicing & vector math
├── 03-Range-Evolution-and-Performance/
│   ├── __init__.py
│   ├── date_range_vs_python_range.py       # range() vs pd.date_range() & RangeIndex
│   ├── pandas_performance_and_evolution.py # Category dtypes RAM savings & benchmarks
│   ├── reflection_and_introspection.py     # dir(pd.Series) & dir(pd.DataFrame) matrices
│   └── test_range_performance.py          # Unit tests for performance & reflection
├── pandas_tutorial_basics.py               # Executable master curriculum runner
├── test_pandas_master.py                   # Master test runner (21 unit tests)
└── README.md                              # Project documentation
```

---

## 2. 3-Step Pedagogical Curriculum

### Step 1: 01-Fundamentals
- **Series Construction**: From lists, dicts, arrays, scalars, with custom index labels.
- **DataFrame Construction**: From 2D dicts, lists of dicts, and Series objects.
- **Metadata Inspection**: Analyzing `.shape`, `.dtypes`, `.columns`, `.info()`, `.describe()`, and `.memory_usage()`.

### Step 2: 02-Advanced-Math-and-Operators
- **Selection & Slicing**: Label-based indexing (`.loc`), integer position indexing (`.iloc`), boolean masking (`df[df['col'] > val]`), and expression queries (`.query()`).
- **Vectorized String Accessor**: String manipulation routines via `.str` (`.str.upper()`, `.str.contains()`, `.str.replace()`).
- **Group Aggregations**: Grouping data via `.groupby()` and applying multi-metric aggregations (`.agg(['count', 'mean', 'sum'])`).
- **File Persistence**: Exporting and importing CSV (`read_csv`, `to_csv`), JSON (`read_json`, `to_json`), and Pickle binary files.

### Step 3: 03-Range-Evolution-and-Performance
- **`pd.date_range()` vs `range()`**: Temporal frequency sequences (`'D'`, `'B'`, `'ME'`, `'h'`) vs standard Python `range()`.
- **Memory Footprint Optimization**: High-efficiency categorical data types (`astype('category')`) achieving **80%+ RAM reduction**.
- **Runtime Introspection**: Using `dir(pd.Series)` and `dir(pd.DataFrame)` to introspect reflection matrices.

---

## 3. Comprehensive Pandas Series & DataFrame Running Attributes & Methods

### Introspection Matrix

| Attribute / Method | Category | Description | `Series` | `DataFrame` | Code Example |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `.index` | Metadata | Index label sequence | ✅ | ✅ | `obj.index` |
| `.values` | Storage | Underlying NumPy array buffer | ✅ | ✅ | `obj.values` |
| `.dtype` / `.dtypes` | Metadata | Data type(s) of elements | ✅ (`.dtype`) | ✅ (`.dtypes`) | `df.dtypes` |
| `.shape` | Geometry | Tuple of dimensions | ✅ | ✅ | `df.shape` |
| `.size` | Geometry | Total element count | ✅ | ✅ | `df.size` |
| `.columns` | Metadata | Column label Index | ❌ | ✅ | `df.columns` |
| `.T` | Linear Alg | Transposed DataFrame table | ❌ | ✅ | `df.T` |
| `.head(n)` / `.tail(n)` | Preview | First/Last N rows | ✅ | ✅ | `df.head(5)` |
| `.info()` | Summary | Schema and memory breakdown | ❌ | ✅ | `df.info()` |
| `.describe()` | Summary | Statistical summary metrics | ✅ | ✅ | `df.describe()` |
| `.loc[row, col]` | Selection | Label-based indexing | ✅ | ✅ | `df.loc[0:2, ['A']]` |
| `.iloc[row, col]` | Selection | Position-based indexing | ✅ | ✅ | `df.iloc[0:2, 0:1]` |
| `.query(expr)` | Selection | Filter rows by query string | ❌ | ✅ | `df.query('Salary > 50000')` |
| `.str` | Accessor | Vectorized string methods | ✅ | ❌ | `s.str.upper()` |
| `.groupby(col)` | Grouping | Group rows by category | ❌ | ✅ | `df.groupby('Dept').mean()` |
| `.astype(dtype)` | Transform | Cast column data type | ✅ | ✅ | `df['Dept'].astype('category')` |
| `.isna()` / `.fillna(val)` | Cleaning | Detect & fill missing values | ✅ | ✅ | `df.fillna(0)` |
| `.unique()` / `.nunique()` | Unique | Extract unique values & counts | ✅ | ❌ | `s.unique(), s.nunique()` |
| `.value_counts()` | Frequency | Frequency distribution table | ✅ | ✅ | `s.value_counts()` |

### Python Code Demonstration of Running Attributes & Methods

```python
import pandas as pd

# Create sample DataFrame
df = pd.DataFrame({
    "Department": ["Engineering", "Marketing", "Engineering", "HR"],
    "Salary": [85000.0, 62000.0, 95000.0, 58000.0],
    "Rating": [4.8, 4.2, 4.9, 3.8]
})

# --- 1. Running Attributes ---
print("Shape:  ", df.shape)    # (4, 3)
print("Columns:", list(df.columns))
print("Dtypes:\n", df.dtypes)

# --- 2. Running Selection & Query Methods ---
sub_loc = df.loc[0:2, ["Department", "Salary"]]
query_res = df.query("Salary > 60000 and Rating >= 4.0")

# --- 3. Running String Accessor & Groupby Methods ---
upper_depts = df["Department"].str.upper()
grouped = df.groupby("Department")["Salary"].agg(["count", "mean"])

# --- 4. Running Memory Optimization ---
df["Department"] = df["Department"].astype("category")
print("Optimized Memory:\n", df.memory_usage(deep=True))
```

---

## 4. Python 3.3 to Python 3.13 Evolution Matrix with Pandas

Below is the complete version-by-version breakdown of Python enhancements from **Python 3.3 to Python 3.13**, detailing their interaction with Pandas data analysis:

| Python Version | Core Feature Updates & Behavioral Evolution | Pandas Integration & Code Demonstration |
| :--- | :--- | :--- |
| **Python 3.3** | `range` sequence slicing ($O(1)$ lazy ranges); `yield from` generator delegation syntax. | ```python<br>r = range(100)[::2]<br>s = pd.Series(r)<br>``` |
| **Python 3.4** | `enum` module; `pathlib.Path` standard library integration for file IO. | ```python<br>from pathlib import Path<br>df = pd.read_csv(Path('data.csv'))<br>``` |
| **Python 3.5** | **PEP 465**: Matrix multiplication operator (`@`) for `DataFrame.__matmul__`. | ```python<br>df = pd.DataFrame([[1, 2], [3, 4]])<br>res = df.T @ df<br>``` |
| **Python 3.6** | Formatted string literals (f-strings); ordered keyword kwargs in `pd.DataFrame()`. | ```python<br>name = "Data"<br>print(f"Loaded {name} with shape {df.shape}")<br>``` |
| **Python 3.7** | Dataclasses (`@dataclass`); CPython bytecode optimizations for dictionary dispatches. | ```python<br>from dataclasses import dataclass<br>@dataclass<br>class Report:<br>    table: pd.DataFrame<br>``` |
| **Python 3.8** | **PEP 570**: Positional-only parameter syntax (`/`); **PEP 572**: Walrus operator (`:=`). | ```python<br>if (m := df['Salary'].mean()) > 60000:<br>    filtered = df[df['Salary'] > m]<br>``` |
| **Python 3.9** | Dictionary union operators (`\|` & `\|=`); built-in generics type hints (`pd.Series[float]`). | ```python<br>meta = {"rows": 100} \| {"cols": 5}<br>def load_data() -> pd.DataFrame: ...<br>``` |
| **Python 3.10** | **PEP 634**: Structural Pattern Matching (`match / case`) over shapes & columns. | ```python<br>match df.columns.tolist():<br>    case ["ID", "Name", *rest]: print("Standard Schema")<br>``` |
| **Python 3.11** | **PEP 659**: Specializing Adaptive Interpreter accelerates CPython loop dispatching by **10–25%**. | ```python<br># Faster element-wise loop iteration in custom apply()<br>df['Col'].apply(lambda x: x * 2)<br>``` |
| **Python 3.12** | Per-interpreter GIL; fine-grained error location indicators in tracebacks. | ```python<br># Traceback underlines failing DataFrame slice:<br># df.loc[row_idx, col_idx]<br>``` |
| **Python 3.13** | **PEP 703**: Free-threaded CPython (GIL removal) and Tier 2 JIT compilation engine. | ```python<br># Multi-threaded parallel processing of Pandas<br># read_csv and groupby pipelines without GIL locks.<br>``` |

---

## 5. Execution & Test Suite Instructions

### Running the Standalone Master Curriculum
To execute the interactive 3-step curriculum demonstration:
```bash
python3 pandas_tutorial_basics.py
```

### Running the Master Unit Test Suite
To execute all 21 unit tests across all curriculum modules:
```bash
python3 test_pandas_master.py
```
