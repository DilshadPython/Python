'''
New feature in Python3.7
'''
def my_detail(fname, lname):
	# breakpoint()
	print('You entered full name')
	return f'{fname}, {lname}'

fname, lname = input('Enter you fname: ').split(', '), input('Enter your lname: ')
my_detail(fname, lname)

print('\nSome practic with debugging:')

breakpoint()

def python(p2, p3):
	print('Python version 2')
	# breakpoint()
	print('Python version 3')

x, y = 'P2', 'P3'
python(x, y)

def anotherway(x, y):
	print('Python.3.7 Breakpoint')
	# import dpt; pdb.set_trace()
	print('Python3.7 import dpt pdb.set_trace().')

first, second = 'Breakpoint', 'import pdb; pdb.set_trace()'
anotherway(x, y)