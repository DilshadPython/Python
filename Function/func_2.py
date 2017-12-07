
def get_gender(sex=None):
	
	print('List of gender m or f and None.')
	sex = input('Please enter the gender list above: ')
	if sex is 'm':
		print('The result is Male')
	elif sex is 'f':
		print('the result is Female')
	elif sex == None:
		print('There is no gender')
	else:
		print('Not in the list above')
	print(sex)

# print 'Enter the charcter of sex: ',
# sex = raw_input()

# get_gender('m')
# get_gender('f')
get_gender()
