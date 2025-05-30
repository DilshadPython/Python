# this is nested function and lecsecal scoping
import math 

'''
sqrtHelper()
improve()

fabs() ==>> absolute values from number
'''

def square(number):
	return number * number

def sqrt(number):
	return sqrtHelper(1.0, number)

def sqrtHelper(guess, number):
	if (closeEnough(guess, number)):
		return guess
	else:
		return sqrtHelper(improve(guess, number), number)

def closeEnough(guess, number):
	return (math.fabs(square(guess) - number) < 0.001)

def improve(guess, x):
	return average(guess, (x / guess))

def average(x, y):
	return (x + y) / 2

num = int(input('Enter a number: '))
print(sqrt(num))