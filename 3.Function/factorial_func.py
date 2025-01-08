def factorial(number):
	item = 1
	for i in range(1, number+1):
		item *= i
	return item

num=int(input('Enter a number: '))
print(str(num) + '! = ', factorial(num))