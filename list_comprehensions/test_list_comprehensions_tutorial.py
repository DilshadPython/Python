import unittest
from cloud_app.tutorials.list_comprehensions_basics import (
    starter_list_comprehension_examples,
    basic_and_conditional_comprehensions,
    nested_and_matrix_comprehensions,
    dict_set_and_generator_comprehensions,
    comprehension_vs_standard_libraries
)


class TestListComprehensionsTutorial(unittest.TestCase):
    """Unit test suite for List Comprehensions tutorial module."""

    def test_starter_list_comprehension_examples(self):
        res = starter_list_comprehension_examples()
        self.assertEqual(res["squares"], [1, 4, 9, 16, 25])
        self.assertEqual(res["evens"], [2, 4, 6, 8, 10])
        self.assertEqual(res["uppercase_words"], ["HELLO", "CLOUD", "FLASK", "PYTHON"])
        self.assertEqual(res["number_labels"], ["Odd", "Even", "Odd", "Even", "Odd"])

    def test_basic_and_conditional_valid(self):
        res = basic_and_conditional_comprehensions([1, -2, 3, -4, 5], threshold=0)
        self.assertEqual(res["squared"], [1, 4, 9, 16, 25])
        self.assertEqual(res["filtered_positive"], [1, 3, 5])
        self.assertEqual(res["clamped_zeros"], [1, 0, 3, 0, 5])
        self.assertEqual(res["formatted_labels"], ["Val:1", "Val:-2", "Val:3", "Val:-4", "Val:5"])

    def test_basic_and_conditional_invalid_type(self):
        with self.assertRaises(TypeError):
            basic_and_conditional_comprehensions("not a list")

    def test_basic_and_conditional_invalid_element(self):
        with self.assertRaises(TypeError):
            basic_and_conditional_comprehensions([1, "invalid", 3])

    def test_nested_and_matrix_comprehensions(self):
        matrix = [[1, 2], [3, 4]]
        res = nested_and_matrix_comprehensions(matrix)
        self.assertEqual(res["flattened"], [1, 2, 3, 4])
        self.assertEqual(res["transposed"], [[1, 3], [2, 4]])
        self.assertEqual(res["positive_numeric"], [1, 2, 3, 4])

    def test_nested_matrix_invalid_type(self):
        with self.assertRaises(TypeError):
            nested_and_matrix_comprehensions("not a list")

    def test_dict_set_and_generator_comprehensions(self):
        items = ["apple", "banana", "apple", "cherry"]
        res = dict_set_and_generator_comprehensions(items)
        self.assertEqual(res["length_dict"]["apple"], 5)
        self.assertEqual(res["length_dict"]["banana"], 6)
        self.assertEqual(res["unique_upper_set"], ["APPLE", "BANANA", "CHERRY"])
        self.assertTrue(res["is_generator_lazy"])
        self.assertLess(res["gen_memory_bytes"], res["list_memory_bytes"])

    def test_dict_set_generator_invalid_type(self):
        with self.assertRaises(TypeError):
            dict_set_and_generator_comprehensions(12345)

    def test_comprehension_vs_standard_libraries(self):
        numbers = [1, 2, 3, 4, 5]
        res = comprehension_vs_standard_libraries(numbers)
        self.assertTrue(res["map_equals_comprehension"])
        self.assertTrue(res["filter_equals_comprehension"])
        self.assertTrue(res["starmap_equals_comprehension"])
        self.assertTrue(res["compress_equals_comprehension"])
        self.assertTrue(res["has_even"])
        self.assertTrue(res["all_positive"])

    def test_comprehension_vs_libraries_invalid(self):
        with self.assertRaises(TypeError):
            comprehension_vs_standard_libraries("invalid")


if __name__ == "__main__":
    unittest.main()
