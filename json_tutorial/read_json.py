"""
JSON File Loader Demonstration (`read_json.py`).

Loads `data_1.txt` JSON configuration file and prints top-level key metadata.
"""

from pathlib import Path
try:
    from json_tutorial.json_processor import JSONProcessor
except ImportError:
    from json_processor import JSONProcessor


def main() -> None:
    """Read data_1.txt and print key-value summary."""
    filepath = Path("data_1.txt")
    if not filepath.exists():
        filepath = Path(__file__).parent / "data_1.txt"

    data = JSONProcessor.read_file(filepath)

    print(f"Project Title: {data.get('title')}")
    print(f"Author: {data.get('author')}")
    print(f"Started Year: {data.get('started_year')}")


if __name__ == "__main__":
    main()