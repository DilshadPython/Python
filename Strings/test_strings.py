"""
Comprehensive Unit Test Suite for 3.Strings Module
Validates cross-version functionality (Python 3.3 to Python 3.13 and Python 2.7)
across all 21 scripts in the 3.Strings directory.
"""

from __future__ import print_function
import unittest
import sys
import os

# Import target modules dynamically with aliases to prevent name mangling
import __int as int_mod
import __str as str_mod
import add_str_together
import all_str_methods
import dir_str
import endwith
import escape_char
import expandstabs
import f_format
import f_string
import global_example
import global_var
import help_str
import imutability
import len_str
import modify_str
import multi_var
import slicing_str
import str_methods
import string as string_mod
import test_sys


class TestStringsModule(unittest.TestCase):

    def test___int(self):
        """1. Test integer parsing from string."""
        self.assertEqual(int_mod.read_and_parse_int('42'), 42)
        self.assertEqual(int_mod.read_and_parse_int('-100'), -100)
        with self.assertRaises(ValueError):
            int_mod.read_and_parse_int('not_a_number')

    def test___str(self):
        """2. Test string name details and type inspection."""
        details = str_mod.get_name_details('Dilshad')
        self.assertEqual(details["name"], 'Dilshad')
        self.assertEqual(details["type"], str)

    def test_add_str_together(self):
        """3. Test string concatenation and mixed formatting."""
        res = add_str_together.concatenate_strings('Hello', 'Python', 'Language')
        self.assertEqual(res["direct"], 'HelloPythonLanguage')
        self.assertEqual(res["with_separator"], 'Hello Python Language')
        mixed = add_str_together.concatenate_mixed(1973, 'Dilshad')
        self.assertEqual(mixed, '1973 Dilshad')

    def test_all_str_methods(self):
        """4. Test string casing, centering, substring count, and encoding."""
        methods = all_str_methods.get_string_methods()
        self.assertIn('upper', methods)
        self.assertIn('lower', methods)

        casing = all_str_methods.demonstrate_casing('python', 'JavaScript')
        self.assertEqual(casing["capitalize"], 'Python')
        self.assertEqual(casing["casefold"], 'javascript')

        centered = all_str_methods.center_text('Welcome', 30)
        self.assertEqual(len(centered), 30)

        cnt = all_str_methods.count_substring("I like oranges, but I don't likes bananas.", 'like')
        self.assertEqual(cnt, 2)

        encoded = all_str_methods.encode_string("visit Köln", "ascii", "ignore")
        self.assertEqual(encoded, b"visit Kln")

    def test_dir_str(self):
        """5. Test string directory attribute inspection."""
        attrs = dir_str.get_str_attributes('test')
        self.assertIn('capitalize', attrs)
        self.assertIn('strip', attrs)

    def test_endwith(self):
        """6. Test endswith substring checking."""
        txt = 'Welcome to the Europe to watch the fantastic football.'
        self.assertTrue(endwith.check_endswith(txt, 'll.'))
        self.assertFalse(endwith.check_endswith(txt, 'fantastic football.', 6, 15))
        self.assertTrue(endwith.check_endswith(txt, 'football.', 45, 55))
        
        msg = 'Welcome to the Europe to watch the fantastic Basketball.'
        self.assertTrue(endwith.check_endswith(msg, ('football.', 'Basketball.')))

    def test_escape_char(self):
        """7. Test escape character sequences."""
        samples = escape_char.get_escaped_strings()
        self.assertEqual(samples["octal_hello"], 'Hello Java!')
        self.assertEqual(samples["hex_hello"], 'Hello JavaScript')
        self.assertEqual(samples["carriage_return"], 'Welcome to\rPython')

    def test_expandstabs(self):
        """8. Test expandtabs space expansion."""
        msg = 'H\te\tl\tl\to \tPytho\tn'
        expanded = expandstabs.expand_tabs(msg, 8)
        self.assertNotIn('\t', expanded)
        self.assertTrue(len(expanded) > len(msg))

    def test_f_format(self):
        """9. Test float formatting precision."""
        res = f_format.format_floats(22.367453, 778.98763)
        self.assertEqual(res["precision_1"], '22.4 / 779.0')
        self.assertEqual(res["precision_2"], '22.37 / 778.99')
        single = f_format.format_single_float(232.45678231, '.2f')
        self.assertEqual(single, '232.46')

    def test_f_string(self):
        """10. Test f-string and str.format greetings."""
        res = f_string.format_greeting('Azad', 'Python', 37)
        self.assertEqual(res["greeting"], 'Hello Azad, do you like to learn Python programming language?')
        self.assertEqual(res["upper_greeting"], 'Hello, AZAD')
        self.assertEqual(res["profile"], 'My name is Azad and I am 37 years old')

    def test_global_example(self):
        """11. Test global scope mutation."""
        self.assertEqual(global_example.set_global_language("Python"), "Python")
        self.assertEqual(global_example.set_global_lang("Java"), "Java")

    def test_global_var(self):
        """12. Test local vs global scope shadowing."""
        self.assertEqual(global_var.get_global_name(), "My name is Dilshad")
        shadow = global_var.test_local_shadowing_first_name()
        self.assertEqual(shadow["local"], 'Julia')
        self.assertEqual(shadow["global"], 'Tomas')

    def test_help_str(self):
        """13. Test string class docstring inspection."""
        doc = help_str.get_str_help_doc()
        self.assertIsNotNone(doc)
        islower_doc = help_str.get_str_help_doc('islower')
        self.assertIsNotNone(islower_doc)

    def test_imutability(self):
        """14. Test string immutability and basic operations."""
        self.assertTrue(imutability.verify_immutability_error())
        res = imutability.demonstrate_immutability('Hello world')
        self.assertEqual(res["replace"], 'Hello Python')
        self.assertEqual(res["find_world"], 6)

    def test_len_str(self):
        """15. Test string length and membership operators."""
        text = 'The gap between writing basic Python code and developing professional-grade systems is far wider than most devs realize.'
        res = len_str.check_string_length_and_membership(text, 'professional-grade ', 'Java')
        self.assertEqual(res["length"], 120)
        self.assertTrue(res["is_present"])
        self.assertTrue(res["is_absent"])

    def test_modify_str(self):
        """16. Test upper, lower, strip, replace, and split transformations."""
        res = modify_str.modify_string(' Welcome to the Python ')
        self.assertEqual(res["stripped"], 'Welcome to the Python')
        self.assertEqual(res["upper"], ' WELCOME TO THE PYTHON ')
        self.assertEqual(res["words"], ['Welcome', 'to', 'the', 'Python'])

    def test_multi_var(self):
        """17. Test variable unpacking and chaining."""
        res = multi_var.unpack_multiple_variables()
        self.assertEqual(res["ints"], (7, 4, 19, 0))
        self.assertEqual(res["os_strings"], ('Linux', 'Apple', 'Windows'))
        self.assertEqual(res["unpacked_list"], ('Linux', 'Apple', 'Windows'))

    def test_slicing_str(self):
        """18. Test range slicing and negative indexing."""
        res = slicing_str.slice_string()
        self.assertEqual(res["first_25"], 'The gap between writing b')
        self.assertEqual(res["last_20"], 'n most devs realize.')

    def test_str_methods(self):
        """19. Test common string inspection methods."""
        res = str_methods.inspect_string_methods('How many years you have Python experiences?')
        self.assertEqual(res["title"], 'How Many Years You Have Python Experiences?')
        self.assertEqual(res["find_python"], 24)
        self.assertTrue(res["in_case_sensitive"])
        self.assertFalse(res["in_case_insensitive"])

    def test_string(self):
        """20. Test indexing, step slicing, and string reversal."""
        res = string_mod.string_slicing_and_reversing()
        self.assertEqual(res["index_6"], 'h')
        self.assertEqual(res["slice_to_37"], 'Test that obj is (or is not) an insta')
        self.assertEqual(res["reversed"][-4:], 'tseT')

    def test_test_sys(self):
        """21. Test Employee class properties and sys info."""
        info = test_sys.get_sys_info()
        self.assertTrue(os.path.exists(info["executable"]) or len(info["executable"]) > 0)
        emp = test_sys.Employee('Dilshad', 'Abdulla')
        self.assertEqual(emp.email, 'Dilshad.Abdulla@gmail.com')
        self.assertEqual(emp.full_name, 'Dilshad Abdulla')


if __name__ == '__main__':
    unittest.main()
