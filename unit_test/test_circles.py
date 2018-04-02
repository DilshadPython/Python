import unittest

from circles import circle_area

from math import pi


# we create class to test the function
class TestCircleArea(unittest.TestCase):
	def test_area(self):
		# we test the areas when radius >= 0
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

	def test_values(self):
		# Make sure value errors are raised when necessary check if the value is less than 0 
		self.assertRaises(ValueError, circle_area, -2)

	def test_types(self):
		# test if the value not real number like boolean, string and 3+5j
		self.assertRaises(TypeError, circle_area, 3+5j)
		self.assertRaises(TypeError, circle_area, True)
		self.assertRaises(TypeError, circle_area, 'radius')

