# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and RAM memory measurement.
# - import time: Standard library module for execution time benchmarking.
# - from pathlib import Path: Safe file path manipulations for CSV, JSON, and Pickle persistence.
# - from typing import Any, Dict, List, Optional, Tuple, Union: PEP 484 type annotations.
# - import pandas as pd: High-performance data structure and tabular data analysis library.
# - import numpy as np: Fast numerical array processing library underlying Pandas core.
# =========================================================================
from pathlib import Path
import sys
import time
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd


# ─── SUBFOLDER 1: 01-FUNDAMENTALS ─────────────────────────────────────────────


def create_series_from_list() -> pd.Series:
    """
    [Subfolder Title: 01-Fundamentals -> series_creation_and_indexing.py]
    Constructs a Pandas Series from a standard Python integer list with RangeIndex.

    Returns:
        pd.Series: Integer series named 'IntegerSequence'.
    """
    data: List[int] = [10, 20, 30, 40, 50]
    series: pd.Series = pd.Series(data, name="IntegerSequence")
    return series


def create_series_with_custom_index() -> pd.Series:
    """
    [Subfolder Title: 01-Fundamentals -> series_creation_and_indexing.py]
    Constructs a Pandas Series with custom string index labels (City names).

    Returns:
        pd.Series: Floating-point series indexed by city strings.
    """
    temperatures: List[float] = [22.5, 18.0, 31.2, 15.4]
    cities: List[str] = ["London", "Paris", "Tokyo", "Berlin"]
    series: pd.Series = pd.Series(
        temperatures, index=cities, name="Temperature_Celsius"
    )
    return series


def create_series_from_dict() -> pd.Series:
    """
    [Subfolder Title: 01-Fundamentals -> series_creation_and_indexing.py]
    Constructs a Pandas Series from a dictionary where keys automatically become index labels.

    Returns:
        pd.Series: Series initialized from fruit inventory dict.
    """
    fruit_stock: Dict[str, int] = {
        "Apples": 150,
        "Bananas": 300,
        "Oranges": 200,
        "Grapes": 90,
    }
    series: pd.Series = pd.Series(fruit_stock, name="FruitInventory")
    return series


def inspect_series_metadata(series: pd.Series) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> series_creation_and_indexing.py]
    Extracts core metadata attributes (.index, .values, .dtype, .shape, .size) from a Series.

    Args:
        series (pd.Series): Target input series.

    Returns:
        Dict[str, Any]: Dictionary of Series metadata.
    """
    return {
        "name": series.name,
        "dtype": str(series.dtype),
        "shape": series.shape,
        "size": series.size,
        "index_type": type(series.index).__name__,
        "has_nulls": bool(series.isnull().any()),
    }


def create_sample_dataframe() -> pd.DataFrame:
    """
    [Subfolder Title: 01-Fundamentals -> dataframe_creation_and_metadata.py]
    Constructs a 2D sample DataFrame containing employee records across departments.

    Returns:
        pd.DataFrame: Table with columns (EmployeeID, Name, Department, Salary, Rating).
    """
    raw_data: Dict[str, Any] = {
        "EmployeeID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
        "Salary": [85000.0, 62000.0, 95000.0, 58000.0, 67000.0],
        "Rating": [4.8, 4.2, 4.9, 3.8, 4.5],
    }
    df: pd.DataFrame = pd.DataFrame(raw_data)
    return df


def inspect_dataframe_metadata(df: pd.DataFrame) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> dataframe_creation_and_metadata.py]
    Extracts structural dimensions, column listings, data types, and total memory usage in bytes.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        Dict[str, Any]: Metadata dictionary.
    """
    return {
        "shape": df.shape,
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "total_memory_bytes": int(df.memory_usage(deep=True).sum()),
    }


def cast_column_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    [Subfolder Title: 01-Fundamentals -> dataframe_creation_and_metadata.py]
    Demonstrates data type casting on DataFrame columns using .astype().

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame copy with converted int32 EmployeeID and category Department.
    """
    updated_df: pd.DataFrame = df.copy()
    updated_df["EmployeeID"] = updated_df["EmployeeID"].astype(np.int32)
    updated_df["Department"] = updated_df["Department"].astype("category")
    return updated_df


# ─── SUBFOLDER 2: 02-ADVANCED-MATH-AND-OPERATORS ──────────────────────────────


def get_preview_slices(
    df: pd.DataFrame, n: int = 2
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_slicing_and_indexing.py]
    Returns top N rows (.head) and bottom N rows (.tail) of a DataFrame.

    Args:
        df (pd.DataFrame): Target input DataFrame.
        n (int, optional): Number of rows to slice. Defaults to 2.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Top slice and bottom slice.
    """
    return df.head(n), df.tail(n)


def select_by_label(
    df: pd.DataFrame, row_start: int, row_end: int, columns: List[str]
) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_slicing_and_indexing.py]
    Selects rows and specific column names using label-based indexing (.loc).

    Args:
        df (pd.DataFrame): Input DataFrame.
        row_start (int): Start row index label.
        row_end (int): End row index label.
        columns (List[str]): Column labels to filter.

    Returns:
        pd.DataFrame: Sub-DataFrame slice.
    """
    return df.loc[row_start:row_end, columns]


def select_by_position(
    df: pd.DataFrame, row_slice: slice, col_slice: slice
) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_slicing_and_indexing.py]
    Selects rows and columns using integer position indexing (.iloc).

    Args:
        df (pd.DataFrame): Input DataFrame.
        row_slice (slice): Row index position slice.
        col_slice (slice): Column index position slice.

    Returns:
        pd.DataFrame: Position-indexed sub-DataFrame.
    """
    return df.iloc[row_slice, col_slice]


def filter_by_boolean_condition(df: pd.DataFrame, min_salary: float) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_slicing_and_indexing.py]
    Filters DataFrame rows using boolean masking on Salary (df[df['Salary'] > min_salary]).

    Args:
        df (pd.DataFrame): Input DataFrame.
        min_salary (float): Salary threshold limit.

    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    mask: pd.Series = df["Salary"] > min_salary
    return df[mask]


def filter_using_query(
    df: pd.DataFrame, department: str, min_rating: float
) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_slicing_and_indexing.py]
    Filters DataFrame rows using dynamic expression query method (.query()).

    Args:
        df (pd.DataFrame): Input DataFrame.
        department (str): Target department name string.
        min_rating (float): Minimum performance rating.

    Returns:
        pd.DataFrame: Query-filtered DataFrame.
    """
    return df.query("Department == @department and Rating >= @min_rating")


def compute_column_statistics(df: pd.DataFrame, num_col: str) -> Dict[str, float]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> vector_math_and_string_methods.py]
    Computes statistical aggregations (.sum(), .mean(), .std(), .median(), .min(), .max()) for a numeric column.

    Args:
        df (pd.DataFrame): Input DataFrame.
        num_col (str): Target numeric column label.

    Returns:
        Dict[str, float]: Dictionary of column statistics.
    """
    col: pd.Series = df[num_col]
    return {
        "sum": float(col.sum()),
        "mean": float(col.mean()),
        "std": float(col.std()),
        "median": float(col.median()),
        "min": float(col.min()),
        "max": float(col.max()),
    }


def apply_vectorized_string_methods(
    df: pd.DataFrame, str_col: str
) -> Tuple[pd.Series, pd.Series]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> vector_math_and_string_methods.py]
    Applies vectorized string methods (.str.upper(), .str.contains()) to a text column.

    Args:
        df (pd.DataFrame): Input DataFrame.
        str_col (str): Target text column label.

    Returns:
        Tuple[pd.Series, pd.Series]: Uppercased Series and boolean regex match mask.
    """
    uppercased: pd.Series = df[str_col].str.upper()
    contains_e: pd.Series = df[str_col].str.contains("e|E", regex=True)
    return uppercased, contains_e


def calculate_group_aggregations(
    df: pd.DataFrame, group_col: str, target_col: str
) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> vector_math_and_string_methods.py]
    Groups data by a categorical column and applies multi-metric aggregations (.groupby().agg()).

    Args:
        df (pd.DataFrame): Input DataFrame.
        group_col (str): Column to group by.
        target_col (str): Numeric column to aggregate.

    Returns:
        pd.DataFrame: Aggregated summary table.
    """
    grouped: pd.DataFrame = (
        df.groupby(group_col)[target_col].agg(["count", "mean", "sum"]).reset_index()
    )
    return grouped


def save_and_load_csv(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_io_and_persistence.py]
    Exports DataFrame to CSV format (df.to_csv) and reloads it (pd.read_csv).

    Args:
        df (pd.DataFrame): Input DataFrame.
        file_path (Path): File path destination.

    Returns:
        pd.DataFrame: Reloaded DataFrame.
    """
    df.to_csv(file_path, index=False)
    reloaded: pd.DataFrame = pd.read_csv(file_path)
    return reloaded


def save_and_load_json(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_io_and_persistence.py]
    Exports DataFrame to JSON format (df.to_json) and reloads it (pd.read_json).

    Args:
        df (pd.DataFrame): Input DataFrame.
        file_path (Path): File path destination.

    Returns:
        pd.DataFrame: Reloaded DataFrame.
    """
    df.to_json(file_path, orient="records", indent=2)
    reloaded: pd.DataFrame = pd.read_json(file_path)
    return reloaded


def save_and_load_pickle(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> dataframe_io_and_persistence.py]
    Exports DataFrame to binary Pickle format (df.to_pickle) and reloads it (pd.read_pickle).

    Args:
        df (pd.DataFrame): Input DataFrame.
        file_path (Path): File path destination.

    Returns:
        pd.DataFrame: Reloaded DataFrame.
    """
    df.to_pickle(file_path)
    reloaded: pd.DataFrame = pd.read_pickle(file_path)
    return reloaded


# ─── SUBFOLDER 3: 03-RANGE-EVOLUTION-AND-PERFORMANCE ──────────────────────────


def generate_python_range(start: int, stop: int, step: int = 1) -> range:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> date_range_vs_python_range.py]
    Generates a standard Python built-in range object.

    Args:
        start (int): Start integer boundary.
        stop (int): Exclusive stop boundary.
        step (int, optional): Step delta. Defaults to 1.

    Returns:
        range: Standard range sequence.
    """
    return range(start, stop, step)


def generate_pandas_date_range(
    start: str,
    periods: Optional[int] = None,
    end: Optional[str] = None,
    freq: str = "D",
) -> pd.DatetimeIndex:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> date_range_vs_python_range.py]
    Generates a Pandas DatetimeIndex sequence using pd.date_range().

    Args:
        start (str): Start ISO date string.
        periods (Optional[int], optional): Number of timestamps. Defaults to None.
        end (Optional[str], optional): End ISO date string. Defaults to None.
        freq (str, optional): Frequency alias ('D', 'B', 'ME', 'h'). Defaults to "D".

    Returns:
        pd.DatetimeIndex: Generated timestamp sequence.
    """
    return pd.date_range(start=start, end=end, periods=periods, freq=freq)


def generate_pandas_range_index(start: int, stop: int, step: int = 1) -> pd.RangeIndex:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> date_range_vs_python_range.py]
    Creates an optimized Pandas RangeIndex sequence.

    Args:
        start (int): Start integer.
        stop (int): Stop integer.
        step (int, optional): Step increment. Defaults to 1.

    Returns:
        pd.RangeIndex: Memory-efficient RangeIndex object.
    """
    return pd.RangeIndex(start=start, stop=stop, step=step)


def measure_category_memory_savings(num_rows: int = 100_000) -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> pandas_performance_and_evolution.py]
    Benchmarks RAM memory usage between object (string) column vs category column (.astype('category')).

    Args:
        num_rows (int, optional): Row count. Defaults to 100,000.

    Returns:
        Dict[str, Any]: RAM footprint bytes and percentage savings.
    """
    categories: List[str] = ["Engineering", "Marketing", "HR", "Sales", "Finance"] * (
        num_rows // 5
    )
    df_obj: pd.DataFrame = pd.DataFrame({"Dept": categories})

    df_cat: pd.DataFrame = df_obj.copy()
    df_cat["Dept"] = df_cat["Dept"].astype("category")

    mem_obj: int = int(df_obj.memory_usage(deep=True).sum())
    mem_cat: int = int(df_cat.memory_usage(deep=True).sum())

    return {
        "object_dtype_bytes": mem_obj,
        "category_dtype_bytes": mem_cat,
        "memory_savings_percent": round((1 - mem_cat / mem_obj) * 100, 2),
    }


def benchmark_pandas_vectorization(num_rows: int = 200_000) -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> pandas_performance_and_evolution.py]
    Benchmarks column summation performance between standard Python loop iteration and Pandas vectorized sum.

    Args:
        num_rows (int, optional): Row count. Defaults to 200,000.

    Returns:
        Dict[str, Any]: Execution times in seconds and speedup factor.
    """
    s: pd.Series = pd.Series(range(num_rows), dtype="float64")

    # Python loop iteration sum
    start_py: float = time.perf_counter()
    py_total: float = 0.0
    for val in s:
        py_total += val
    time_py: float = time.perf_counter() - start_py

    # Pandas vectorized C sum
    start_pd: float = time.perf_counter()
    _ = s.sum()
    time_pd: float = time.perf_counter() - start_pd

    speedup: float = round(time_py / time_pd, 2) if time_pd > 0 else 0.0

    return {
        "python_loop_seconds": time_py,
        "pandas_vectorized_seconds": time_pd,
        "speedup_factor": speedup,
    }


def get_version_evolution_matrix() -> Dict[str, str]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> pandas_performance_and_evolution.py]
    Provides detailed Python version evolution matrix (Python 3.3 to Python 3.13) with Pandas.

    Returns:
        Dict[str, str]: Evolution matrix map.
    """
    return {
        "Python 3.3": "Lazy range sequence slicing range(100)[::2]; yield from generator delegation in Pandas readers.",
        "Python 3.4": "pathlib module introduced; enabling path objects in pd.read_csv(Path('data.csv')).",
        "Python 3.5": "Matrix multiplication operator (@) supported for DataFrame.__matmul__ and Series.__matmul__.",
        "Python 3.6": "F-strings syntax for inline DataFrame formatting; ordered keyword kwargs in pd.DataFrame(a=1, b=2).",
        "Python 3.7": "CPython core opcode optimizations accelerating series aggregation loops and dict iteration.",
        "Python 3.8": "Positional-only parameters (/) and Walrus operator (:=) for inline DataFrame filtering.",
        "Python 3.9": "Dictionary union operators (| and |=); built-in type hints (pd.Series[int]) integration.",
        "Python 3.10": "Structural Pattern Matching (match/case PEP 634) over DataFrame column names and shapes.",
        "Python 3.11": "Specializing Adaptive Interpreter (PEP 659) accelerates binary loop dispatches by 10-25%.",
        "Python 3.12": "Per-interpreter GIL and detailed traceback error indicators highlighting failing loc/iloc slices.",
        "Python 3.13": "Free-threaded CPython (PEP 703 - GIL removal) and Tier 2 JIT for parallel multi-threaded Pandas pipelines.",
    }


def introspect_series_attributes(s: pd.Series) -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> reflection_and_introspection.py]
    Inspects running attributes (.index, .values, .dtype, .shape, .size, .name) and methods (.unique(), .value_counts()) on Series.

    Args:
        s (pd.Series): Input Series.

    Returns:
        Dict[str, Any]: Reflection metadata dictionary.
    """
    public_attrs: List[str] = [attr for attr in dir(s) if not attr.startswith("_")]

    return {
        "public_attribute_count": len(public_attrs),
        "sample_attributes": public_attrs[:15],
        "name": s.name,
        "dtype": str(s.dtype),
        "shape": s.shape,
        "size": s.size,
        "unique_values": s.unique().tolist(),
        "nunique_count": int(s.nunique()),
        "value_counts": s.value_counts().to_dict(),
        "has_na": bool(s.isna().any()),
        "summary": s.describe().to_dict(),
    }


def introspect_dataframe_attributes(df: pd.DataFrame) -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> reflection_and_introspection.py]
    Inspects running attributes (.columns, .index, .dtypes, .shape, .size, .T) and methods (.drop(), .fillna()) on DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        Dict[str, Any]: Reflection metadata dictionary.
    """
    public_attrs: List[str] = [attr for attr in dir(df) if not attr.startswith("_")]
    transposed_shape: Tuple[int, ...] = df.T.shape
    dropped_col_df: pd.DataFrame = df.drop(columns=[df.columns[0]])

    return {
        "public_attribute_count": len(public_attrs),
        "sample_attributes": public_attrs[:15],
        "shape": df.shape,
        "size": df.size,
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "transposed_shape": transposed_shape,
        "dropped_column_names": list(dropped_col_df.columns),
        "memory_usage_bytes": int(df.memory_usage(deep=True).sum()),
    }


def run_all_pandas_module_demos() -> Dict[str, Any]:
    """
    Executes all 3 subfolder Pandas curriculum demonstrations in sequence.

    Returns:
        Dict[str, Any]: Consolidated outputs across all 3 steps.
    """
    emp_df: pd.DataFrame = create_sample_dataframe()
    sample_s: pd.Series = create_series_from_dict()
    head_df, tail_df = get_preview_slices(emp_df, 2)
    up_names, has_e = apply_vectorized_string_methods(emp_df, "Name")

    return {
        "01_fundamentals": {
            "series_list": create_series_from_list(),
            "series_custom": create_series_with_custom_index(),
            "series_dict": sample_s,
            "series_meta": inspect_series_metadata(sample_s),
            "sample_df": emp_df,
            "df_meta": inspect_dataframe_metadata(emp_df),
            "casted_df": cast_column_dtypes(emp_df),
        },
        "02_advanced_math": {
            "preview_head": head_df,
            "preview_tail": tail_df,
            "loc_slice": select_by_label(emp_df, 0, 2, ["Name", "Salary"]),
            "iloc_slice": select_by_position(emp_df, slice(0, 3), slice(1, 4)),
            "boolean_mask": filter_by_boolean_condition(emp_df, 70000.0),
            "query_filter": filter_using_query(emp_df, "Engineering", 4.5),
            "stats": compute_column_statistics(emp_df, "Salary"),
            "string_upper": up_names,
            "string_has_e": has_e,
            "groupby_summary": calculate_group_aggregations(
                emp_df, "Department", "Salary"
            ),
        },
        "03_range_performance": {
            "py_range": list(generate_python_range(1, 10, 2)),
            "date_range_daily": generate_pandas_date_range(
                "2026-01-01", periods=5, freq="D"
            ),
            "date_range_business": generate_pandas_date_range(
                "2026-01-01", periods=5, freq="B"
            ),
            "range_index": generate_pandas_range_index(0, 100, 5),
            "category_memory": measure_category_memory_savings(10_000),
            "vector_benchmark": benchmark_pandas_vectorization(50_000),
            "evolution_matrix": get_version_evolution_matrix(),
            "series_introspection": introspect_series_attributes(sample_s),
            "dataframe_introspection": introspect_dataframe_attributes(emp_df),
        },
    }


def run_pandas_curriculum_demo() -> None:
    """Execute master pedagogical demonstration across all 3 steps to stdout."""
    print("=" * 65)
    print(" STEP 1: PANDAS FUNDAMENTALS (SERIES & DATAFRAMES)")
    print("=" * 65)
    s_custom = create_series_with_custom_index()
    print("Series with Custom Index:\n", s_custom)

    emp_df = create_sample_dataframe()
    print("\nSample Employee DataFrame:\n", emp_df)
    meta = inspect_dataframe_metadata(emp_df)
    print(
        f"DataFrame Metadata -> Shape: {meta['shape']}, Total Memory: {meta['total_memory_bytes']} bytes"
    )

    print("\n" + "=" * 65)
    print(" STEP 2: ADVANCED MATH, SLICING & STRING METHODS")
    print("=" * 65)
    loc_slice = select_by_label(emp_df, 0, 2, ["Name", "Salary", "Department"])
    print("Label Slicing .loc[0:2]:\n", loc_slice)

    high_sal = filter_by_boolean_condition(emp_df, 70000.0)
    print("\nBoolean Masking (Salary > 70,000):\n", high_sal)

    sal_stats = compute_column_statistics(emp_df, "Salary")
    print(
        f"\nSalary Aggregations -> Sum: {sal_stats['sum']:,.2f}, Mean: {sal_stats['mean']:,.2f}"
    )

    up_names, _ = apply_vectorized_string_methods(emp_df, "Name")
    print("\nVectorized String Method (.str.upper()):\n", up_names.values)

    print("\n" + "=" * 65)
    print(" STEP 3: RANGE EVOLUTION, MEMORY OPTIMIZATION & REFLECTION")
    print("=" * 65)
    d_rng = generate_pandas_date_range("2026-01-01", periods=5, freq="B")
    print("Business Date Range (pd.date_range freq='B'):\n", d_rng)

    mem_savings = measure_category_memory_savings(100_000)
    print(
        f"\nCategory Memory Reduction: {mem_savings['memory_savings_percent']}% RAM Savings"
    )

    df_info = introspect_dataframe_attributes(emp_df)
    print(
        f"Public pd.DataFrame Attributes/Methods Count: {df_info['public_attribute_count']}"
    )
    print("=" * 65)


if __name__ == "__main__":
    run_pandas_curriculum_demo()
