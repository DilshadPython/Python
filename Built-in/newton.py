# create own module do something
import math 

'''
we are conbine the perivouse exercise all function in one function as nested scope function
fabs() ==>> absolute values from number
'''
def average(x, y):
	return (x + y) / 2

def square(number):
	return number * number

# this is the main function
def sqrt(number):
	def closeEnough(guess):
		return (math.fabs((square(guess)) - number) < 0.001)
	def improve(guess):
		return average(guess, (number / guess))
	def sqrtHelper(guess):
		if (closeEnough(guess)):
			return guess
		else:
			return sqrtHelper(improve(guess))
	return sqrtHelper(1.0)