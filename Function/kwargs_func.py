'''
1 inch = 2.54
1 feet = 12 inces
'''

def centimter(inches = 0, feet = 0):
	print('Please the inches and the feet value: ')

	# inches = int(input('Please enter the length in inches: '))
	# feet = int(input('Enter the length in feet: '))

	inche_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	
	return print(inche_to_cm + feet_to_cm)

centimter(12, 6)

print('')

def centimter_1():
	print('Please the inches and the feet value: ')

	inches = int(input('Please enter the length in inches: '))
	feet = int(input('Enter the length in feet: '))

	inche_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	
	return print(inche_to_cm + feet_to_cm)

centimter_1()
