"""
Unit test suite for the modernized 11.Set module.
Tests all 12 set scripts across Python 3.3 - 3.13.
"""

import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from add_to_set import demo_add_to_set
from create_empty_set import demo_empty_instantiations
from duplicate_set import demo_set_duplicates
from insersection import demo_drink_sets
from lib_set import demo_set_update_and_dir
from remove_det import demo_remove_methods
from set import demo_set_deduplication
from set_1 import demo_set_membership
from set_clear import demo_set_clear_math
from set_info import demo_set_info
from set_keywords import demo_set_algebra
from union_set import demo_set_properties


class TestSetModule(unittest.TestCase):

    def test_add_to_set(self):
        res = demo_add_to_set()
        self.assertIn(55, res)
        self.assertIn(105, res)
        self.assertIn(4444, res)

    def test_empty_instantiations(self):
        dict_t, set_t = demo_empty_instantiations()
        self.assertEqual(dict_t, dict)
        self.assertEqual(set_t, set)

    def test_set_duplicates(self):
        union_s, inter_s, diff_s = demo_set_duplicates()
        self.assertIn(2.7, inter_s)
        self.assertIn('Hello', diff_s)

    def test_drink_sets(self):
        common, top_only, all_d = demo_drink_sets()
        self.assertIn('Whiskey', common)
        self.assertIn('Milk', top_only)

    def test_set_update_and_dir(self):
        fruits, public_m = demo_set_update_and_dir()
        self.assertIn('pineapple', fruits)
        self.assertIn('intersection', public_m)

    def test_remove_methods(self):
        fruits, popped = demo_remove_methods()
        self.assertNotIn('oranges', fruits)
        self.assertNotIn('bananas', fruits)

    def test_set_deduplication(self):
        unique_s, dedup_l = demo_set_deduplication()
        self.assertEqual(len(unique_s), 7)

    def test_set_membership(self):
        has_b, has_w = demo_set_membership()
        self.assertTrue(has_b)
        self.assertFalse(has_w)

    def test_set_clear_math(self):
        elem, combined = demo_set_clear_math()
        self.assertEqual(len(elem), 0)
        self.assertEqual(len(combined), 22)

    def test_set_info(self):
        test_s, has_17 = demo_set_info()
        self.assertTrue(has_17)

    def test_set_algebra(self):
        common, only1, only2, all_l = demo_set_algebra()
        self.assertIn('Java', common)
        self.assertIn('Python', only1)
        self.assertIn('C++', only2)

    def test_set_properties(self):
        u_eq, i_eq, d_eq, s_eq = demo_set_properties()
        self.assertTrue(u_eq)
        self.assertTrue(i_eq)
        self.assertFalse(d_eq)
        self.assertTrue(s_eq)


if __name__ == '__main__':
    unittest.main()
