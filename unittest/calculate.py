
def add(num1, num2):
	''' Addition method '''
	result = num1 + num2
	return result


def subtruct(num1, num2):
	''' Substruction method '''
	result = num1 - num2
	return result


def multiply(num1, num2):
	''' Multiply method '''
	result = num1 * num2
	return result


def divide(num1, num2):
	''' Divid method '''
	result = num1 / num2
	if result == 0:
		raise ValueError('You can not divid this number by Zero!')
	return result