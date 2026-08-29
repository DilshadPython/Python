# we have to import 
import functools


def sum(x, y):
	return x + y

numbers = list(range(1, 11))
print(numbers)

# the reduce func take the sum function apply to numbers and adding one by one
sum = functools.reduce(sum, numbers)


print('The results are: ', sum)