"""
Stack JSON Reader Script (`read_stack_to_json.py`).

Loads `stack.json` file and demonstrates dictionary `.items()` iteration.
"""

from pathlib import Path
try:
    from json_tutorial.json_processor import JSONProcessor
except ImportError:
    from json_processor import JSONProcessor


def main() -> None:
    """Read stack.json file and iterate key-value mappings."""
    filepath = Path("stack.json")
    if not filepath.exists():
        filepath = Path(__file__).parent / "stack.json"

    data = JSONProcessor.read_file(filepath)

    print("Stack JSON Contents:")
    for key, value in data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
