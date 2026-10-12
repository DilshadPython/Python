"""
Pandas Series Creation and Indexing Fundamentals Module.

This module demonstrates:
- Constructing Pandas Series objects from Python lists, dictionaries, NumPy arrays, and scalars.
- Custom index label assignment.
- Accessing fundamental attributes: .index, .values, .dtype, .shape, .size.
- Position-based and label-based Series indexing.
"""

# Import numpy for numeric array conversions
import numpy as np

# Import pandas for high-performance Series data structure manipulation
import pandas as pd


def create_series_from_list() -> pd.Series:
    """Create a Pandas Series from a standard Python list.

    Returns:
        pd.Series: Integer series with default RangeIndex (0..N-1).
    """
    data = [10, 20, 30, 40, 50]
    series: pd.Series = pd.Series(data, name="IntegerSequence")
    return series


def create_series_with_custom_index() -> pd.Series:
    """Create a Pandas Series with custom string index labels.

    Returns:
        pd.Series: Floating-point series indexed by city names.
    """
    temperatures = [22.5, 18.0, 31.2, 15.4]
    cities = ["London", "Paris", "Tokyo", "Berlin"]
    series: pd.Series = pd.Series(temperatures, index=cities, name="Temperature_Celsius")
    return series


def create_series_from_dict() -> pd.Series:
    """Create a Pandas Series from a Python dictionary (keys become index labels).

    Returns:
        pd.Series: Series initialized from key-value pairs.
    """
    fruit_stock = {"Apples": 150, "Bananas": 300, "Oranges": 200, "Grapes": 90}
    series: pd.Series = pd.Series(fruit_stock, name="FruitInventory")
    return series


def inspect_series_metadata(series: pd.Series) -> dict[str, object]:
    """Extract metadata attributes from a Pandas Series object.

    Args:
        series (pd.Series): Target input series.

    Returns:
        dict[str, object]: Dictionary of attributes (.index, .values, .dtype, .shape, .size).
    """
    return {
        "name": series.name,
        "dtype": str(series.dtype),
        "shape": series.shape,
        "size": series.size,
        "index_type": type(series.index).__name__,
        "has_nulls": bool(series.isnull().any()),
    }


if __name__ == "__main__":
    s_list = create_series_from_list()
    s_custom = create_series_with_custom_index()
    s_dict = create_series_from_dict()

    print("--- Series from List ---")
    print(s_list)

    print("\n--- Series with Custom Index ---")
    print(s_custom)
    print("Paris Temperature:", s_custom["Paris"])

    print("\n--- Series Metadata Introspection ---")
    for k, v in inspect_series_metadata(s_custom).items():
        print(f"{k:15s}: {v}")
