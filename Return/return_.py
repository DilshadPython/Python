
# we create function to use return function and how to use it

def triangle(x, y, z):
	# we make a calculations without using return function and we get None
	x * y * z

print(triangle(7, 8, 4))

print('\n')

def cube(x, y, z):
	# we mwill get the result because use return function any other code write 
	# after return not be read
	return x * y * z

print(cube(7, 8, 4))