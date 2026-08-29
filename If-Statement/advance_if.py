def cal():
	num = int(input('Enter a number: '))
	if is_even(num):
		print('Even number ') # no reminder
	else:
		print('Odd number') # with reminder

def is_even(n):
	return True if n % 2 == 0 else False

cal()