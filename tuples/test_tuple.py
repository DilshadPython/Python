"""
Unit test suite for the modernized 10.Tuple module.
Tests all 19 tuple scripts across Python 3.3 - 3.13.
"""

import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from builtin_tuple import demo_builtin_tuple
from minmax import minmax, demo_minmax
from multy_tuple import demo_tuple_syntax
from numbersAndCharacter import demo_nested_unpacking
from temas import demo_team_unpacking
from tupl_list_dic import process_file_words
from tuple import demo_tuple_lookup
from tupleParameter import demo_star_unpacking
from tuple_1 import demo_tuple_basics
from tuple_2 import demo_storage_tuple
from tuple_3 import demo_parenthesis_free_tuples
from tuple_4 import demo_function_unpacking
from tuple_5 import demo_tuple_concatenation
from tuple_6 import demo_tuple_iteration
from tuple_dict import demo_tuple_comparison
from tuple_index import demo_tuple_unpacking
from tuple_keywords import demo_tuple_references
from tuple_memory import compare_tuple_vs_list


class TestTupleModule(unittest.TestCase):

    def test_builtin_tuple(self):
        methods, count_11, idx_17 = demo_builtin_tuple()
        self.assertIn('count', methods)
        self.assertIn('index', methods)
        self.assertEqual(count_11, 3)
        self.assertEqual(idx_17, 5)

    def test_minmax(self):
        lower, upper, lst_low, lst_up = demo_minmax()
        self.assertEqual(lower, -9)
        self.assertEqual(upper, 654)

    def test_tuple_syntax(self):
        t_not, t_single, t_multi = demo_tuple_syntax()
        self.assertEqual(t_not, str)
        self.assertEqual(t_single, tuple)

    def test_nested_unpacking(self):
        a, e, i, l = demo_nested_unpacking()
        self.assertEqual(a, 12)
        self.assertEqual(e, 8)
        self.assertEqual(i, 4)
        self.assertEqual(l, 1)

    def test_team_unpacking(self):
        c, e, g = demo_team_unpacking()
        self.assertEqual(c, 'Chelsea')
        self.assertEqual(e, 'Liverpool')
        self.assertEqual(g, 10)

    def test_process_file_words(self):
        sorted_w = process_file_words()
        self.assertTrue(len(sorted_w) > 0)

    def test_tuple_lookup(self):
        idx_f, count_24 = demo_tuple_lookup()
        self.assertEqual(idx_f, 3)
        self.assertEqual(count_24, 4)

    def test_star_unpacking(self):
        res, kw_res = demo_star_unpacking()
        self.assertEqual(kw_res['Alan'], 32)

    def test_tuple_basics(self):
        t1, t2, t3, t4 = demo_tuple_basics()
        self.assertEqual(len(t1), 4)
        self.assertEqual(len(t4), 0)

    def test_storage_tuple(self):
        is_empty, storage = demo_storage_tuple(interactive=False)
        self.assertTrue(is_empty)
        self.assertEqual(len(storage), 10)

    def test_parenthesis_free_tuples(self):
        t_type, s_tup = demo_parenthesis_free_tuples()
        self.assertEqual(t_type, tuple)
        self.assertEqual(s_tup, ('solo',))

    def test_function_unpacking(self):
        res = demo_function_unpacking()
        self.assertEqual(res, 25)

    def test_tuple_concatenation(self):
        combined = demo_tuple_concatenation()
        self.assertEqual(len(combined), 13)

    def test_tuple_iteration(self):
        elems, expanded = demo_tuple_iteration()
        self.assertEqual(len(elems), 7)
        self.assertEqual(len(expanded), 10)

    def test_tuple_comparison(self):
        items, c1, c2 = demo_tuple_comparison()
        self.assertTrue(c1)
        self.assertFalse(c2)

    def test_tuple_unpacking(self):
        st, pl = demo_tuple_unpacking()
        self.assertEqual(st[2], 'Dilshad Abdulla')
        self.assertEqual(pl[2], 'David Beckham')

    def test_tuple_references(self):
        same_ref, methods = demo_tuple_references()
        self.assertTrue(same_ref)

    def test_compare_tuple_vs_list(self):
        l_size, t_size, t_l, t_t = compare_tuple_vs_list()
        self.assertLess(t_size, l_size)


if __name__ == '__main__':
    unittest.main()
