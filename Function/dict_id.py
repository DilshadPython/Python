
'''
Create function called studentid  
'''

list_student_id = {
	814747: 'Dilshad Abdulla',
	805824: 'Tom Tawi',
	853654: 'Adam Silver',
	772564: 'Susan Doe'
}

def get_studid(input):
	print('814747', '772564', '853654', '805824')
	enter_id = int(input('Please enter the id number: '))
	return print('Hello  %s'% list_student_id.get(enter_id, ' known user which is not registered'))

get_studid(input)