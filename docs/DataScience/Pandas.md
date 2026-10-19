# 🐼 Pandas Mastery: Tabular Engineering & High-Performance Data Analysis Guide

> **Module Scope:** Series, DataFrames, Explicit Indexing (`.loc` vs `.iloc`), GroupBy Aggregations, Categorical Memory Optimization, and High-Throughput I/O.

---

## 📌 Table of Contents
1. [Core Mental Model: Columnar Architecture](#1-core-mental-model-columnar-architecture)
2. [Explicit Selection: `.loc` vs `.iloc` & SettingWithCopyWarning](#2-explicit-selection-loc-vs-iloc--settingwithcopywarning)
3. [Filtering: Boolean Masks & `df.query()`](#3-filtering-boolean-masks--dfquery)
4. [The Split-Apply-Combine Pattern (`GroupBy`)](#4-the-split-apply-combine-pattern-groupby)
5. [Handling Missing Data Rigorously (`NaN`, `None`)](#5-handling-missing-data-rigorously-nan-none)
6. [Categorical Dtypes: 85%+ Memory Optimization](#6-categorical-dtypes-85-memory-optimization)
7. [Time-Series Analysis & Rolling Windows](#7-time-series-analysis--rolling-windows)
8. [Large Data I/O & Chunked Ingestion](#8-large-data-io--chunked-ingestion)
9. [Common Anti-Patterns & Performance Killers](#9-common-anti-patterns--performance-killers)
10. [Pandas Quick-Reference Cheat Sheet](#10-pandas-quick-reference-cheat-sheet)

---

## 1. Core Mental Model: Columnar Architecture

A **Pandas DataFrame** is fundamentally a dictionary of 1D arrays (**Series**) aligned by a shared **Index**:

```
Index Labels   Column: "Name" (object)   Column: "Age" (int64)   Column: "Salary" (float64)
    [0]            "Alice"                    28                      95000.0
    [1]            "Bob"                      34                      62000.0
    [2]            "Charlie"                  45                     110000.0
```

* **Memory Efficiency**: Calculations across a column (e.g. `df["Salary"].mean()`) execute as contiguous C-level NumPy array routines.
* **Row-wise operations are slow**: Accessing data across rows breaks memory locality and introduces heavy Python object overhead.

---

## 2. Explicit Selection: `.loc` vs `.iloc` & SettingWithCopyWarning

> [!CAUTION]
> Avoid chained assignment like `df['Salary'][df['Age'] > 30] = 50000`. This triggers `SettingWithCopyWarning` because Pandas cannot guarantee if it modified a view or a temporary copy.

### The Explicit Selection Rule:
| Method | Syntax | Basis | Slicing Behavior |
| :--- | :--- | :--- | :--- |
| **`.loc`** | `df.loc[row_label, col_label]` | **Label / Name-based** | Endpoint is **INCLUSIVE** |
| **`.iloc`** | `df.iloc[row_idx, col_idx]` | **Integer Position-based** | Endpoint is **EXCLUSIVE** (Python standard) |

```python
import pandas as pd

df = pd.DataFrame({
    "Department": ["Eng", "Sales", "Eng", "HR"],
    "Salary": [90000, 65000, 115000, 58000]
}, index=["e101", "e102", "e103", "e104"])

# 1. Label-based selection
high_eng = df.loc[df["Department"] == "Eng", "Salary"]

# 2. Integer position selection (First 2 rows, all columns)
first_two = df.iloc[0:2, :]

# 3. Safe in-place modification without warnings
df.loc["e101", "Salary"] = 98000
```

---

## 3. Filtering: Boolean Masks & `df.query()`

### Method A: Vectorized Boolean Masks
```python
# Multiple conditions require bitwise operators: & (AND), | (OR), ~ (NOT)
# Parentheses are MANDATORY due to Python operator precedence:
filtered_df = df[(df["Salary"] >= 80000) & (df["Department"] != "HR")]
```

### Method B: Clean Expression Filtering via `.query()`
`.query()` parses expressions using compiled C-level engines, improving readability for complex filters:
```python
min_sal = 80000
filtered_df = df.query("Salary >= @min_sal and Department != 'HR'")
```

---

## 4. The Split-Apply-Combine Pattern (`GroupBy`)

The `groupby` mechanism divides data into logical subsets, applies an aggregation or transformation, and combines results into a new tabular structure:

```python
# Group by Department and compute multiple summary metrics:
dept_summary = df.groupby("Department")["Salary"].agg([
    ("Headcount", "count"),
    ("Average_Pay", "mean"),
    ("Min_Pay", "min"),
    ("Max_Pay", "max")
])
```

### Transformations vs Aggregations:
* **`.agg()`**: Reduces each group to a single scalar value (changes row count).
* **`.transform()`**: Returns an array with the **same length** as the original DataFrame, ideal for computing group-relative features:
```python
# Compute employee salary relative to their department average
df["Dept_Avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")
df["Salary_vs_Dept_Avg"] = df["Salary"] - df["Dept_Avg_Salary"]
```

---

## 5. Handling Missing Data Rigorously (`NaN`, `None`)

In numerical columns, missing values are represented by IEEE 754 floating-point `NaN` (`np.nan`).

```python
# 1. Detection
missing_counts = df.isna().sum()

# 2. Removal
df_clean = df.dropna(subset=["Salary"])  # Drop only rows missing Salary

# 3. Imputation (Replacement)
# Median imputation is robust against outliers
median_sal = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_sal)

# 4. Time-series forward fill (carry last known value forward)
df["StockPrice"] = df["StockPrice"].ffill()
```

---

## 6. Categorical Dtypes: 85%+ Memory Optimization

When a string column contains repeated values (e.g. Country, Department, Plan), storing it as `object` allocates discrete Python string pointers for every single row.

```python
# Convert text to categorical codes
df["Department"] = df["Department"].astype("category")
```

### Real-World Memory Benchmark (100,000 Rows):
* **Object Dtype RAM**: `558,132 bytes`
* **Categorical Dtype RAM**: `10,411 bytes`
* **RAM Savings**: **98.1% Reduction**!

---

## 7. Time-Series Analysis & Rolling Windows

Pandas excels at high-frequency time-stamped datasets:

```python
# 1. Generate Business Daily Date Range
dates = pd.date_range(start="2026-01-01", periods=365, freq="B")

# 2. Set as DatetimeIndex
ts_df = pd.DataFrame({"Revenue": np.random.uniform(1000, 5000, len(dates))}, index=dates)

# 3. 7-Day Moving Average
ts_df["7D_MA"] = ts_df["Revenue"].rolling(window=7).mean()

# 4. Resample to Monthly Totals
monthly_revenue = ts_df["Revenue"].resample("ME").sum()
```

---

## 8. Large Data I/O & Chunked Ingestion

For datasets that exceed physical RAM, ingest using the `chunksize` iterator:

```python
chunk_size = 50_000
total_records = 0

for chunk in pd.read_csv("massive_telemetry.csv", chunksize=chunk_size):
    # Process chunk in C-level memory:
    filtered = chunk[chunk["Status"] == "CRITICAL"]
    total_records += len(filtered)

print("Total critical events:", total_records)
```

### Preferred File Formats:
* **Parquet (`df.to_parquet()`)**: Columnar, binary, gzip-compressed, retains exact schema/dtypes, 5x faster than CSV.
* **Feather (`df.to_feather()`)**: Zero-copy arrow format for ultrafast local caching.

---

## 9. Common Anti-Patterns & Performance Killers

### ❌ Anti-Pattern 1: Iterating with `for row in df.iterrows()`
```python
# DISASTROUS (Slow Python loop overhead):
for idx, row in df.iterrows():
    df.loc[idx, "Bonus"] = row["Salary"] * 0.1

# 100x FASTER (Vectorized SIMD):
df["Bonus"] = df["Salary"] * 0.1
```

### ❌ Anti-Pattern 2: Repeatedly appending rows to a DataFrame
```python
# DISASTROUS (Re-allocates memory on every append):
df = pd.DataFrame()
for data in raw_records:
    df = pd.concat([df, pd.DataFrame([data])])

# CORRECT (Collect in list, build DataFrame once):
rows = []
for data in raw_records:
    rows.append(data)
df = pd.DataFrame(rows)
```

---

## 10. Pandas Quick-Reference Cheat Sheet

```python
# Creation & Inspection
df.head(5)                    # First 5 rows
df.info()                     # Column types & non-null memory report
df.describe()                 # Numerical statistics (mean, std, percentiles)

# Selection & Filtering
df.loc[row_mask, "ColName"]   # Label-based accessor
df.iloc[0:10, 0:3]            # Position-based slice
df.query("Age > 25")          # String expression query

# Aggregation & Reshaping
df.groupby("Category").mean() # Grouped summary
df.pivot_table(values="V", index="A", columns="B", aggfunc="sum")
df.melt(id_vars=["ID"])       # Unpivot wide table to long format
df.sort_values(by="Salary", ascending=False)
```
