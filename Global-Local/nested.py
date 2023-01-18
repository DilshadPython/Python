# create function with 2 arguments and doing the calculation by another function
# create inside the function itself, the idea of nested varable is the second 
# function has access to the two varables are created in first function or main
# function

# first import math for calculation sqrt()
import math

# create first func or main function
def get_result(num_1, num_2):
	# create second function or (sub function)
	def get_sequre(num):
		return num * num
	'''
	here the return of main function work call the second function with one argument
	and this function get_sequre has access t num_1 and num_2 it show does the calculation
	and return the result to main function this is nested scope role.
	'''
	return math.sqrt(get_sequre(num_1) + get_sequre(num_2))

# create another var to do the job
height = int(input('Enter the height number: '))
width = int(input('Enter the width number: '))

measure = get_result(height, width)
print('The measure of get result is: ', measure)