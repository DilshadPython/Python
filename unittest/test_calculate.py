import unittest

# https://docs.python.org/3.9/library/unittest.html
# import calculation library methods
import calculate


# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# result = calculate.add(num1, num2)

class TestCalculate(unittest.TestCase):
	'''the method must be started with test word of the method
	 you want to test'''
	def test_add(self):
		# result = calculate.add(8, 5)
		# self.assertEqual(result, 13)
		self.assertEqual(calculate.add(4, 8), 12)
		self.assertEqual(calculate.add(-3, 4), 1)
		self.assertEqual(calculate.add(-3, -3), -6)

		self.assertNotEqual(calculate.add(-3, 4), -1)

	def test_subtruct(self):
		self.assertEqual(calculate.subtruct(4, 2), 2)
		self.assertEqual(calculate.subtruct(-5, 4), -9)
		self.assertEqual(calculate.subtruct(-7, -5), -2)

		self.assertNotEqual(calculate.subtruct(-5, 4), -3)

	def test_multiply(self):
		self.assertEqual(calculate.multiply(8, 3), 24)
		self.assertEqual(calculate.multiply(3, 2), 6)

		self.assertNotEqual(calculate.multiply(9, 4), 35)

	def test_divide(self):
		self.assertEqual(calculate.divide(6, 3), 2)
		self.assertEqual(calculate.divide(7, 2), 3.5)
		self.assertEqual(calculate.divide(12, 3), 4)

		self.assertNotEqual(calculate.divide(7, 2), 2.5)

		# self.assertRaises(ValueError, calculate.divide, 10, 0)

		# with self.assertRaises(ValueError):
		# 	calculate.divide(10, 0)


if __name__ == '__main__':
	unittest.main()

