"""
Unit test suite for the modernized 8.List module.
Tests all 40 list manipulation and algorithmic scripts across Python 3.3 - 3.13.
"""

import unittest
import sys
import os

# Add 8.List directory to module lookup path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from append_and_remove_from_the_list import demo_append_remove
from append_pop import demo_append_pop
from append_to_list import build_number_list
from ascending_order import demo_sorting
from books import manage_books
from change_list import demo_modify_by_index
from concatinat import demo_concatenation
from delete import demo_delete
from drop_add import demo_drop_add
from enumerate_list import demo_enumerate
from example import demo_basic
from extend_list import demo_extend
from footbal_teams import manage_football_teams
from for_list import iterate_list
from index_list import demo_index
from insert_to_line import demo_insert
import importlib
is_equal_mod = importlib.import_module('is_==')
demo_identity_vs_equality = is_equal_mod.demo_identity_vs_equality
from join_list import demo_join
from list_1 import demo_list_basics
from list_func import demo_list_aggregates
from list_func_1 import demo_add_methods
from list_func_2 import demo_list_operations
from list_func_3 import demo_membership_and_iter
from list_inside_list import demo_nested_lists
from list_keys import demo_list_methods
from list_number import demo_number_stats
from more_list import demo_more_list_ops
from number import demo_sort_comparison
from numbers import demo_numeric_operations
from planets import demo_planet_sorting
from reverse_list import demo_reversing
from reverse_url import demo_reverse_url
from slicing_list import demo_slicing
from sort_str import demo_sort_strings
from sorted_list import analyze_sentence
from sorted_not_sort import demo_sorted_vs_sort
from sorted_tuple_sort import demo_sorted_immutable
from str_list import demo_char_list
from students import demo_custom_object_sorting, Student
from sum import demo_sum_len


class TestListModule(unittest.TestCase):

    def test_append_remove(self):
        first, second, shopping = demo_append_remove()
        self.assertIn('Rope', second)
        self.assertNotIn('Wumpus B Gone', second)
        self.assertEqual(shopping[0], first)
        self.assertEqual(shopping[1], second)

    def test_append_pop(self):
        items = demo_append_pop()
        self.assertEqual(items, ['banana', 'cherry'])

    def test_append_to_list(self):
        numbers = build_number_list(5)
        self.assertEqual(numbers, [10, 20, 30, 40, 50])

    def test_ascending_order(self):
        asc, desc = demo_sorting()
        self.assertEqual(asc, [1, 3, 12, 27, 42, 88, 99])
        self.assertEqual(desc, [99, 88, 42, 27, 12, 3, 1])

    def test_books(self):
        books = manage_books()
        self.assertIn('Fluent Python', books)

    def test_change_list(self):
        colors = demo_modify_by_index()
        self.assertEqual(colors, ['purple', 'orange', 'blue'])

    def test_concatenation(self):
        combined, extended = demo_concatenation()
        self.assertEqual(combined, [1, 2, 3, 4, 5, 6])
        self.assertEqual(extended, [1, 2, 3, 4, 5, 6])

    def test_delete(self):
        data = demo_delete()
        self.assertEqual(data, [10, 50, 60])

    def test_drop_add(self):
        queue = demo_drop_add()
        self.assertEqual(queue, ['Customer 1', 'Customer 3'])

    def test_enumerate(self):
        indexed = demo_enumerate()
        self.assertEqual(indexed[0], (1, 'Apple'))

    def test_example(self):
        sample = demo_basic()
        self.assertEqual(len(sample), 4)

    def test_extend(self):
        appended, extended = demo_extend()
        self.assertEqual(appended, [1, 2, 3, [4, 5]])
        self.assertEqual(extended, [1, 2, 3, 4, 5])

    def test_football_teams(self):
        teams = manage_football_teams()
        self.assertEqual(len(teams), 5)

    def test_for_list(self):
        output = iterate_list()
        self.assertEqual(len(output), 4)

    def test_index_list(self):
        idx1, idx2 = demo_index()
        self.assertEqual(idx1, 1)
        self.assertEqual(idx2, 3)

    def test_insert_to_line(self):
        nums = demo_insert()
        self.assertEqual(nums, [0, 1, 2, 3, 4, 5])

    def test_is_equal(self):
        eq, identity1, identity2 = demo_identity_vs_equality()
        self.assertTrue(eq)
        self.assertFalse(identity1)
        self.assertTrue(identity2)

    def test_join_list(self):
        s1, s2 = demo_join()
        self.assertEqual(s1, 'Python is a versatile language')

    def test_list_basics(self):
        lst = demo_list_basics()
        self.assertEqual(lst[0], 10)

    def test_list_aggregates(self):
        max_v, min_v, total, count, char_list = demo_list_aggregates()
        self.assertEqual(max_v, 99)
        self.assertEqual(min_v, 3)
        self.assertEqual(total, 270)
        self.assertEqual(count, 7)
        self.assertEqual(char_list, ['D', 'i', 'l', 's', 'h', 'a', 'd'])

    def test_add_methods(self):
        langs = demo_add_methods()
        self.assertEqual(langs[0], 'Java')

    def test_list_operations(self):
        copy_lst, js_idx = demo_list_operations()
        self.assertEqual(js_idx, 3)

    def test_membership_and_iter(self):
        r, p, formatted = demo_membership_and_iter()
        self.assertTrue(r)
        self.assertFalse(p)

    def test_nested_lists(self):
        matrix, val = demo_nested_lists()
        self.assertEqual(val, 'g')

    def test_list_methods(self):
        attrs = demo_list_methods()
        self.assertIn('append', attrs)

    def test_number_stats(self):
        min_v, max_v, total = demo_number_stats()
        self.assertEqual(min_v, 2)
        self.assertEqual(max_v, 33)
        self.assertEqual(total, 91)

    def test_more_list_ops(self):
        t = demo_more_list_ops()
        self.assertEqual(t[0], 'Man United')

    def test_sort_comparison(self):
        s_copy, n_sort = demo_sort_comparison()
        self.assertEqual(s_copy, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_numeric_operations(self):
        rev, min_v, max_v, total = demo_numeric_operations()
        self.assertEqual(min_v, 6)
        self.assertEqual(max_v, 38)

    def test_planet_sorting(self):
        by_size, by_dist = demo_planet_sorting()
        self.assertEqual(by_size[0][0], 'Jupiter')

    def test_reversing(self):
        foods, teams = demo_reversing()
        self.assertEqual(teams, ['Tottenham', 'Chelsea', 'Man City', 'Liverpool'])

    def test_reverse_url(self):
        rev_str, rev_lst = demo_reverse_url()
        self.assertEqual(rev_str, 'ku.oc.elgoog//:sptth')

    def test_slicing(self):
        first_5, reversed_seq = demo_slicing()
        self.assertEqual(first_5, [1, 2, 3, 4, 5])
        self.assertEqual(reversed_seq, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_sort_strings(self):
        teams = demo_sort_strings()
        self.assertIn('Southampton', teams)

    def test_sorted_list(self):
        words, counts = analyze_sentence()
        self.assertIn('program', counts)

    def test_sorted_vs_sort(self):
        sorted_t = demo_sorted_vs_sort()
        self.assertEqual(len(sorted_t), 20)

    def test_sorted_immutable(self):
        s_num, s_char = demo_sorted_immutable()
        self.assertEqual(s_num[0], 1)

    def test_char_list(self):
        chars = demo_char_list()
        self.assertEqual(chars, sorted(['s', 'i', 'p', 'k', 'a', 'g', 'o', 'd']))

    def test_custom_object_sorting(self):
        by_id, by_fname, by_lname = demo_custom_object_sorting()
        self.assertEqual(by_id[0].id, 1254)
        self.assertEqual(by_fname[0].fname, 'James')

    def test_sum_len(self):
        total, count, avg = demo_sum_len()
        self.assertEqual(total, 229)
        self.assertEqual(count, 5)
        self.assertAlmostEqual(avg, 45.8)


if __name__ == '__main__':
    unittest.main()
