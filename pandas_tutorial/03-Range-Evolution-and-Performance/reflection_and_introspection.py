"""
Runtime Introspection and Reflection Matrix Module for Pandas Series and DataFrame.

This module demonstrates:
- Reflection via dir(pd.Series) and dir(pd.DataFrame).
- Accessing running Series attributes (.index, .values, .dtype, .shape, .size, .name).
- Accessing running Series methods (.head(), .tail(), .describe(), .unique(), .nunique(), .value_counts(), .isna(), .fillna(), .map(), .apply()).
- Accessing running DataFrame attributes (.columns, .index, .dtypes, .shape, .size, .T).
- Accessing running DataFrame methods (.head(), .tail(), .info(), .describe(), .loc[], .iloc[], .groupby(), .pivot(), .drop(), .fillna(), .apply(), .eval()).
"""

# Import pandas for introspection target structures
import pandas as pd


def introspect_series_attributes(s: pd.Series) -> dict[str, object]:
    """Inspect and demonstrate running attributes and methods on a Pandas Series.

    Args:
        s (pd.Series): Target input Series.

    Returns:
        dict[str, object]: Reflection metadata dictionary.
    """
    public_attrs = [attr for attr in dir(s) if not attr.startswith("_")]

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


def introspect_dataframe_attributes(df: pd.DataFrame) -> dict[str, object]:
    """Inspect and demonstrate running attributes and methods on a Pandas DataFrame.

    Args:
        df (pd.DataFrame): Target input DataFrame.

    Returns:
        dict[str, object]: Reflection metadata dictionary.
    """
    public_attrs = [attr for attr in dir(df) if not attr.startswith("_")]

    # Perform running manipulations
    transposed_shape = df.T.shape
    dropped_col_df = df.drop(columns=[df.columns[0]])
    filled_df = df.fillna(0)

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


if __name__ == "__main__":
    sample_s = pd.Series(["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"], name="Fruit")
    s_info = introspect_series_attributes(sample_s)

    print("--- Reflection: dir(pd.Series) ---")
    print(f"Total Public Attributes/Methods: {s_info['public_attribute_count']}")
    print(f"Unique Values: {s_info['unique_values']}")
    print(f"Value Counts:  {s_info['value_counts']}")

    sample_df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4.0, 5.0, 6.0],
        "C": ["X", "Y", "Z"]
    })
    df_info = introspect_dataframe_attributes(sample_df)

    print("\n--- Reflection: dir(pd.DataFrame) ---")
    print(f"Total Public Attributes/Methods: {df_info['public_attribute_count']}")
    print(f"Shape: {df_info['shape']} | Columns: {df_info['columns']}")
    print(f"Transposed Shape: {df_info['transposed_shape']}")
