"""Unit test suite for Python For Loops, Iteration Control & Iterator Mechanics (For Loop Module)."""

import unittest
from cloud_app.tutorials.for_loop_basics import (
    starter_loop_examples,
    enumerate_and_zip_iteration,
    nested_loops_and_control_flow,
    execute_all_dir_loop_methods,
    itertools_advanced_loops,
    dictionary_and_generator_iteration,
    cross_version_loop_analysis,
)


class TestForLoopTutorial(unittest.TestCase):
    """Test suite for verifying for-loop iteration mechanics, enumerate/zip, itertools, and memory benchmarks."""

    def test_starter_loop_examples(self):
        """Validates basic for loops, range accumulators, continue/break, and for-else clauses."""
        res = starter_loop_examples()
        self.assertEqual(res["collected_fruits"], ["APPLE", "BANANA", "CHERRY"])
        self.assertEqual(res["range_numbers"], [1, 3, 5, 7, 9])
        self.assertEqual(res["accumulated_counter"], 5)
        self.assertEqual(res["accumulated_sum"], 15)
        self.assertEqual(res["filtered_sequence"], [1, 3, 5, 7])
        self.assertTrue(res["loop_completed_normally"])

    def test_enumerate_and_zip_iteration(self):
        """Validates index tracking via enumerate and multi-sequence pairing via zip & zip_longest."""
        names = ["Dilshad", "Monika"]
        scores = [98, 95]
        res = enumerate_and_zip_iteration(names, scores)

        self.assertEqual(res["indexed_students"], ["#1 Dilshad", "#2 Monika"])
        self.assertEqual(res["paired_results"], [("Dilshad", 98), ("Monika", 95)])
        self.assertEqual(len(res["padded_pairs"]), 4)

    def test_enumerate_and_zip_invalid_types(self):
        """Validates guard clauses raising TypeError on non-list inputs."""
        with self.assertRaises(TypeError):
            enumerate_and_zip_iteration("not a list", [10, 20])

    def test_nested_loops_and_control_flow(self):
        """Validates 2D matrix iteration, row flattening, and early target break coordinates."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        res = nested_loops_and_control_flow(matrix, search_target=5)

        self.assertTrue(res["target_found"])
        self.assertEqual(res["target_coordinates"], (1, 1))
        self.assertEqual(res["flattened_matrix"], [1, 2, 3, 4, 5])

    def test_execute_all_dir_loop_methods(self):
        """Validates dir(range) methods/attributes and iterator progression."""
        res = execute_all_dir_loop_methods()

        self.assertIn("start", res["range_public_methods"])
        self.assertEqual(res["range_start"], 1)
        self.assertEqual(res["range_stop"], 10)
        self.assertEqual(res["range_step"], 2)
        self.assertEqual(res["range_count_five"], 1)
        self.assertEqual(res["range_index_five"], 2)
        self.assertTrue(res["enum_has_next"])
        self.assertTrue(res["zip_has_next"])
        self.assertEqual(res["iterator_first_value"], 10)
        self.assertEqual(res["iterator_second_value"], 20)

    def test_itertools_advanced_loops(self):
        """Validates itertools chain, islice, accumulate, and cycle pipelines."""
        items = ["a", "b"]
        res = itertools_advanced_loops(items)

        self.assertEqual(res["chained_iter"], ["a", "b", "extra_1", "extra_2"])
        self.assertEqual(res["sliced_iter"], [5, 6, 7, 8, 9])
        self.assertEqual(res["accumulated_sum"], [1, 3, 6, 10, 15])
        self.assertEqual(len(res["cycled_colors"]), 7)

    def test_dictionary_and_generator_iteration(self):
        """Validates dictionary iteration, generator sums, and memory benchmarks."""
        mapping = {"python": 3.13, "flask": 3.0}
        res = dictionary_and_generator_iteration(mapping)

        self.assertEqual(res["formatted_pairs"], ["python=3.13", "flask=3.0"])
        self.assertEqual(res["dict_keys"], ["python", "flask"])
        self.assertGreater(res["generator_sum"], 0)
        self.assertLess(res["gen_memory_bytes"], res["list_memory_bytes"])

    def test_cross_version_loop_analysis(self):
        """Validates lazy range sequence detection and Python version diagnostics."""
        res = cross_version_loop_analysis()
        self.assertTrue(res["is_lazy_range_sequence"])
        self.assertLess(res["range_memory_bytes"], 1000)


if __name__ == "__main__":
    unittest.main()
