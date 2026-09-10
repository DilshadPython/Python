"""
Unit Test Suite for JSON Operations across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. Core `json_processor.py` operations (`loads`, `dumps`, `load`, `dump`).
2. Beginner level JSON string parsing and file I/O (`beginner_json.py`).
3. Intermediate custom `JSONEncoder` subclassing for dataclasses and datetimes (`intermediate_json.py`).
4. Senior custom `object_hook` transformations, NDJSON line streaming, and async JSON I/O (`senior_json.py`).
"""

import asyncio
from datetime import datetime
from pathlib import Path
import sys
import tempfile
import unittest

# Support both package and local directory import paths
root = Path(__file__).parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from json_processor import JSONProcessor
from beginner_json import demonstrate_json_string_parsing, demonstrate_json_file_io
from intermediate_json import ProjectMetadata, serialize_custom_metadata
from senior_json import parse_json_with_object_hook, stream_ndjson_lines, async_read_json_file, UserRecord


class TestJSONTutorial(unittest.TestCase):
    """Test suite verifying JSON operations across all modules and developer tiers."""

    def test_json_processor(self) -> None:
        """Verify core JSONProcessor parse, serialize, read, write methods."""
        data = {"name": "Test", "count": 42}
        json_str = JSONProcessor.serialize_object(data)
        parsed = JSONProcessor.parse_string(json_str)
        self.assertEqual(parsed, data)

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.json"
            JSONProcessor.write_file(file_path, data)
            read_back = JSONProcessor.read_file(file_path)
            self.assertEqual(read_back, data)

    def test_beginner_json(self) -> None:
        """Verify beginner JSON loads/dumps and file I/O."""
        raw = '{"key": "val", "num": 100}'
        d_obj, formatted = demonstrate_json_string_parsing(raw)
        self.assertEqual(d_obj["key"], "val")
        self.assertIn("100", formatted)

        with tempfile.TemporaryDirectory() as temp_dir:
            f_path = Path(temp_dir) / "beginner.json"
            read_data = demonstrate_json_file_io(f_path, d_obj)
            self.assertEqual(read_data["key"], "val")

    def test_intermediate_json(self) -> None:
        """Verify intermediate custom JSONEncoder for dataclasses and datetimes."""
        proj = ProjectMetadata(
            title="UnitTest Project",
            started_year=2026,
            author="Developer",
            created_at=datetime(2026, 9, 10, 12, 0, 0),
            skills=["Python", "JSON"],
        )
        encoded = serialize_custom_metadata(proj)
        self.assertIn("UnitTest Project", encoded)
        self.assertIn("2026-09-10T12:00:00", encoded)

    def test_senior_json(self) -> None:
        """Verify senior object_hook mapping, NDJSON streaming, and async JSON I/O."""
        json_in = '{"username": "monika", "role": "admin", "active": true}'
        user_obj = parse_json_with_object_hook(json_in)
        self.assertIsInstance(user_obj, UserRecord)
        self.assertEqual(user_obj.username, "monika")

        with tempfile.TemporaryDirectory() as temp_dir:
            nd_path = Path(temp_dir) / "stream.ndjson"
            nd_path.write_text('{"a": 1}\n{"b": 2}\n', encoding="utf-8")

            records = list(stream_ndjson_lines(nd_path))
            self.assertEqual(len(records), 2)
            self.assertEqual(records[0]["a"], 1)

            json_path = Path(temp_dir) / "data.json"
            JSONProcessor.write_file(json_path, {"status": "ok"})
            async_data = asyncio.run(async_read_json_file(json_path))
            self.assertEqual(async_data["status"], "ok")


if __name__ == "__main__":
    unittest.main()
