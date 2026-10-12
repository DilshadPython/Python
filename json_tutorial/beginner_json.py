"""
Beginner Level JSON Operations Module (`beginner_json.py`).

This module provides clear, well-commented examples of fundamental JSON parsing methods
designed for beginner developers (`json.loads`, `json.dumps`, `json.load`, `json.dump`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import json`: Python standard library module for JSON operations.
# - `from pathlib import Path`: Object-oriented file path abstraction.
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Dict, Tuple`: PEP 484 type hint generics.
# =========================================================================
import json
from pathlib import Path
import sys
from typing import Dict, Tuple


def demonstrate_json_string_parsing(json_raw_string: str) -> Tuple[Dict, str]:
    """Parse JSON string into dict (`json.loads`) and re-encode to JSON (`json.dumps`).

    Args:
        json_raw_string (str): Valid JSON text input string.

    Returns:
        Tuple[Dict, str]: (Parsed Python dictionary, Formatted JSON string).
    """
    # 1. Decode JSON string into Python dictionary
    parsed_data = json.loads(json_raw_string)

    # 2. Encode Python dictionary back into pretty-printed JSON string
    formatted_json_str = json.dumps(parsed_data, indent=4)

    return parsed_data, formatted_json_str


def demonstrate_json_file_io(target_file: Path, data: Dict) -> Dict:
    """Write dictionary to JSON file (`json.dump`) and read back (`json.load`).

    Args:
        target_file (Path): Output JSON file path.
        data (Dict): Input Python dictionary.

    Returns:
        Dict: Dictionary read back from JSON file.
    """
    # Write dictionary object directly to text file
    with target_file.open("w", encoding="utf-8") as f_out:
        json.dump(data, f_out, indent=2)

    # Read dictionary object directly from text file
    with target_file.open("r", encoding="utf-8") as f_in:
        read_back_data = json.load(f_in)

    return read_back_data


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner JSON demonstration."""
    print("=== Beginner Level JSON Operations ===")

    raw_json = '{"name": "Dilshad", "started_year": 2018, "is_clear": true, "budget": null}'
    dict_obj, formatted_str = demonstrate_json_string_parsing(raw_json)

    print(f"Parsed Dictionary Type: {type(dict_obj)}")
    print(f"Formatted Output:\n{formatted_str}")

    demo_file = Path("beginner_output.json")
    read_data = demonstrate_json_file_io(demo_file, dict_obj)
    print(f"Read File Title: '{read_data.get('name')}'")

    if demo_file.exists():
        demo_file.unlink()

    return 0


if __name__ == "__main__":
    sys.exit(main())
