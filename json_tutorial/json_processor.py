"""
JSON Processor Module (`json_processor.py`).

This module provides reusable helper functions and the `JSONProcessor` class
for serializing Python objects into JSON and parsing JSON data into Python data structures.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import json`: Python standard library module for JSON encoding/decoding.
# - `from pathlib import Path`: Object-oriented file path manipulation.
# - `import sys`: System execution status utilities.
# - `from typing import Any, Dict, Union`: PEP 484 type hint generics.
# =========================================================================
import json
from pathlib import Path
import sys
from typing import Any, Dict, Union


class JSONProcessor:
    """Wrapper class providing static utility methods for JSON operations."""

    @staticmethod
    def parse_string(json_string: str) -> Any:
        """Parse JSON formatted string into Python data structures (`json.loads`).

        Args:
            json_string (str): JSON formatted string.

        Returns:
            Any: Decoded Python dict, list, primitive, or None.
        """
        return json.loads(json_string)

    @staticmethod
    def serialize_object(data: Any, indent: int = 4, sort_keys: bool = False) -> str:
        """Serialize Python object into formatted JSON string (`json.dumps`).

        Args:
            data (Any): Python dictionary, list, or primitive object.
            indent (int): Indentation space count for pretty-printing.
            sort_keys (bool): Whether output dictionary keys should be sorted.

        Returns:
            str: JSON formatted string.
        """
        return json.dumps(data, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def read_file(filepath: Union[str, Path]) -> Any:
        """Read and decode JSON data from file (`json.load`).

        Args:
            filepath (Union[str, Path]): Target JSON file path.

        Returns:
            Any: Decoded Python object structure.
        """
        path_obj = Path(filepath)
        with path_obj.open("r", encoding="utf-8") as json_file:
            return json.load(json_file)

    @staticmethod
    def write_file(filepath: Union[str, Path], data: Any, indent: int = 4) -> None:
        """Encode and write Python data structure to JSON file (`json.dump`).

        Args:
            filepath (Union[str, Path]): Target JSON file path.
            data (Any): Python data object.
            indent (int): Indentation space count for pretty-printing.
        """
        path_obj = Path(filepath)
        path_obj.parent.mkdir(parents=True, exist_ok=True)
        with path_obj.open("w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=indent)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for JSON processor demonstration."""
    print("=== JSON Processor Demonstration ===")

    sample_dict = {"name": "Dilshad", "role": "Developer", "skills": ["Python", "JSON"]}
    json_str = JSONProcessor.serialize_object(sample_dict)
    print(f"Serialized JSON String:\n{json_str}")

    parsed = JSONProcessor.parse_string(json_str)
    print(f"Parsed Back Object: {parsed}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
