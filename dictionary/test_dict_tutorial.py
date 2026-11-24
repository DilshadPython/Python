import unittest
from cloud_app.tutorials.dict_basics import (
    starter_dict_examples,
    execute_all_dir_dict_methods,
    dict_standard_libraries_and_json,
    process_dict_with_standard_libraries
)


class TestDictTutorial(unittest.TestCase):
    """Unit test suite for Dictionary tutorial module."""

    def test_starter_dict_examples(self):
        res = starter_dict_examples()
        self.assertEqual(res["accessed_username"], "coder_starter")
        self.assertEqual(res["safe_get_role"], "Guest")
        self.assertEqual(res["user_profile"]["score"], 150)
        self.assertTrue(res["has_score_key"])
        self.assertIn("language", res["dict_keys"])

    def test_execute_all_dir_dict_methods(self):
        initial = {"name": "Dilshad", "role": "Developer"}
        res = execute_all_dir_dict_methods(initial)
        self.assertEqual(res["get_name"], "Dilshad")
        self.assertEqual(res["setdefault_role"], "Developer")
        self.assertEqual(res["fromkeys_dict"], {"a": 0, "b": 0, "c": 0})

    def test_execute_all_dir_dict_invalid_type(self):
        with self.assertRaises(TypeError):
            execute_all_dir_dict_methods(["not", "a", "dict"])

    def test_dict_standard_libraries_and_json(self):
        pairs = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
        res = dict_standard_libraries_and_json(pairs)
        self.assertEqual(res["defaultdict_result"]["fruit"], ["apple", "banana"])
        self.assertEqual(res["chainmap_font"], "Inter")
        self.assertEqual(res["chainmap_language"], "Python")
        self.assertEqual(res["json_parsed"]["language"], "Python")

    def test_dict_libraries_invalid_type(self):
        with self.assertRaises(TypeError):
            dict_standard_libraries_and_json("invalid")

    def test_process_dict_with_standard_libraries(self):
        scores = {"Dilshad": 98, "Monika": 95}
        res = process_dict_with_standard_libraries(scores, "banana")
        self.assertTrue(res["is_read_only_enforced"])
        self.assertEqual(res["sorted_by_value"][0], ("Dilshad", 98))
        self.assertGreater(res["pretty_json_length"], 0)

    def test_process_dict_libraries_invalid_type(self):
        with self.assertRaises(TypeError):
            process_dict_with_standard_libraries("invalid", 123)


if __name__ == "__main__":
    unittest.main()
