"""
Unittest Suite for File Handling & I/O Module (`file_handling_and_io`)
"""
import os
import tempfile
import unittest
from file_handling_and_io.text_file_operations import (
    write_lines_to_file,
    append_line_to_file,
    read_file_lines,
    demonstrate_seek_and_tell,
)
from file_handling_and_io.binary_file_operations import (
    write_binary_data,
    read_binary_data,
    copy_binary_file_chunked,
    inspect_binary_header,
)
from file_handling_and_io.csv_file_operations import (
    write_csv_rows,
    read_csv_dict,
    sort_csv_records_by_field,
    analyze_google_stock_csv,
)
from file_handling_and_io.file_search_and_filter import (
    search_keyword_in_file,
    extract_emails_from_file,
    count_words_in_file,
)
from file_handling_and_io.temp_and_file_system import (
    create_temporary_file_demo,
    inspect_file_metadata,
)


class TestFileHandlingAndIO(unittest.TestCase):
    """Test suite validating text, binary, CSV, search, and temp file operations."""

    def setUp(self) -> None:
        """Sets up temporary test directory for file operations."""
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        """Cleans up temporary directory after test runs."""
        self.test_dir.cleanup()

    def test_text_file_operations(self) -> None:
        """Tests text file writing, appending, reading, and seeking."""
        file_path = os.path.join(self.test_dir.name, "cities_test.txt")
        initial = ["Tokyo", "London", "Paris"]

        chars = write_lines_to_file(file_path, initial)
        self.assertGreater(chars, 0)

        append_line_to_file(file_path, "Sydney")
        lines = read_file_lines(file_path)
        self.assertEqual(lines, ["Tokyo", "London", "Paris", "Sydney"])

        logs = demonstrate_seek_and_tell(file_path)
        self.assertEqual(len(logs), 3)

    def test_binary_file_operations(self) -> None:
        """Tests binary file writing, reading, copying, and header inspection."""
        src_path = os.path.join(self.test_dir.name, "binary_src.bin")
        dest_path = os.path.join(self.test_dir.name, "binary_dest.bin")
        raw_bytes = b"\x89PNG\r\n\x1a\nHeaderData"

        bytes_written = write_binary_data(src_path, raw_bytes)
        self.assertEqual(bytes_written, len(raw_bytes))

        copied = copy_binary_file_chunked(src_path, dest_path, chunk_size=4)
        self.assertEqual(copied, len(raw_bytes))
        self.assertEqual(read_binary_data(dest_path), raw_bytes)

        header, hex_rep = inspect_binary_header(src_path, 4)
        self.assertEqual(header, b"\x89PNG")
        self.assertEqual(hex_rep, "89 50 4E 47")

    def test_csv_file_operations(self) -> None:
        """Tests CSV writing, DictReader parsing, lambda sorting, and google.csv stock analysis."""
        csv_path = os.path.join(self.test_dir.name, "data_test.csv")
        headers = ["Name", "Age"]
        rows = [["Alice", "30"], ["Bob", "25"], ["Charlie", "35"]]

        write_csv_rows(csv_path, headers, rows)
        dict_records = read_csv_dict(csv_path)
        self.assertEqual(len(dict_records), 3)
        self.assertEqual(dict_records[0]["Name"], "Alice")

        sorted_records = sort_csv_records_by_field(dict_records, "Age", reverse=True)
        self.assertEqual(sorted_records[0]["Name"], "Charlie")

        # Test google.csv financial stock analysis
        base_dir = os.path.dirname(os.path.abspath(__file__))
        google_csv = os.path.join(base_dir, "google.csv")
        metrics = analyze_google_stock_csv(google_csv)
        self.assertIn("total_days", metrics)
        self.assertGreater(metrics["total_days"], 200)

    def test_file_search_and_filter(self) -> None:
        """Tests line searching, email extraction, and word counting."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        email_path = os.path.join(base_dir, "emailList.txt")

        emails = extract_emails_from_file(email_path)
        self.assertGreater(len(emails), 0)
        self.assertTrue(any("gmail.com" in e for e in emails))

    def test_temp_and_file_system(self) -> None:
        """Tests temporary file auto-cleanup and pathlib metadata inspection."""
        text_to_write = "Temporary buffer text"
        read_back = create_temporary_file_demo(text_to_write)
        self.assertEqual(read_back, text_to_write)

        target_file = os.path.join(self.test_dir.name, "meta_test.txt")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("Metadata content")

        meta = inspect_file_metadata(target_file)
        self.assertTrue(meta["exists"])
        self.assertEqual(meta["name"], "meta_test.txt")
        self.assertEqual(meta["stem"], "meta_test")
        self.assertEqual(meta["suffix"], ".txt")


if __name__ == "__main__":
    unittest.main()
