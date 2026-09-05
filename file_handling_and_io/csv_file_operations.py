"""
File Handling & I/O: Structured CSV File Operations & Stock Analysis

This module demonstrates reading and writing structured CSV (Comma Separated Values) files
using Python's built-in `csv` module:
- `csv.reader` and `csv.writer`: Positional list-based row parsing.
- `csv.DictReader` and `csv.DictWriter`: Dictionary-based header-mapped row parsing.
- Real-world financial stock analysis (`google.csv`) and geographical city dataset parsing (`dict_city.csv`).
- Row filtering and sorting using `sorted()` with lambda key functions.
"""
import csv
import os
from typing import List, Dict, Any, Tuple


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


def analyze_google_stock_csv(filepath: str) -> Dict[str, Any]:
    """
    Parses `google.csv` stock historical data and calculates key market metrics.

    Args:
        filepath (str): Path to google.csv stock dataset.

    Returns:
        Dict[str, Any]: Financial metrics (total_days, max_close, min_close, avg_close).
    """
    if not os.path.exists(filepath):
        return {"error": f"File {filepath} not found"}

    closing_prices: List[float] = []
    total_volume = 0

    with open(filepath, "r", newline="", encoding="utf-8") as f:
        content = f.read().strip()
        # Clean byte string wrapper if file contains b'...' format
        if content.startswith("b'") or content.startswith('b"'):
            content = content[2:-1]
        content = content.replace("\\n", "\n").replace("\\r", "")

        lines = [line.strip() for line in content.splitlines() if line.strip()]
        reader = csv.DictReader(lines)
        for row in reader:
            close_str = row.get("Close")
            vol_str = row.get("Volume")
            if close_str is not None and vol_str is not None:
                try:
                    close_val = float(close_str)
                    vol_val = int(vol_str)
                    closing_prices.append(close_val)
                    total_volume += vol_val
                except ValueError:
                    continue

    if not closing_prices:
        return {"error": "No valid stock records parsed"}

    return {
        "total_days": len(closing_prices),
        "max_close": max(closing_prices),
        "min_close": min(closing_prices),
        "avg_close": sum(closing_prices) / len(closing_prices),
        "total_volume": total_volume,
    }


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
    """Demonstrates CSV file operations and dataset analysis."""
    print("=" * 60)
    print("3. Structured CSV Operations & Financial Dataset Analysis")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_csv = os.path.join(base_dir, "sample_data.csv")
    google_csv = os.path.join(base_dir, "google.csv")

    # 1. Custom CSV Writing
    headers = ["Name", "City", "Age", "Role"]
    data_rows = [
        ["Alice", "London", "30", "Engineer"],
        ["Bob", "Tokyo", "25", "Designer"],
        ["Charlie", "New York", "35", "Manager"],
    ]
    write_csv_rows(sample_csv, headers, data_rows)
    print(f"\n1. Wrote {len(data_rows)} custom rows to {sample_csv}")

    # 2. Read as DictReader
    records = read_csv_dict(sample_csv)
    print(f"2. Parsed DictReader records ({len(records)} items):")
    for rec in records:
        print(f"   {rec}")

    # 3. Financial Analysis of Google Stock Data
    print("\n3. Analyzing `google.csv` Stock Dataset:")
    metrics = analyze_google_stock_csv(google_csv)
    for key, val in metrics.items():
        if isinstance(val, float):
            print(f"   {key:<15s}: {val:.2f}")
        else:
            print(f"   {key:<15s}: {val}")


if __name__ == "__main__":
    main()
