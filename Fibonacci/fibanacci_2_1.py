# create function call itself recursiva function

fibanacci_cache = {}

def fibanacci(number):
	# if we have cached the value, then return it
	if number in fibanacci_cache:
		return fibanacci_cache[number]

	# compute the Nth term
	if number == 1:
		value = 1
	elif number == 2:
		value = 1
	elif number > 2:
		value = fibanacci(number-1) + fibanacci(number-2)

	# cach the value and return it
	fibanacci_cache[number] = value
	return value
	
"""
This function it works fine but after 35 slow down the speed of the program how explain:
fibanacci(5) = fibanacci(4) + fibanacci(3)
but fibanacci(3) = fibanacci(1) + fibanacci(2) + fibanacci(2) + fibanacci(1)
How to fix it
"""

for number in range(1, 599):
	print(number, ":", fibanacci(number))
