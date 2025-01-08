# testing python code using unittest
# to test run python -m unittest test_example
import unittest
import example


class TestExample(unittest.TestCase):

    def test_name(self):
    	assert example.name == str
