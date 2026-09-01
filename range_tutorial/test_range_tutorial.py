import datetime
import unittest
from cloud_app.tutorials.range_basics import (
    starter_range_examples,
    range_and_number_formatting,
    datetime_and_graphics_formatting,
    range_vs_xrange_mechanics,
)


class TestRangeTutorial(unittest.TestCase):
    def test_starter_range_examples(self):
        res = starter_range_examples()
        self.assertEqual(res["stop_sequence"], [0, 1, 2, 3, 4])
        self.assertEqual(res["start_stop_sequence"], [2, 3, 4, 5, 6, 7])
        self.assertEqual(res["step_sequence"], [1, 3, 5, 7, 9])
        self.assertEqual(res["countdown_sequence"], [10, 8, 6, 4, 2])
        self.assertEqual(len(res["grid_matrix"]), 3)
        self.assertEqual(res["grid_matrix"][0], [0, 1, 2, 3])
        self.assertEqual(res["horizontal_sequence"], "1 -> 2 -> 3 -> 4 -> 5")

    def test_range_and_number_formatting_valid(self):
        res = range_and_number_formatting(limit=3, large_number=1000000, float_val=99.9876)
        self.assertEqual(res["zero_padded_items"], ["01", "02", "03"])
        self.assertEqual(res["custom_padded_items"], ["ITEM_0001", "ITEM_0002", "ITEM_0003"])
        self.assertEqual(res["formatted_float_2dp"], "99.99")
        self.assertEqual(res["formatted_float_4dp"], "99.9876")
        self.assertEqual(res["formatted_large_comma"], "1,000,000")
        self.assertEqual(res["formatted_large_underscore"], "1_000_000")

    def test_range_and_number_formatting_invalid_types(self):
        with self.assertRaises(TypeError):
            range_and_number_formatting(limit="invalid")
        with self.assertRaises(TypeError):
            range_and_number_formatting(large_number="1000")
        with self.assertRaises(TypeError):
            range_and_number_formatting(float_val="invalid")

    def test_datetime_and_graphics_formatting_valid(self):
        res = datetime_and_graphics_formatting(days_count=3, pyramid_height=3)
        self.assertEqual(len(res["formatted_dates"]), 3)
        self.assertEqual(res["formatted_dates"][0]["iso"], "2026-01-01")
        self.assertEqual(res["formatted_dates"][0]["day_of_year"], "Day 001")
        self.assertEqual(res["ascii_pyramid"], ["  *", " ***", "*****"])
        self.assertEqual(res["ascii_single_sided"], ["*", "**", "***"])
        self.assertEqual(res["ascii_decreasing_space"], ["###", " ##", "  #"])

    def test_datetime_and_graphics_formatting_invalid_inputs(self):
        with self.assertRaises(TypeError):
            datetime_and_graphics_formatting(days_count=0)
        with self.assertRaises(TypeError):
            datetime_and_graphics_formatting(pyramid_height=-1)

    def test_range_vs_xrange_mechanics(self):
        res = range_vs_xrange_mechanics()
        self.assertEqual(res["range_attributes"]["start"], 2)
        self.assertEqual(res["range_attributes"]["stop"], 20)
        self.assertEqual(res["range_attributes"]["step"], 3)
        self.assertEqual(res["range_attributes"]["length"], 6)

        self.assertEqual(res["sequence_methods"]["index_of_8"], 2)
        self.assertEqual(res["sequence_methods"]["count_of_8"], 1)
        self.assertEqual(res["sequence_methods"]["count_of_99"], 0)

        self.assertTrue(res["containment_test"]["in_range"])
        self.assertFalse(res["containment_test"]["not_in_range"])

        self.assertTrue(res["memory_benchmark"]["is_constant_memory"])
        self.assertLess(res["memory_benchmark"]["range_1m_bytes"], res["memory_benchmark"]["list_1k_bytes"])

        self.assertTrue(res["range_equality"]["empty_ranges_equal"])
        self.assertTrue(res["range_equality"]["equivalent_ranges_equal"])
        self.assertIn("index", res["dir_range_public_methods"])
        self.assertIn("count", res["dir_range_public_methods"])
        self.assertIn("Python 2.7", res["python2_vs_3_notes"])


if __name__ == "__main__":
    unittest.main()
