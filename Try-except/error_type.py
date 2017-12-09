
try: 
	print('Running try before except ....')
	print('23' + 25)

# except Exception, e: in python2.7
except TypeError as t:
	print('Running except ..............')
	print('\nTypeError triggered ')

