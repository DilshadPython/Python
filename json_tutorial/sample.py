"""
JSON API Function Overview Demonstration (`sample.py`).

Demonstrates `json.load()` and `json.dumps()` string encoding.
"""

from pathlib import Path
try:
    from json_tutorial.json_processor import JSONProcessor
except ImportError:
    from json_processor import JSONProcessor


def main() -> None:
    """Read JSON file and display formatted string output."""
    filepath = Path("data_1.txt")
    if not filepath.exists():
        filepath = Path(__file__).parent / "data_1.txt"

    load_data = JSONProcessor.read_file(filepath)
    print("Loaded Data Object:", load_data)

    output_json_string = JSONProcessor.serialize_object(load_data, indent=2)
    print("\nSerialized JSON Output String:\n", output_json_string)


if __name__ == "__main__":
    main()
