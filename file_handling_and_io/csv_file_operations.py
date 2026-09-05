"""
File Handling & I/O: Structured CSV File Operations

This module demonstrates reading and writing structured CSV (Comma Separated Values) files
using Python's built-in `csv` module:
- `csv.reader` and `csv.writer`: Positional list-based row parsing.
- `csv.DictReader` and `csv.DictWriter`: Dictionary-based header-mapped row parsing.
- Row filtering and sorting using `sorted()` with lambda key functions.
"""
import csv
import os
from typing import List, Dict, Any


def write_csv_rows(filepath: str, headers: List[str], rows: List[List[Any]]) -> None:
    """
    Writes a list of positional row data to a CSV file using `csv.writer`.

    Args:
        filepath (str): Target CSV file path.
        headers (List[str]): Column header names.
        rows (List[List[Any]]): Data rows.
    """
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def read_csv_dict(filepath: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file into a list of dictionaries using `csv.DictReader`.

    Args:
        filepath (str): Target CSV file path.

    Returns:
        List[Dict[str, str]]: List of row dictionaries keyed by column headers.
    """
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


def sort_csv_records_by_field(records: List[Dict[str, str]], field_name: str, reverse: bool = False) -> List[Dict[str, str]]:
    """
    Sorts a list of dictionary records by a specific field key using lambda sorting.

    Args:
        records (List[Dict[str, str]]): List of CSV dict records.
        field_name (str): Key to sort by.
        reverse (bool): Descending order flag if True.

    Returns:
        List[Dict[str, str]]: Sorted records list.
    """
    return sorted(records, key=lambda x: x.get(field_name, ""), reverse=reverse)


def main() -> None:
    """Demonstrates CSV file operations."""
    print("=" * 60)
    print("3. Structured CSV Operations (`csv.writer`, `DictReader`, lambda sorting)")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "sample_data.csv")

    headers = ["Name", "City", "Age", "Role"]
    data_rows = [
        ["Alice", "London", "30", "Engineer"],
        ["Bob", "Tokyo", "25", "Designer"],
        ["Charlie", "New York", "35", "Manager"],
        ["Diana", "Berlin", "28", "Developer"],
    ]

    # 1. Write CSV rows
    write_csv_rows(csv_file, headers, data_rows)
    print(f"\n1. Wrote {len(data_rows)} data rows to {csv_file}")

    # 2. Read as DictReader
    records = read_csv_dict(csv_file)
    print(f"2. Parsed {len(records)} dict records via `csv.DictReader`:")
    for rec in records:
        print(f"   {rec}")

    # 3. Sort by Name using lambda
    sorted_records = sort_csv_records_by_field(records, "Age", reverse=True)
    print("\n3. Records sorted by 'Age' descending (lambda key):")
    for r in sorted_records:
        print(f"   Name: {r['Name']}, Age: {r['Age']}, Role: {r['Role']}")


if __name__ == "__main__":
    main()
