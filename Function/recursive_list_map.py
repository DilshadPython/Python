# this is a fuction signed as an object and at the end this function a siged to verables

def square(num):
	return num * num

# create number to be entered
number = int(input('Enter a number: '))

# a signed the function to a varable
var = square(number)

# created another varable called sqnumber signed to privouse var
sqnumber = var 

# print the result of the recursive func as varable
print(sqnumber)

print('===========================')
numbers = range(1, 10)

# map in python means higher-order function
mapping = list(map(square, numbers))

print(mapping)