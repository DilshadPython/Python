"""
Pandas DataFrame Slicing, Selection, and Masking Module.

This module demonstrates:
- Previewing datasets using .head() and .tail().
- Label-based indexing using .loc[row_label, col_label].
- Integer position indexing using .iloc[row_idx, col_idx].
- Conditional boolean masking (e.g., df[df['Salary'] > 65000]).
- Dynamic filtering using .query().
"""

# Import pandas for DataFrame selection operations
import pandas as pd


def get_preview_slices(df: pd.DataFrame, n: int = 2) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return top N rows (.head) and bottom N rows (.tail) of a DataFrame.

    Args:
        df (pd.DataFrame): Target input DataFrame.
        n (int, optional): Number of rows to slice. Defaults to 2.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: Top slice and bottom slice.
    """
    return df.head(n), df.tail(n)


def select_by_label(df: pd.DataFrame, row_start: int, row_end: int, columns: list[str]) -> pd.DataFrame:
    """Select rows and specific columns using label-based indexing (.loc).

    Args:
        df (pd.DataFrame): Input DataFrame.
        row_start (int): Start row index label.
        row_end (int): End row index label.
        columns (list[str]): List of column names to select.

    Returns:
        pd.DataFrame: Label-indexed sub-DataFrame.
    """
    return df.loc[row_start:row_end, columns]


def select_by_position(df: pd.DataFrame, row_slice: slice, col_slice: slice) -> pd.DataFrame:
    """Select rows and columns using integer position indexing (.iloc).

    Args:
        df (pd.DataFrame): Input DataFrame.
        row_slice (slice): Row position slice range.
        col_slice (slice): Column position slice range.

    Returns:
        pd.DataFrame: Position-indexed sub-DataFrame.
    """
    return df.iloc[row_slice, col_slice]


def filter_by_boolean_condition(df: pd.DataFrame, min_salary: float) -> pd.DataFrame:
    """Filter DataFrame rows using a boolean condition mask on Salary.

    Args:
        df (pd.DataFrame): Input DataFrame.
        min_salary (float): Salary threshold limit.

    Returns:
        pd.DataFrame: Filtered DataFrame containing rows where Salary > min_salary.
    """
    mask = df["Salary"] > min_salary
    return df[mask]


def filter_using_query(df: pd.DataFrame, department: str, min_rating: float) -> pd.DataFrame:
    """Filter DataFrame rows using expression query method (.query()).

    Args:
        df (pd.DataFrame): Input DataFrame.
        department (str): Target department name.
        min_rating (float): Minimum performance rating.

    Returns:
        pd.DataFrame: Query-filtered DataFrame.
    """
    return df.query("Department == @department and Rating >= @min_rating")


if __name__ == "__main__":
    data = {
        "EmployeeID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
        "Salary": [85000.0, 62000.0, 95000.0, 58000.0, 67000.0],
        "Rating": [4.8, 4.2, 4.9, 3.8, 4.5],
    }
    emp_df = pd.DataFrame(data)

    head_df, tail_df = get_preview_slices(emp_df, 2)
    print("--- Head (2 rows) ---")
    print(head_df)

    loc_df = select_by_label(emp_df, 0, 2, ["Name", "Salary"])
    print("\n--- .loc[0:2, ['Name', 'Salary']] ---")
    print(loc_df)

    iloc_df = select_by_position(emp_df, slice(1, 4), slice(0, 3))
    print("\n--- .iloc[1:4, 0:3] ---")
    print(iloc_df)

    high_salary_df = filter_by_boolean_condition(emp_df, 65000.0)
    print("\n--- Boolean Mask (Salary > 65k) ---")
    print(high_salary_df)

    query_df = filter_using_query(emp_df, "Engineering", 4.5)
    print("\n--- Query (.query('Department == Engineering and Rating >= 4.5')) ---")
    print(query_df)
