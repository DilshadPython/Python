
def get_gender(sex=None):
	if sex is 'm':
		sex = 'Male'
	elif sex is 'f':
		sex = 'Female'
	elif sex is None:
		sex = 'None'
	else:
		sex = 'Not ins the list'

	print(sex)

print('Call the function with four different char')
get_gender('m')
get_gender('f')
get_gender()
get_gender('H')
