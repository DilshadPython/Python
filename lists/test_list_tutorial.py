import unittest
from cloud_app.tutorials.list_basics import (
    starter_list_examples,
    manage_list_elements,
    slice_and_reverse_list,
    filter_and_transform_numbers,
    sort_elements_custom,
    execute_all_dir_list_methods,
    process_list_with_standard_libraries
)


class TestListTutorial(unittest.TestCase):
    """Unit test suite for List operations tutorial module."""

    def test_starter_list_examples(self):
        res = starter_list_examples()
        self.assertEqual(res["first_fruit_extracted"], "apple")
        self.assertEqual(res["sub_numbers_slice"], [20, 30, 40])
        self.assertEqual(res["removed_fruit"], "apple")
        self.assertTrue(res["has_cherry"])
        self.assertEqual(res["total_fruits"], 3)

    def test_manage_list_elements_valid(self):
        updated_list, popped = manage_list_elements([10, 20, 30], item_to_add=40, remove_index=0)
        self.assertEqual(updated_list, [20, 30, 40])
        self.assertEqual(popped, 10)

    def test_manage_list_elements_invalid_type(self):
        with self.assertRaises(TypeError):
            manage_list_elements("not a list")

    def test_manage_list_elements_index_error(self):
        with self.assertRaises(IndexError):
            manage_list_elements([1, 2], remove_index=10)

    def test_slice_and_reverse_list(self):
        items = ["Python", "Flask", "Django", "FastAPI"]
        result = slice_and_reverse_list(items, start=0, stop=3, reverse=True)
        self.assertEqual(result, ["Django", "Flask", "Python"])

    def test_filter_and_transform_numbers(self):
        numbers = [10, -5, 20, 0, 15]
        result = filter_and_transform_numbers(numbers, threshold=0, multiplier=2)
        self.assertEqual(result, [20, 40, 30])

    def test_filter_and_transform_invalid_element(self):
        with self.assertRaises(TypeError):
            filter_and_transform_numbers([10, "invalid", 20])

    def test_sort_elements_custom(self):
        langs = ["Python", "C", "JavaScript"]
        sorted_langs = sort_elements_custom(langs, reverse=True)
        self.assertEqual(sorted_langs, ["Python", "JavaScript", "C"])
        # Verify original list is unchanged (sorted() returns a new list)
        self.assertEqual(langs, ["Python", "C", "JavaScript"])

    def test_execute_all_dir_list_methods(self):
        items = ["apple", "banana", "apple"]
        res = execute_all_dir_list_methods(items)
        self.assertEqual(res["count_apple"], 2)
        self.assertEqual(res["cleared_list"], [])
        self.assertEqual(res["popped_first"], "apple")
        self.assertIn("fig", res["modified_list"])
        self.assertTrue(isinstance(res["sorted_strings"], list))

    def test_execute_all_dir_list_invalid_type(self):
        with self.assertRaises(TypeError):
            execute_all_dir_list_methods(12345)

    def test_process_list_with_standard_libraries(self):
        items = ["apple", "banana", "apple"]
        numbers = [10, 20, 30, 40, 50]
        res = process_list_with_standard_libraries(items, numbers)
        self.assertEqual(res["deque_left_append"][0], "first_header")
        self.assertEqual(res["counter_frequency"], {"apple": 2, "banana": 1})
        self.assertEqual(res["functools_reduce_sum"], 150)
        self.assertEqual(res["operator_sorted_records"][0]["name"], "Dilshad")
        self.assertEqual(len(res["random_sample"]), 2)

    def test_process_list_standard_libraries_invalid_type(self):
        with self.assertRaises(TypeError):
            process_list_with_standard_libraries("invalid", [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
