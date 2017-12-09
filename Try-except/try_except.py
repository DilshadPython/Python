
try:
	print('Running try before except ....')
	print('23' + 25)

# except Exception, e: in python2.7
except Exception as e:
	print('\n Display e: ', str(e))

