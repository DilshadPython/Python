


def factorial(num):
	# num = input('Please enter a number: ')
	if num == 1:
		return 1
	else:
		return num * factorial(num - 1)


print(factorial(3))