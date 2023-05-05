def square(num):
	result = num * num
	return result


def square(num=int(input('Enter a number: '))):
	result = num * num
	return print(num, ' squared is: ', result)

print(square())
