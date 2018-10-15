
numbers_not_divid_to_zero = []

for number in range(1, 200):
	if number % 5 ==0 and number % 3 ==0:
		print(True, ' == 3', True , ' == 5')
		print('FizzBuzz')
	elif number % 3 == 0:
		print('Fizz')
		print(True, ' == 3', False, ' != 5')
	elif number % 5 == 0:
		print('Buzz')
		print(True, ' == 5', ' || ', False, ' != 3')
	else:
		print(number)
		numbers_not_divid_to_zero.append(number)
		print(numbers_not_divid_to_zero)