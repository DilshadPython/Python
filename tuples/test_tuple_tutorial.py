import unittest
from cloud_app.tutorials.tuple_basics import (
    starter_tuple_examples,
    tuple_packing_and_unpacking,
    execute_all_dir_tuple_methods,
    tuple_memory_and_namedtuple,
    process_tuple_with_standard_libraries
)


class TestTupleTutorial(unittest.TestCase):
    """Unit test suite for Tuple tutorial module."""

    def test_starter_tuple_examples(self):
        res = starter_tuple_examples()
        self.assertEqual(res["color_rgb"], (255, 128, 0))
        self.assertEqual(res["single_element_tuple"], ("python",))
        self.assertEqual(res["extracted_red"], 255)
        self.assertEqual(res["slice_green_blue"], (128, 0))
        self.assertTrue(res["is_immutable_verified"])

    def test_tuple_packing_and_unpacking(self):
        res = tuple_packing_and_unpacking(10, 20, 30)
        self.assertEqual(res["packed_tuple"], (10, 20, 30))
        self.assertEqual(res["unpacked_values"], [10, 20, 30])
        self.assertEqual(res["extended_head"], 10)
        self.assertEqual(res["extended_rest"], [20, 30, "extra1", "extra2"])
        self.assertTrue(res["is_immutable"])

    def test_execute_all_dir_tuple_methods(self):
        sample = ("apple", "banana", "apple", "cherry")
        res = execute_all_dir_tuple_methods(sample)
        self.assertEqual(res["count_of_first"], 2)
        self.assertEqual(res["index_of_first"], 0)
        self.assertEqual(res["length"], 4)

    def test_execute_all_dir_tuple_invalid_type(self):
        with self.assertRaises(TypeError):
            execute_all_dir_tuple_methods("not a tuple")

    def test_tuple_memory_and_namedtuple(self):
        records = [("Dilshad", 95), ("Monika", 98)]
        res = tuple_memory_and_namedtuple(records)
        self.assertEqual(res["namedtuple_x"], 10)
        self.assertEqual(res["namedtuple_y"], 20)
        self.assertTrue(res["is_tuple_more_lightweight"])

    def test_tuple_memory_invalid_type(self):
        with self.assertRaises(TypeError):
            tuple_memory_and_namedtuple("not a list")

    def test_process_tuple_with_standard_libraries(self):
        coords = [(1, 5), (2, 3), (3, 8)]
        bin_vals = (42, 3.14)
        res = process_tuple_with_standard_libraries(coords, bin_vals)
        self.assertEqual(res["itertools_starmap_sums"], [6, 5, 11])
        self.assertEqual(res["struct_unpacked_tuple"][0], 42)
        self.assertAlmostEqual(res["struct_unpacked_tuple"][1], 3.14, places=2)

    def test_process_tuple_libraries_invalid_type(self):
        with self.assertRaises(TypeError):
            process_tuple_with_standard_libraries("invalid", (1, 2.5))


if __name__ == "__main__":
    unittest.main()
