import unittest
from cloud_app.tutorials.set_basics import (
    starter_set_examples,
    set_operations_and_math,
    execute_all_dir_set_methods,
    process_set_with_standard_libraries
)


class TestSetTutorial(unittest.TestCase):
    """Unit test suite for Set tutorial module."""

    def test_starter_set_examples(self):
        res = starter_set_examples()
        self.assertEqual(res["unique_numbers"], [1, 2, 3, 4])
        self.assertTrue(res["has_apple"])
        self.assertFalse(res["has_banana"])
        self.assertEqual(res["common_skills_intersection"], ["python"])

    def test_set_operations_and_math(self):
        set_a = {1, 2, 3, 4}
        set_b = {3, 4, 5, 6}
        res = set_operations_and_math(set_a, set_b)
        self.assertEqual(res["union"], [1, 2, 3, 4, 5, 6])
        self.assertEqual(res["intersection"], [3, 4])
        self.assertEqual(res["difference"], [1, 2])
        self.assertEqual(res["symmetric_difference"], [1, 2, 5, 6])
        self.assertTrue(res["is_subset"])

    def test_set_operations_invalid_type(self):
        with self.assertRaises(TypeError):
            set_operations_and_math([1, 2], {3, 4})

    def test_execute_all_dir_set_methods(self):
        initial = ["apple", "banana", "apple"]
        res = execute_all_dir_set_methods(initial)
        self.assertIn("new_element", res["modified_set"])
        self.assertEqual(res["frozenset_instance"], ["immutable_1", "immutable_2"])

    def test_execute_all_dir_set_invalid_type(self):
        with self.assertRaises(TypeError):
            execute_all_dir_set_methods(12345)

    def test_process_set_with_standard_libraries(self):
        items = ["apple", "banana", "cherry"]
        res = process_set_with_standard_libraries(items, "banana")
        self.assertEqual(res["frozen_key_dict"], "valid_dict_value")
        self.assertTrue(res["operator_contains_target"])
        self.assertIn("set_bytes", res["set_bytes_vs_list"])

    def test_process_set_libraries_invalid_type(self):
        with self.assertRaises(TypeError):
            process_set_with_standard_libraries("invalid", "apple")


if __name__ == "__main__":
    unittest.main()
