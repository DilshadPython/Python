
'''
We create  a function called itself when is run called clouser function
this function also work like global and local variable
'''

def university():
	name = 'Main function university name is: Cambridge university'

	def student():
		nonlocal name
		name  = 'Sub function student name is: Raffi Bonar'
		print(f'\n 1. {name}')

	student() #sub function
	print(f'\n 2. {name}')

university() # main function