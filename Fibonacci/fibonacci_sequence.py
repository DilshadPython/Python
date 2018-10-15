'''
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

def fibonacci(x):
	x, y = 0, 1
	for i in range(0, 101):
		print('X: ', x, ', Y:', y)
		x, y = y, x + y
		print(f'Index: {i} - Result {i, x} ')


fibonacci(101)