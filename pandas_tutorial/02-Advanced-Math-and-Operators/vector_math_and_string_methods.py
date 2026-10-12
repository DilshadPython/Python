"""
Pandas Vector Math, String Accessor Methods, and Aggregations Module.

This module demonstrates:
- Column-wise vector arithmetic (bonus calculation, normalized metrics).
- Statistical aggregations (.sum(), .mean(), .std(), .median()).
- Vectorized string accessor methods (.str.upper(), .str.contains(), .str.replace()).
- Grouping aggregations via .groupby().
"""

# Import pandas for vector math and aggregation routines
import pandas as pd


def compute_column_statistics(df: pd.DataFrame, num_col: str) -> dict[str, float]:
    """Compute statistical summaries for a numeric DataFrame column.

    Args:
        df (pd.DataFrame): Input DataFrame.
        num_col (str): Numeric column name.

    Returns:
        dict[str, float]: Calculated statistics (sum, mean, std, median, min, max).
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


def apply_vectorized_string_methods(df: pd.DataFrame, str_col: str) -> tuple[pd.Series, pd.Series]:
    """Perform vectorized string operations on a text column.

    Args:
        df (pd.DataFrame): Input DataFrame.
        str_col (str): Text column name.

    Returns:
        tuple[pd.Series, pd.Series]:
            - Uppercased text series.
            - Boolean mask matching sub-string condition.
    """
    uppercased = df[str_col].str.upper()
    contains_e = df[str_col].str.contains("e|E", regex=True)
    return uppercased, contains_e


def calculate_group_aggregations(df: pd.DataFrame, group_col: str, target_col: str) -> pd.DataFrame:
    """Group rows by a categorical column and compute mean and sum metrics.

    Args:
        df (pd.DataFrame): Input DataFrame.
        group_col (str): Column name to group by.
        target_col (str): Numeric target column to aggregate.

    Returns:
        pd.DataFrame: Aggregated summary table.
    """
    grouped = df.groupby(group_col)[target_col].agg(["count", "mean", "sum"]).reset_index()
    return grouped


if __name__ == "__main__":
    data = {
        "EmployeeID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
        "Salary": [85000.0, 62000.0, 95000.0, 58000.0, 67000.0],
    }
    emp_df = pd.DataFrame(data)

    print("--- Salary Column Statistics ---")
    stats = compute_column_statistics(emp_df, "Salary")
    for k, v in stats.items():
        print(f"{k:10s}: {v:12.2f}")

    up_names, has_e = apply_vectorized_string_methods(emp_df, "Name")
    print("\n--- Vectorized String .str.upper() ---")
    print(up_names)

    dept_summary = calculate_group_aggregations(emp_df, "Department", "Salary")
    print("\n--- Groupby Department Summary ---")
    print(dept_summary)
