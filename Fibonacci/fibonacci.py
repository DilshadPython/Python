'''
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

def fibonacci(x):
	a = 0
	b = 1
	for i in range(0, 101):
		a, b = b, a + b
		print('Index: {} - Result {}'.format(i, a))

fibonacci(101)

print('#######################################\n') 

def fibonacci(x):
	a = 0
	b = 1
	for i in range(0, 101):
		a, b = b, a + b
		print(f'Index: {i} - Result {i, a} ')

fibonacci(101)