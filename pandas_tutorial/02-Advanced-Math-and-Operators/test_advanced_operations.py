"""
Unit Test Suite for Pandas Advanced Math and Operators Module.

Tests DataFrame slicing (.head, .tail, .loc, .iloc), boolean masking,
.query(), column statistics, string methods (.str), groupby aggregations, and I/O.
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import pandas as pd

from dataframe_io_and_persistence import (
    save_and_load_csv,
    save_and_load_json,
    save_and_load_pickle,
)
from dataframe_slicing_and_indexing import (
    filter_by_boolean_condition,
    filter_using_query,
    get_preview_slices,
    select_by_label,
    select_by_position,
)
from vector_math_and_string_methods import (
    apply_vectorized_string_methods,
    calculate_group_aggregations,
    compute_column_statistics,
)


class TestPandasAdvancedOperations(unittest.TestCase):
    """Test cases for indexing, vector math, string accessor, and I/O."""

    def setUp(self) -> None:
        """Set up standard test DataFrame fixture."""
        self.data = {
            "EmployeeID": [101, 102, 103, 104, 105],
            "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
            "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
            "Salary": [85000.0, 62000.0, 95000.0, 58000.0, 67000.0],
            "Rating": [4.8, 4.2, 4.9, 3.8, 4.5],
        }
        self.df = pd.DataFrame(self.data)

    def test_preview_slices(self) -> None:
        """Verify .head() and .tail() slicing."""
        head_df, tail_df = get_preview_slices(self.df, 2)
        self.assertEqual(len(head_df), 2)
        self.assertEqual(len(tail_df), 2)
        self.assertEqual(head_df.iloc[0]["Name"], "Alice")
        self.assertEqual(tail_df.iloc[-1]["Name"], "Eva")

    def test_select_by_label(self) -> None:
        """Verify .loc label indexing."""
        sub = select_by_label(self.df, 0, 2, ["Name", "Salary"])
        self.assertEqual(sub.shape, (3, 2))
        self.assertListEqual(list(sub.columns), ["Name", "Salary"])

    def test_select_by_position(self) -> None:
        """Verify .iloc position indexing."""
        sub = select_by_position(self.df, slice(0, 3), slice(1, 3))
        self.assertEqual(sub.shape, (3, 2))

    def test_filter_boolean_and_query(self) -> None:
        """Verify boolean masking and .query()."""
        bool_df = filter_by_boolean_condition(self.df, 70000.0)
        self.assertEqual(len(bool_df), 2)  # Alice (85k) and Charlie (95k)

        query_df = filter_using_query(self.df, "Engineering", 4.5)
        self.assertEqual(len(query_df), 2)

    def test_column_statistics(self) -> None:
        """Verify numeric column aggregations."""
        stats = compute_column_statistics(self.df, "Salary")
        self.assertEqual(stats["sum"], 367000.0)
        self.assertEqual(stats["min"], 58000.0)
        self.assertEqual(stats["max"], 95000.0)

    def test_string_methods(self) -> None:
        """Verify vectorized .str accessor methods."""
        up_names, has_e = apply_vectorized_string_methods(self.df, "Name")
        self.assertEqual(up_names[0], "ALICE")
        self.assertTrue(has_e[0])  # "Alice" contains 'e'
        self.assertFalse(has_e[1])  # "Bob" does not contain 'e'

    def test_group_aggregations(self) -> None:
        """Verify groupby aggregations."""
        grouped = calculate_group_aggregations(self.df, "Department", "Salary")
        self.assertEqual(len(grouped), 3)  # Engineering, HR, Marketing

    def test_io_persistence(self) -> None:
        """Verify CSV, JSON, and Pickle export and import."""
        temp_dir = Path("test_temp_pandas_io")
        temp_dir.mkdir(exist_ok=True)
        csv_path = temp_dir / "test.csv"
        json_path = temp_dir / "test.json"
        pkl_path = temp_dir / "test.pkl"

        try:
            csv_res = save_and_load_csv(self.df, csv_path)
            json_res = save_and_load_json(self.df, json_path)
            pkl_res = save_and_load_pickle(self.df, pkl_path)

            self.assertEqual(len(csv_res), 5)
            self.assertEqual(len(json_res), 5)
            self.assertEqual(len(pkl_res), 5)
        finally:
            csv_path.unlink(missing_ok=True)
            json_path.unlink(missing_ok=True)
            pkl_path.unlink(missing_ok=True)
            temp_dir.rmdir()


if __name__ == "__main__":
    unittest.main()
