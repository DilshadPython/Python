'''
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''
# This way it works but use lots of time so is getting slower after 30
def fibonacci(x):
	if x == 1:
		return 1
	elif x == 2:
		return 1
	elif x > 2:
		return fibonacci(x-1) + fibonacci(x-2)

for x in range(1, 101):
	print(x, ': ', fibonacci(x))
