# create function call itself recursiva function

def fibanacci(number):
	if number == 1:
		return 1
	elif number == 2:
		return 1
	elif number > 2:
		return fibanacci(number-1) + fibanacci(number-2)

"""
This function it works fine but after 35 slow down the speed of the program how explain:
fibanacci(5) = fibanacci(4) + fibanacci(3)
but fibanacci(3) = fibanacci(1) + fibanacci(2) + fibanacci(2) + fibanacci(1)
How to fix it
"""

for number in range(1, 99):
	print(number, ":", fibanacci(number))
