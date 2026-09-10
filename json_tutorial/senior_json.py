"""
Senior Level JSON Streaming & Deserialization Module (`senior_json.py`).

This module provides enterprise JSON architecture patterns designed for senior software engineers
(NDJSON JSON-Lines streaming, custom `JSONDecoder` `object_hook` transformations, non-blocking async file I/O).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import asyncio`: Asynchronous event loop framework for non-blocking I/O.
# - `import json`: Core JSON library.
# - `from pathlib import Path`: Path abstraction.
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Any, Dict, Generator, List`: PEP 484 type hint generics.
# =========================================================================
import asyncio
import json
from pathlib import Path
import sys
from typing import Any, Dict, Generator, List


class UserRecord:
    """Domain model class representing a parsed user record."""

    def __init__(self, username: str, role: str, active: bool) -> None:
        self.username = username
        self.role = role
        self.active = active

    def __repr__(self) -> str:
        return f"UserRecord(username='{self.username}', role='{self.role}', active={self.active})"


def user_object_hook(dct: Dict[str, Any]) -> Any:
    """Object hook callback function converting JSON dictionaries into UserRecord instances.

    Args:
        dct (Dict[str, Any]): Parsed JSON dictionary.

    Returns:
        Any: UserRecord instance if keys match schema, else raw dict.
    """
    if "username" in dct and "role" in dct:
        return UserRecord(
            username=dct["username"],
            role=dct["role"],
            active=dct.get("active", True),
        )
    return dct


def parse_json_with_object_hook(json_str: str) -> Any:
    """Parse JSON string using custom `object_hook` mapping.

    Args:
        json_str (str): Input JSON string.

    Returns:
        Any: Instantiated domain object or structure.
    """
    return json.loads(json_str, object_hook=user_object_hook)


def stream_ndjson_lines(filepath: Path) -> Generator[Dict[str, Any], None, None]:
    """Stream and parse newline-delimited JSON (NDJSON) line-by-line for high efficiency.

    Args:
        filepath (Path): Input NDJSON file path.

    Yields:
        Generator[Dict[str, Any], None, None]: Yields parsed dictionary per line.
    """
    with filepath.open("r", encoding="utf-8") as ndjson_file:
        for line in ndjson_file:
            line_str = line.strip()
            if line_str:
                yield json.loads(line_str)


async def async_read_json_file(filepath: Path) -> Dict[str, Any]:
    """Simulate non-blocking asynchronous JSON file parsing using `asyncio`.

    Args:
        filepath (Path): Target JSON file path.

    Returns:
        Dict[str, Any]: Decoded JSON object structure.
    """
    await asyncio.sleep(0.01)  # Non-blocking context switch
    with filepath.open("r", encoding="utf-8") as f_in:
        return json.load(f_in)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior JSON demonstration."""
    print("=== Senior Level JSON Operations ===")

    json_input = '{"username": "Dilshad", "role": "Senior Engineer", "active": true}'
    user_obj = parse_json_with_object_hook(json_input)
    print(f"Object Hook Transformation: {user_obj}")

    demo_json = Path("data_1.txt")
    if demo_json.exists():
        data = asyncio.run(async_read_json_file(demo_json))
        print(f"Async Parsed JSON Title: '{data.get('title')}'")

    return 0


if __name__ == "__main__":
    sys.exit(main())
