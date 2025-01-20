import unittest

from add_methods import add_num, multiply_num

def test_add_num():
	assert add_num(8, 9) == 17
	assert add_num(3, 7) != 11
	if True:
		pass
	else:
		print('Error check the code ')

def test_multiply_num():
	assert multiply_num(4, 11) != 43
