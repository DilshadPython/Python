def fact(num):
	item = 1
	for i in range(1, num + 1):
		item *= i
	return item

# print('Enter a number: ')
number = int(input('Enter a number: '))
print(str(number) + "! Equal to " + str(fact(number)))