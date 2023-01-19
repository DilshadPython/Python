import newton

# this function sqrt() has been created in newton modules
new_sqrt = newton.sqrt(int(input('Enter a number to find sqrt from newton: '))) 

print(new_sqrt)

def square(number):
	# this function created here not the same square() from newton modules
	return number * number

num = square(int(input('Enter number: '))) 
print(num)

print('\n=====')
new_num = square(9)
print(new_num)

print('This square is from newton file: ', newton.square(25))