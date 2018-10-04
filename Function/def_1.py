def my_func():
	fname = 'Dilshad'
	lname = 'Abdulla'
	return print('The fullname is {} {}'.format(fname, lname))

my_func()

def your_func():
	num_1 = input('Enter a number: ')
	a = int(num_1)
	num_2 = input('\n Enter second number: ')
	b = int(num_2)
	total = a + b
	return print(f'The result of {num_1} + {num_2} is: {total}')

your_func()