"""
Pandas DataFrame I/O and Persistence Module.

This module demonstrates:
- Saving and loading CSV files (pd.read_csv, df.to_csv).
- Saving and loading JSON formats (pd.read_json, df.to_json).
- Saving and loading Pickle serialization (pd.read_pickle, df.to_pickle).
"""

# Import pathlib for file management
from pathlib import Path

# Import pandas for data export and import functions
import pandas as pd


def save_and_load_csv(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """Export DataFrame to CSV format and reload it.

    Args:
        df (pd.DataFrame): Input DataFrame.
        file_path (Path): Target file path destination.

    Returns:
        pd.DataFrame: Reloaded DataFrame from CSV.
    """
    df.to_csv(file_path, index=False)
    reloaded: pd.DataFrame = pd.read_csv(file_path)
    return reloaded


def save_and_load_json(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """Export DataFrame to JSON format and reload it.

    Args:
        df (pd.DataFrame): Input DataFrame.
        file_path (Path): Target file path destination.

    Returns:
        pd.DataFrame: Reloaded DataFrame from JSON.
    """
    df.to_json(file_path, orient="records", indent=2)
    reloaded: pd.DataFrame = pd.read_json(file_path)
    return reloaded


def save_and_load_pickle(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
    """Export DataFrame to binary Pickle format and reload it.

    Args:
        df (pd.DataFrame): Input DataFrame.
        file_path (Path): Target file path destination.

    Returns:
        pd.DataFrame: Reloaded DataFrame from Pickle.
    """
    df.to_pickle(file_path)
    reloaded: pd.DataFrame = pd.read_pickle(file_path)
    return reloaded


if __name__ == "__main__":
    sample_df = pd.DataFrame({
        "ID": [1, 2, 3],
        "Item": ["Laptop", "Monitor", "Keyboard"],
        "Price": [1200.0, 350.0, 85.0]
    })

    temp_dir = Path("./temp_pandas_io")
    temp_dir.mkdir(exist_ok=True)

    csv_path = temp_dir / "sample.csv"
    json_path = temp_dir / "sample.json"
    pickle_path = temp_dir / "sample.pkl"

    try:
        csv_df = save_and_load_csv(sample_df, csv_path)
        json_df = save_and_load_json(sample_df, json_path)
        pickle_df = save_and_load_pickle(sample_df, pickle_path)

        print("--- CSV Persistence Check ---")
        print(csv_df)
        print("--- JSON Persistence Check ---")
        print(json_df)
        print("--- Pickle Persistence Check ---")
        print(pickle_df)
    finally:
        csv_path.unlink(missing_ok=True)
        json_path.unlink(missing_ok=True)
        pickle_path.unlink(missing_ok=True)
        temp_dir.rmdir()
