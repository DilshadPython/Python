"""
Unit Test Suite for All 17 Modules in 2.Numbers (Python 3.3 to Python 3.13 & Python 2.7 Compatible)

Executes test coverage using Python's standard `unittest` framework across all 17 number scripts:
1. bin_hex_oct_num.py
2. calculator.py
3. complex_num.py
4. deciamel.py
5. example.py
6. f_num.py
7. floats.py
8. get_average.py
9. inte.py
10. is_prime_v.py
11. is_prime_v2.py
12. is_prime_v3.py
13. multipl.py
14. nearst_number.py
15. none_bool.py
16. primnumber.py
17. random_num.py
"""

from __future__ import print_function
import unittest
import math

# Import all 17 modules from 2.Numbers
import bin_hex_oct_num
import calculator
import complex_num
import deciamel
import example
import f_num
import floats
import get_average
import inte
import is_prime_v
import is_prime_v2
import is_prime_v3
import multipl
import nearst_number
import none_bool
import primnumber
import random_num


class TestNumbersSuite(unittest.TestCase):

    # 1. Test bin_hex_oct_num.py
    def test_bin_hex_oct_num(self):
        info = bin_hex_oct_num.convert_number_bases(10)
        self.assertEqual(info["number"], 10)
        self.assertEqual(info["binary"], '0b1010')
        self.assertEqual(info["hexadecimal"], '0xa')
        self.assertIn(info["octal"], ['0o12', '012'])  # Py3: '0o12', Py2: '012'
        
        comp = bin_hex_oct_num.to_complex(5)
        self.assertEqual(comp, complex(5, 0))

    # 2. Test calculator.py
    def test_calculator(self):
        self.assertEqual(calculator.calculate(10, '+', 5), 15)
        self.assertEqual(calculator.calculate(10, '-', 5), 5)
        self.assertEqual(calculator.calculate(10, '*', 5), 50)
        self.assertEqual(calculator.calculate(10, '/', 5), 2.0)
        self.assertEqual(calculator.calculate(2, '^', 3), 8)
        self.assertEqual(calculator.calculate(10, '%', 3), 1)
        self.assertEqual(calculator.calculate(10, '//', 3), 3)
        
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(10, '/', 0)
        with self.assertRaises(ValueError):
            calculator.calculate(10, 'invalid_op', 5)

    # 3. Test complex_num.py
    def test_complex_num(self):
        c_val = 4 + 8 + 3j  # 12 + 3j
        details = complex_num.get_complex_details(c_val)
        self.assertEqual(details["real"], 12.0)
        self.assertEqual(details["imag"], 3.0)
        
        demo_res = complex_num.demo_complex()
        self.assertEqual(len(demo_res), 3)

    # 4. Test deciamel.py
    def test_deciamel(self):
        res = deciamel.decimal_operations(10, 4)
        self.assertEqual(res["sum"], 14)
        self.assertEqual(res["difference"], 6)
        self.assertEqual(res["multiplication"], 40)
        self.assertEqual(res["division"], 2.5)
        self.assertEqual(res["floor_division"], 2)
        self.assertEqual(res["exponent"], 10000)
        self.assertEqual(res["modulus"], 2)

    # 5. Test example.py
    def test_example(self):
        self.assertEqual(example.parse_base_string('10000', 3), 81)
        self.assertEqual(example.parse_base_string('10000', 2), 16)
        self.assertEqual(example.parse_base_string('10000', 4), 256)
        
        demo = example.demo_base_conversions()
        self.assertEqual(demo["base_3"], 81)

    # 6. Test f_num.py
    def test_f_num(self):
        input_list = [2, 3, 9, 24]
        add_val = 3
        res = f_num.add_constant_to_list(input_list, add_val)
        self.assertEqual(res, [5, 6, 12, 27])
        
        demo_res = f_num.run_demo()
        self.assertEqual(demo_res, [5, 6, 12, 27])

    # 7. Test floats.py
    def test_floats(self):
        res = floats.float_operations(10.5, 2.5)
        self.assertEqual(res["sum"], 13.0)
        self.assertEqual(res["difference"], 8.0)
        self.assertEqual(res["multiplication"], 26.25)
        self.assertEqual(res["division"], 4.2)
        self.assertEqual(res["floor_division"], 4.0)
        
        specials = floats.inspect_special_floats()
        self.assertTrue(math.isnan(specials["nan"]))
        self.assertTrue(math.isinf(specials["inf"]))
        self.assertEqual(specials["scientific_3e8"], 300000000.0)

    # 8. Test get_average.py
    def test_get_average(self):
        numbers = [10, 20, 30, 40]
        self.assertEqual(get_average.calculate_average(numbers), 25.0)
        
        demo_avg = get_average.run_average_demo()
        self.assertAlmostEqual(demo_avg, 35.166666666666664, places=5)

        with self.assertRaises(ValueError):
            get_average.calculate_average([])

    # 9. Test inte.py
    def test_inte(self):
        res = inte.integer_operations(20, 6)
        self.assertEqual(res["sum"], 26)
        self.assertEqual(res["difference"], 14)
        self.assertEqual(res["multiplication"], 120)
        self.assertEqual(res["floor_division"], 3)
        self.assertEqual(res["modulus"], 2)

    # 10. Test is_prime_v.py
    def test_is_prime_v(self):
        self.assertFalse(is_prime_v.is_prime_v(-5))
        self.assertFalse(is_prime_v.is_prime_v(0))
        self.assertFalse(is_prime_v.is_prime_v(1))
        self.assertTrue(is_prime_v.is_prime_v(2))
        self.assertTrue(is_prime_v.is_prime_v(3))
        self.assertFalse(is_prime_v.is_prime_v(4))
        self.assertTrue(is_prime_v.is_prime_v(29))

    # 11. Test is_prime_v2.py
    def test_is_prime_v2(self):
        self.assertFalse(is_prime_v2.is_prime_v2(-5))
        self.assertFalse(is_prime_v2.is_prime_v2(0))
        self.assertFalse(is_prime_v2.is_prime_v2(1))
        self.assertTrue(is_prime_v2.is_prime_v2(2))
        self.assertTrue(is_prime_v2.is_prime_v2(3))
        self.assertFalse(is_prime_v2.is_prime_v2(4))
        self.assertTrue(is_prime_v2.is_prime_v2(29))

    # 12. Test is_prime_v3.py
    def test_is_prime_v3(self):
        self.assertFalse(is_prime_v3.is_prime_v3(-5))
        self.assertFalse(is_prime_v3.is_prime_v3(0))
        self.assertFalse(is_prime_v3.is_prime_v3(1))
        self.assertTrue(is_prime_v3.is_prime_v3(2))
        self.assertTrue(is_prime_v3.is_prime_v3(3))
        self.assertFalse(is_prime_v3.is_prime_v3(4))
        self.assertTrue(is_prime_v3.is_prime_v3(29))

    # 13. Test multipl.py
    def test_multipl(self):
        self.assertEqual(multipl.shift_multiply(10, 2), 40)
        self.assertEqual(multipl.shift_multiply(15, 3), 120)
        self.assertEqual(multipl.shift_multiply(20, 4), 320)
        
        seq = multipl.shift_sequence(1, 1, steps=5)
        self.assertEqual(seq, [2, 4, 8, 16, 32])

        demo_res = multipl.run_bitwise_demo()
        self.assertEqual(demo_res["section1"]["single"], 40)

    # 14. Test nearst_number.py
    def test_nearst_number(self):
        res = nearst_number.format_and_round(888.0, 112.0)
        self.assertEqual(res["rounded_sum"], 1000)
        self.assertEqual(res["rounded_sum_formatted"], "1,000")
        self.assertEqual(res["rounded_div"], 8)
        self.assertEqual(res["rounded_div_2dec"], 7.93)

    # 15. Test none_bool.py
    def test_none_bool(self):
        self.assertFalse(none_bool.evaluate_truthiness(0))
        self.assertFalse(none_bool.evaluate_truthiness(0.0))
        self.assertFalse(none_bool.evaluate_truthiness([]))
        self.assertFalse(none_bool.evaluate_truthiness(''))
        self.assertFalse(none_bool.evaluate_truthiness({}))
        self.assertFalse(none_bool.evaluate_truthiness(None))
        
        self.assertTrue(none_bool.evaluate_truthiness(1))
        self.assertTrue(none_bool.evaluate_truthiness(-1))
        self.assertTrue(none_bool.evaluate_truthiness([3]))
        self.assertTrue(none_bool.evaluate_truthiness('Hello'))

    # 16. Test primnumber.py
    def test_primnumber(self):
        self.assertFalse(primnumber.is_prime_number(-10))
        self.assertFalse(primnumber.is_prime_number(0))
        self.assertFalse(primnumber.is_prime_number(1))
        self.assertTrue(primnumber.is_prime_number(2))
        self.assertTrue(primnumber.is_prime_number(3))
        self.assertFalse(primnumber.is_prime_number(4))
        self.assertTrue(primnumber.is_prime_number(29))
        self.assertEqual(primnumber.number(7), True)

    # 17. Test random_num.py
    def test_random_num(self):
        val = random_num.get_random_single(1, 12)
        self.assertTrue(1 <= val < 12)
        
        samples = random_num.get_random_sample(1, 12, 4)
        self.assertEqual(len(samples), 4)
        self.assertEqual(len(set(samples)), 4)  # All unique elements
        for item in samples:
            self.assertTrue(1 <= item < 12)


if __name__ == '__main__':
    unittest.main()
