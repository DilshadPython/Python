'''
What is an Automated Test?
It's a piece of code which makes sure that another piece of code is working
correctly under a certain condition.

Integration Tests
- test multiplte pieces together to assurt that they work well with one another

Functional Tests
- test that everything works from the end-user's of view
- slowest run
'''
import unittest

def add_num(num1, num2):
	result = num1 + num2
	return result


print(add_num(3, 8))

def multiply_num(x, y):
	return x * y


print(multiply_num(4, 11))