def calculator():
	a = 17
	b = 36
	print('Add Result', a + b)
	print('Sub Result', a - b)
	print('Multiple Result', a * b)
	print('Divid Result', a / b)
	print('Reminder Result', a % b)
	
	if a < b:
		print('The result is negative because a is {} where b is '.format(a, b))


if __name__ == '__main__':
	calculator()