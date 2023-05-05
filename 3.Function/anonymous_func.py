# Anonymous function is a function doesn't have a name example lambda
# structure of lambda function
# lambda x: x*x 

'''
def sequre(num):
	return num * num
This example above is exactly the same like lambda
'''

sq = lambda x: x*x

print(sq(int(input('Enter any number: '))))

print('\n Another anonymous function using list, map lambda:')
# create another anonymous function using map with lambda
numbers = range(1, 9)
sqroot = list(map(lambda x: x*x, numbers))

print(sqroot)