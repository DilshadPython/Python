"""
Pandas DataFrame Creation and Metadata Introspection Module.

This module demonstrates:
- Constructing 2D DataFrames from dictionaries of lists, lists of dicts, and NumPy arrays.
- Inspecting columns, index labels, shape, dtypes, and memory usage.
- Data type conversion using .astype() and downcasting.
- Exporting summary statistics via .describe() and schema via .info().
"""

# Import numpy for numerical matrix creation
import numpy as np

# Import pandas for DataFrame table manipulation
import pandas as pd


def create_sample_dataframe() -> pd.DataFrame:
    """Create a structured sample DataFrame containing employee records.

    Returns:
        pd.DataFrame: 2D table with columns (EmployeeID, Name, Department, Salary, Rating).
    """
    raw_data = {
        "EmployeeID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
        "Salary": [85000.0, 62000.0, 95000.0, 58000.0, 67000.0],
        "Rating": [4.8, 4.2, 4.9, 3.8, 4.5],
    }
    df: pd.DataFrame = pd.DataFrame(raw_data)
    return df


def inspect_dataframe_metadata(df: pd.DataFrame) -> dict[str, object]:
    """Extract structural and memory metadata from a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        dict[str, object]: Metadata dictionary (shape, columns, dtypes, memory_bytes).
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
    """Demonstrate data type casting on DataFrame columns.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Copy of DataFrame with updated column dtypes.
    """
    updated_df = df.copy()
    updated_df["EmployeeID"] = updated_df["EmployeeID"].astype(np.int32)
    updated_df["Department"] = updated_df["Department"].astype("category")
    return updated_df


if __name__ == "__main__":
    emp_df = create_sample_dataframe()
    print("--- Sample Employee DataFrame ---")
    print(emp_df)

    print("\n--- Metadata Introspection ---")
    meta = inspect_dataframe_metadata(emp_df)
    for k, v in meta.items():
        print(f"{k:20s}: {v}")

    print("\n--- DataFrame Statistical Summary (.describe()) ---")
    print(emp_df.describe())

    casted_df = cast_column_dtypes(emp_df)
    print("\n--- Updated Column Types ---")
    print(casted_df.dtypes)
