"""
Local, Enclosing, Global, Built-in (LEGB)
"""
a = 'I am Gloabal variable: a'

def search_variable():
	global a
	a = 'I am LOCAL variable (a) only access in my function search_variable'
	print('\n', a)

search_variable()

print('\n The global variable outside function called again not Display.\n')
print(a)