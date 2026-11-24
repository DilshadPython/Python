"""
Master Executable Script for Pandas Tutorial Module.

This script executes and demonstrates all three curriculum steps:
- Step 1: 01-Fundamentals (Series creation, DataFrames, metadata inspection).
- Step 2: 02-Advanced-Math-and-Operators (Slicing, loc/iloc, vector math, string methods).
- Step 3: 03-Range-Evolution-and-Performance (date_range, category memory savings, reflection).
"""

# Import pathlib and sys to configure folder import paths
from pathlib import Path
import sys

# Ensure subfolder modules can be imported directly
BASE_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(BASE_DIR / "01-Fundamentals"))
sys.path.insert(0, str(BASE_DIR / "02-Advanced-Math-and-Operators"))
sys.path.insert(0, str(BASE_DIR / "03-Range-Evolution-and-Performance"))

# Import pandas for data manipulation
import pandas as pd

# Import Step 1 functions
from dataframe_creation_and_metadata import create_sample_dataframe, inspect_dataframe_metadata
from series_creation_and_indexing import create_series_from_dict, create_series_with_custom_index

# Import Step 2 functions
from dataframe_slicing_and_indexing import filter_by_boolean_condition, select_by_label
from vector_math_and_string_methods import apply_vectorized_string_methods, compute_column_statistics

# Import Step 3 functions
from date_range_vs_python_range import generate_pandas_date_range
from pandas_performance_and_evolution import measure_category_memory_savings
from reflection_and_introspection import introspect_dataframe_attributes


def run_pandas_curriculum_demo() -> None:
    """Execute master pedagogical demonstration across all 3 steps."""
    print("=" * 65)
    print(" STEP 1: PANDAS FUNDAMENTALS (SERIES & DATAFRAMES)")
    print("=" * 65)
    s_custom = create_series_with_custom_index()
    print("Series with Custom Index:\n", s_custom)

    emp_df = create_sample_dataframe()
    print("\nSample Employee DataFrame:\n", emp_df)
    meta = inspect_dataframe_metadata(emp_df)
    print(f"DataFrame Metadata -> Shape: {meta['shape']}, Total Memory: {meta['total_memory_bytes']} bytes")

    print("\n" + "=" * 65)
    print(" STEP 2: ADVANCED MATH, SLICING & STRING METHODS")
    print("=" * 65)
    loc_slice = select_by_label(emp_df, 0, 2, ["Name", "Salary", "Department"])
    print("Label Slicing .loc[0:2]:\n", loc_slice)

    high_sal = filter_by_boolean_condition(emp_df, 70000.0)
    print("\nBoolean Masking (Salary > 70,000):\n", high_sal)

    sal_stats = compute_column_statistics(emp_df, "Salary")
    print(f"\nSalary Aggregations -> Sum: {sal_stats['sum']:,.2f}, Mean: {sal_stats['mean']:,.2f}")

    up_names, _ = apply_vectorized_string_methods(emp_df, "Name")
    print("\nVectorized String Method (.str.upper()):\n", up_names.values)

    print("\n" + "=" * 65)
    print(" STEP 3: RANGE EVOLUTION, MEMORY OPTIMIZATION & REFLECTION")
    print("=" * 65)
    d_rng = generate_pandas_date_range("2026-01-01", periods=5, freq="B")
    print("Business Date Range (pd.date_range freq='B'):\n", d_rng)

    mem_savings = measure_category_memory_savings(100_000)
    print(f"\nCategory Memory Reduction: {mem_savings['memory_savings_percent']}% RAM Savings")

    df_info = introspect_dataframe_attributes(emp_df)
    print(f"Public pd.DataFrame Attributes/Methods Count: {df_info['public_attribute_count']}")
    print("=" * 65)


if __name__ == "__main__":
    run_pandas_curriculum_demo()
