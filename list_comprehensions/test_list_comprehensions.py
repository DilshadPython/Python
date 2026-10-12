"""
Unit test suite for the modernized 9.List-comprehensions module.
Tests all 23 list and dictionary comprehension scripts across Python 3.3 - 3.13.
"""

import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from awesome import demo_awesome_comp
from comprehensions import demo_string_comprehensions
from comprehensions_if import demo_even_squares
from comprehensions_list import demo_matrix_column_extraction
from create_dict_use_for_comperhe import demo_dict_list_creation
from dict_comperhension import demo_dict_comprehension
from filters import filter_students
from generate_comp import demo_generators
from index_list import demo_index_and_lengths
from lambda_map import demo_map_vs_comprehension
from lcomprehensions import demo_math_series
from list_comp_exit_values import demo_numeric_filter
from list_multiply_index import demo_cartesian_product
from list_of_dict import demo_nested_dict_filtering
from list_with_year import demo_year_filtering
from listcomp import demo_grade_boosting
from listcomp1 import demo_string_case_conversion
from listcomp2 import read_files_with_comp
from listcomp3 import read_numbers_one_liner
from listcomp_file import clean_file_lines
from listcomp_if import demo_multi_condition_comp
from movies import filter_movies
from zip_list import demo_zip_comprehension


class TestListComprehensions(unittest.TestCase):

    def test_awesome_comp(self):
        res = demo_awesome_comp()
        self.assertEqual(res, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_string_comprehensions(self):
        m_teams, s_teams = demo_string_comprehensions()
        self.assertIn('Manchester City', m_teams)
        self.assertIn('Southampton', s_teams)

    def test_even_squares(self):
        res = demo_even_squares()
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 4)

    def test_matrix_column_extraction(self):
        col1, col3, elem = demo_matrix_column_extraction()
        self.assertEqual(col1, ['s', 'k', 'u'])
        self.assertEqual(col3, ['p', 'g', 'd'])
        self.assertEqual(elem, 6)

    def test_dict_list_creation(self):
        loop_res, comp_res, sorted_res = demo_dict_list_creation()
        self.assertEqual(len(comp_res), 6)
        self.assertEqual(sorted_res[0]['name'], 'Claudia')

    def test_dict_comprehension(self):
        mapping = demo_dict_comprehension()
        self.assertEqual(mapping['Claudia'], 'Berlin')

    def test_filter_students(self):
        over_40, english = filter_students()
        self.assertIn('Dilshad', over_40)
        self.assertIn('Victoria', english)

    def test_generators(self):
        gen_list, gen_expr = demo_generators()
        self.assertEqual(gen_list[0], 4)
        self.assertEqual(gen_expr[3], 9)

    def test_index_and_lengths(self):
        indexed, lengths = demo_index_and_lengths()
        self.assertEqual(indexed[0], (1, 'Claudia'))
        self.assertEqual(lengths['John'], 4)

    def test_map_vs_comprehension(self):
        d_comp, s_comp, e_comp = demo_map_vs_comprehension()
        self.assertEqual(d_comp, [2, 6, 10, 14, 18, 22])

    def test_math_series(self):
        squares, mult5 = demo_math_series()
        self.assertEqual(len(squares), 20)
        self.assertEqual(mult5, [25, 100, 225, 400])

    def test_numeric_filter(self):
        evens, odds = demo_numeric_filter()
        self.assertIn(74, evens)
        self.assertIn(91, odds)

    def test_cartesian_product(self):
        scaled, cart = demo_cartesian_product()
        self.assertEqual(scaled[0], 8)
        self.assertEqual(len(cart), 9)

    def test_nested_dict_filtering(self):
        senior = demo_nested_dict_filtering()
        self.assertIn('Dilshad Abdulla', senior)

    def test_year_filtering(self):
        older = demo_year_filtering()
        self.assertIn('Arsenal', older)

    def test_grade_boosting(self):
        loop_b, comp_b = demo_grade_boosting()
        self.assertEqual(loop_b, comp_b)

    def test_string_case_conversion(self):
        cars = demo_string_case_conversion()
        self.assertEqual(cars[0], 'audi')

    def test_read_files_with_comp(self):
        raw, nums = read_files_with_comp()
        self.assertEqual(len(raw), 11)
        self.assertEqual(nums[0], 23)

    def test_read_numbers_one_liner(self):
        nums = read_numbers_one_liner()
        self.assertEqual(len(nums), 11)

    def test_clean_file_lines(self):
        lines = clean_file_lines()
        self.assertEqual(lines[0], '23')

    def test_multi_condition_comp(self):
        evens, w_len = demo_multi_condition_comp()
        self.assertEqual(len(evens), 51)

    def test_filter_movies(self):
        movies_80s = filter_movies()
        self.assertIn('Ghostbusters II (1989)', movies_80s)

    def test_zip_comprehension(self):
        zipped, car_dict, keys, values = demo_zip_comprehension()
        self.assertEqual(car_dict['Audi'], 'A7')


if __name__ == '__main__':
    unittest.main()
