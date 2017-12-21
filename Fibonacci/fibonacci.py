

def fib(x):
	a = 0
	b = 1
	for i in range(0, 101):
		a, b = b, a + b
		print('Index: {} - Result {}'.format(i, a))

fib(101)
