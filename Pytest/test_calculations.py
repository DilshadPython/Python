# importing the file I want to test
import calculations
# run the test py.test -v -rxs test_calculations.py
# python -m pytest # or python -m pytest filename.py

# created the same function in the other file included test_ in front
def test_adding():
	assert calculations.adding(15, 9) == 24
# or
# def test_adding():
# 	total = calculations.adding(61, 17)
# 	assert total == 78

def test_substracting():
	assert calculations.substracting(16, 7) == 9
# or
# def test_substracting():
# 	result = calculations.substracting(9, 14)
# 	assert result == -5

def test_multiply():
	assert calculations.multiply(18, 4) == 72
# or
# def test_multiply():
# 	ouput = calculations.multiply(6, 9)
# 	assert ouput == 54
