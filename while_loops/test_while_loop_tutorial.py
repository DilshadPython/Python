import unittest
from cloud_app.tutorials.while_loop_basics import (
    starter_while_loop_examples,
    interactive_and_event_controlled_loops,
    state_flags_and_accumulators,
    loop_control_and_sentinels,
    process_while_loop_with_standard_libraries,
)


class TestWhileLoopTutorial(unittest.TestCase):
    def test_starter_while_loop_examples(self):
        res = starter_while_loop_examples()
        self.assertEqual(res["counter_sequence"], [0, 1, 2, 3, 4])
        self.assertEqual(res["countdown_sequence"], [5, 4, 3, 2, 1])
        self.assertEqual(
            res["dual_variable_steps"],
            [(0, 10), (1, 9), (2, 8), (3, 7), (4, 6)],
        )
        self.assertEqual(res["accumulated_sum"], 55)
        self.assertEqual(res["final_counter_value"], 5)

    def test_interactive_and_event_controlled_loops_valid(self):
        res = interactive_and_event_controlled_loops(
            quiz_guesses=[2, 1],
            pet_guesses=["Rex", "Raffi"],
            calc_op=(10.0, 5.0, "+"),
        )
        self.assertTrue(res["quiz_success"])
        self.assertEqual(res["quiz_attempts"], 2)
        self.assertEqual(res["quiz_message"], "Correct! The company is Google.")
        self.assertTrue(res["pet_found"])
        self.assertEqual(res["pet_attempts"], 2)
        self.assertEqual(res["calc_result"], 15.0)

    def test_interactive_loops_quiz_failure_and_division(self):
        res = interactive_and_event_controlled_loops(
            quiz_guesses=[3],
            pet_guesses=["Rover"],
            calc_op=(10.0, 0.0, "/"),
        )
        self.assertFalse(res["quiz_success"])
        self.assertEqual(
            res["quiz_message"],
            "Sorry, your guess was wrong. The answer was Google.",
        )
        self.assertFalse(res["pet_found"])
        self.assertEqual(res["calc_result"], "Error: Division by zero")

    def test_interactive_loops_type_errors(self):
        with self.assertRaises(TypeError):
            interactive_and_event_controlled_loops("invalid", ["Rex"], (1, 2, "+"))
        with self.assertRaises(TypeError):
            interactive_and_event_controlled_loops([1], "invalid", (1, 2, "+"))

    def test_state_flags_and_accumulators_valid(self):
        res = state_flags_and_accumulators(target_sum=24)
        self.assertGreaterEqual(res["final_total"], 24)
        self.assertEqual(res["trajectory"], [12, 24, 36])
        self.assertFalse(res["status_active"])

    def test_state_flags_invalid_target(self):
        with self.assertRaises(TypeError):
            state_flags_and_accumulators(target_sum=-5)

    def test_loop_control_and_sentinels_valid(self):
        res = loop_control_and_sentinels(
            numbers=[10, 20, 0, 5, -1, 40], stop_val=-1
        )
        self.assertEqual(res["collected_before_sentinel"], [10, 20, 0, 5])
        self.assertTrue(res["hit_sentinel"])
        self.assertEqual(res["valid_division_results"], [10.0, 5.0, 20.0, -100.0, 2.5])
        self.assertEqual(res["skipped_zero_count"], 1)
        self.assertTrue(res["else_executed"])

    def test_loop_control_invalid_type(self):
        with self.assertRaises(TypeError):
            loop_control_and_sentinels("not a list", stop_val=-1)

    def test_process_while_loop_with_standard_libraries(self):
        res = process_while_loop_with_standard_libraries([2, 4, 6, 7, 8, 10])
        self.assertEqual(res["takewhile_even"], [2, 4, 6])
        self.assertEqual(res["dropwhile_even"], [7, 8, 10])
        self.assertEqual(
            res["manual_iterator_extraction"], [20, 40, 60, 70, 80, 100]
        )

    def test_process_while_loop_invalid_type(self):
        with self.assertRaises(TypeError):
            process_while_loop_with_standard_libraries("invalid")


if __name__ == "__main__":
    unittest.main()
