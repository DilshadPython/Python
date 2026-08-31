"""
Unit test suite for the modernized 12.Dictionary module.
Tests all 20 dictionary scripts across Python 3.3 - 3.13.
"""

import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from build_dict import demo_build_dict
from copy_to_dic import demo_copy_dict
from count_words import count_file_words
from dict_ import demo_sort_dict_by_value
from dict_1 import demo_dict_mapping
from dict_list import demo_employee_records
from dict_num import demo_numeric_dict
from dict_num_1 import demo_dynamic_keys
from dict_update import demo_dict_update
from dict_update_func import demo_update_func
from dir_dic import demo_dir_dict
from empty_dict import demo_empty_dict
from lib_dict import demo_lib_dict
from my_calender import demo_calendar
from nested_dict import demo_nested_dict
from read_dict import demo_read_dict
from remove_from_dic import demo_pop_dict
from remove_from_dict import demo_advanced_removal
from sort_dict_by_value import demo_sort_by_value


class TestDictionaryModule(unittest.TestCase):

    def test_build_dict(self):
        cdict, keys, values = demo_build_dict()
        self.assertEqual(cdict['Hello'], 219)
        self.assertIn('Merci', keys)

    def test_copy_dict(self):
        m_table, c_table = demo_copy_dict()
        self.assertEqual(c_table['Jan'], 'January')
        self.assertEqual(len(m_table), len(c_table))

    def test_count_file_words(self):
        w_counts, sorted_w = count_file_words()
        self.assertTrue(len(w_counts) > 0)

    def test_sort_dict_by_value(self):
        asc, desc = demo_sort_dict_by_value()
        self.assertEqual(asc[0], ('h', -8))
        self.assertEqual(desc[0], ('i', 27))

    def test_dict_mapping(self):
        details = demo_dict_mapping()
        self.assertEqual(details['name'], 'Dilshad')
        self.assertEqual(details['email'], 'dilshad.abdulla@gmail.com')

    def test_employee_records(self):
        employees = demo_employee_records()
        self.assertEqual(len(employees), 3)

    def test_numeric_dict(self):
        sub_res, mul_res, num2 = demo_numeric_dict()
        self.assertEqual(sub_res, -866)
        self.assertEqual(mul_res, 11256)
        self.assertEqual(num2, 88)

    def test_dynamic_keys(self):
        data, total, max_val = demo_dynamic_keys()
        self.assertEqual(total, 228)
        self.assertEqual(max_val, 84)

    def test_dict_update(self):
        account = demo_dict_update()
        self.assertEqual(account['fname'], 'Azad')
        self.assertNotIn('date_of_birth', account)

    def test_update_func(self):
        details = demo_update_func()
        self.assertEqual(details['age'], 45)
        self.assertNotIn('website', details)

    def test_dir_dict(self):
        methods = demo_dir_dict()
        self.assertIn('get', methods)
        self.assertIn('keys', methods)

    def test_empty_dict(self):
        vehicles = demo_empty_dict()
        self.assertEqual(vehicles['Car'], 'Audi')

    def test_lib_dict(self):
        methods = demo_lib_dict()
        self.assertIn('values', methods)

    def test_calendar(self):
        aug, inv = demo_calendar()
        self.assertEqual(aug, 'August')
        self.assertEqual(inv, 'Invalid Month')

    def test_nested_dict(self):
        car, upper_car = demo_nested_dict()
        self.assertEqual(car, 'Audi')
        self.assertEqual(upper_car, 'AUDI')

    def test_read_dict(self):
        keys, items = demo_read_dict()
        self.assertIn('stid', keys)

    def test_pop_dict(self):
        popped, m_table = demo_pop_dict()
        self.assertEqual(popped, 'March')
        self.assertNotIn('Mar', m_table)

    def test_advanced_removal(self):
        popped_lang, last_item, post = demo_advanced_removal()
        self.assertEqual(popped_lang, 'English')

    def test_sort_by_value(self):
        s_lambda, s_itemgetter = demo_sort_by_value()
        self.assertEqual(s_lambda[0], ('e', 1))
        self.assertEqual(s_itemgetter[0], ('e', 1))


if __name__ == '__main__':
    unittest.main()
