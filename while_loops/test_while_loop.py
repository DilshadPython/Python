"""
Comprehensive Unit Test Suite for Python While Loop Modules.
Tests count-controlled loops, event-controlled loops, file line reading,
break/continue controls, state tracking, and dual variable counters.
"""

import os
import sys
import tempfile
import unittest

# Ensure module directory is in sys.path for clean direct imports
sys.path.insert(0, os.path.dirname(__file__))

from while_count_control import count_control
from while_count_control_step import count_control_step
from while_decrease_counter import decrease_counter
from while_event_control import event_control_loop
from while_company_quiz import quiz_company
from while_calculator import calculate_operation
from while_increase_counter import increase_counter
from while_read_file_average import calculate_file_average
from while_guess_pet import guess_pet_name
from while_exit_validation import validate_exit_number
from while_ascending_descending import loop_up, loop_down
from while_divisible_by_seven import find_divisible_by_seven
from while_modulus_sequence import modulus_sequence
from while_boolean_accumulator import sum_accumulator_5_7
from while_early_check_accumulator import sum_accumulator_early_check
from while_username_validation import validate_username
from while_trajectory_status import accumulate_with_status
from while_formatted_accumulator import formatted_accumulator
from while_dual_variable import dual_variable_loop
from while_break_sentinel import accumulate_until_sentinel
from while_continue_division import process_division_pairs
from while_write_messages import write_messages_to_file
from while_nested_safe import nested_while_safe
from while_true_threshold import validate_threshold
from while_send_msg_to_file import send_messages_to_file


class TestWhileLoopBasics(unittest.TestCase):
    """Test basic count-controlled and step-controlled while loop operations."""

    def test_count_control(self):
        res = count_control(4)
        self.assertEqual(res, [0, 1, 2, 3, 4])

    def test_count_control_step(self):
        res = count_control_step(1, 10, 2)
        self.assertEqual(res, [1, 3, 5, 7, 9])

    def test_decrease_counter(self):
        res = decrease_counter(5, 0)
        self.assertEqual(res, [5, 4, 3, 2, 1, 0])

    def test_increase_counter(self):
        res = increase_counter(0, 5)
        self.assertEqual(res, [0, 1, 2, 3, 4, 5])

    def test_loop_up_and_down(self):
        asc = loop_up(5)
        self.assertEqual(asc, [0, 1, 2, 3, 4, 5])
        desc = loop_down(5)
        self.assertEqual(desc, [5, 4, 3, 2, 1, 0])


class TestEventAndInteractiveLoops(unittest.TestCase):
    """Test event-controlled loops, interactive validation, and arithmetic operations."""

    def test_event_control_loop(self):
        events = ['init', 'start', 'process', 'exit', 'post']
        out = event_control_loop(events, 'exit')
        self.assertEqual(out, ['init', 'start', 'process'])

    def test_quiz_company(self):
        success, msg = quiz_company([2, 1])
        self.assertTrue(success)
        self.assertIn("Google", msg)

        failed, msg_fail = quiz_company([3])
        self.assertFalse(failed)
        self.assertIn("wrong", msg_fail)

    def test_calculate_operation(self):
        self.assertEqual(calculate_operation(10.0, 5.0, '+'), 15.0)
        self.assertEqual(calculate_operation(10.0, 5.0, '-'), 5.0)
        self.assertEqual(calculate_operation(10.0, 5.0, '*'), 50.0)
        self.assertEqual(calculate_operation(10.0, 5.0, '/'), 2.0)
        self.assertEqual(calculate_operation(10.0, 0.0, '/'), "Error: Division by zero")

    def test_guess_pet_name(self):
        found, tries = guess_pet_name(["Rex", "Raffi"])
        self.assertTrue(found)
        self.assertEqual(tries, 2)

    def test_validate_exit_number(self):
        found, tries = validate_exit_number([9, 4, 1])
        self.assertTrue(found)
        self.assertEqual(tries, 3)

    def test_find_divisible_by_seven(self):
        val, tries = find_divisible_by_seven([10, 12, 49])
        self.assertEqual(val, 49)
        self.assertEqual(tries, 3)

    def test_validate_username(self):
        found, tries = validate_username(['Alice', 'Dilshad'])
        self.assertTrue(found)
        self.assertEqual(tries, 2)


class TestAdvancedWhileControl(unittest.TestCase):
    """Test modulus sequences, boolean flag accumulators, dual variables, and sentinels."""

    def test_modulus_sequence(self):
        res = modulus_sequence(7)
        self.assertEqual(len(res), 6)
        self.assertEqual(res[0], (1, "ODD"))
        self.assertEqual(res[1], (2, "EVEN"))

    def test_sum_accumulators(self):
        res57 = sum_accumulator_5_7(24)
        self.assertTrue(len(res57) > 0)
        self.assertGreaterEqual(res57[-1][2], 24)

        early = sum_accumulator_early_check(24)
        self.assertTrue(len(early) > 0)

        traj, status = accumulate_with_status(24)
        self.assertFalse(status)

        msgs = formatted_accumulator(24)
        self.assertTrue(len(msgs) > 0)

    def test_dual_variable_loop(self):
        res = dual_variable_loop(0, 10, 10, 0)
        self.assertEqual(len(res), 11)
        self.assertEqual(res[0], (1, 9))
        self.assertEqual(res[-1], (11, -1))

    def test_break_and_continue(self):
        tot, cnt, avg = accumulate_until_sentinel([10.0, 20.0, 30.0, -1.0])
        self.assertEqual(tot, 60.0)
        self.assertEqual(cnt, 3)
        self.assertEqual(avg, 20.0)

        div_res = process_division_pairs([(10.0, 2.0), (5.0, 0.0), (20.0, 4.0), (8.0, -1.0)])
        self.assertEqual(div_res, [5.0, 5.0])

    def test_nested_while_safe(self):
        res = nested_while_safe(3, 3)
        self.assertEqual(res, [9])

    def test_validate_threshold(self):
        val, tries = validate_threshold([2, 5, 15, 8], 10)
        self.assertEqual(val, 15)
        self.assertEqual(tries, 3)


class TestFileIOWhileLoops(unittest.TestCase):
    """Test file operations utilizing while loops."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_file_average(self):
        q_path = os.path.join(os.path.dirname(__file__), 'quotes.txt')
        tot, cnt, avg = calculate_file_average(q_path)
        self.assertEqual(cnt, 7)
        self.assertEqual(tot, 308.0)
        self.assertAlmostEqual(avg, 44.0)

    def test_file_writing(self):
        tmp_path = os.path.join(self.temp_dir.name, 'test_output.txt')
        lines = ['Line 1', 'Line 2']
        written = write_messages_to_file(tmp_path, lines)
        self.assertEqual(written, 2)

        sent_written = send_messages_to_file(tmp_path, ['msg1', 'msg2', 'q'])
        self.assertEqual(sent_written, 2)


if __name__ == '__main__':
    unittest.main()
