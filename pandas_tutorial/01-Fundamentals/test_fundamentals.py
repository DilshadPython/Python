"""
Unit Test Suite for Pandas Fundamentals Module.

Tests Series creation, dictionary conversion, custom index labels,
DataFrame construction, metadata extraction, and type casting.
"""

from pathlib import Path
import sys
import unittest

# Ensure current directory is in Python path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import pandas as pd

from dataframe_creation_and_metadata import (
    cast_column_dtypes,
    create_sample_dataframe,
    inspect_dataframe_metadata,
)
from series_creation_and_indexing import (
    create_series_from_dict,
    create_series_from_list,
    create_series_with_custom_index,
    inspect_series_metadata,
)


class TestPandasFundamentals(unittest.TestCase):
    """Test cases for Pandas Series and DataFrame creation and metadata."""

    def test_create_series_from_list(self) -> None:
        """Verify Series creation from list."""
        s = create_series_from_list()
        self.assertEqual(len(s), 5)
        self.assertEqual(s[0], 10)
        self.assertEqual(s.name, "IntegerSequence")

    def test_create_series_with_custom_index(self) -> None:
        """Verify custom string indexing on Series."""
        s = create_series_with_custom_index()
        self.assertEqual(s["London"], 22.5)
        self.assertEqual(s["Tokyo"], 31.2)
        self.assertIn("Paris", s.index)

    def test_create_series_from_dict(self) -> None:
        """Verify Series creation from dictionary."""
        s = create_series_from_dict()
        self.assertEqual(s["Apples"], 150)
        self.assertEqual(s["Grapes"], 90)

    def test_inspect_series_metadata(self) -> None:
        """Verify series metadata extraction."""
        s = create_series_with_custom_index()
        meta = inspect_series_metadata(s)
        self.assertEqual(meta["shape"], (4,))
        self.assertEqual(meta["size"], 4)
        self.assertFalse(meta["has_nulls"])

    def test_create_sample_dataframe(self) -> None:
        """Verify DataFrame creation and columns."""
        df = create_sample_dataframe()
        self.assertEqual(df.shape, (5, 5))
        self.assertListEqual(list(df.columns), ["EmployeeID", "Name", "Department", "Salary", "Rating"])

    def test_inspect_dataframe_metadata(self) -> None:
        """Verify DataFrame metadata dictionary."""
        df = create_sample_dataframe()
        meta = inspect_dataframe_metadata(df)
        self.assertEqual(meta["row_count"], 5)
        self.assertEqual(meta["column_count"], 5)

    def test_cast_column_dtypes(self) -> None:
        """Verify data type casting on DataFrame columns."""
        df = create_sample_dataframe()
        casted = cast_column_dtypes(df)
        self.assertEqual(str(casted["Department"].dtype), "category")


if __name__ == "__main__":
    unittest.main()
