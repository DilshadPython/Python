
def welcome_msg(greeting, name=' Dilshad'):
	return '{}, {}'.format(greeting, name)

print(welcome_msg('Hello, '))

print()
def user_details(*args, **kwargs):
	print(args)
	print(kwargs)


user_details('Dilshad', 'dilshad@gmail.com', age=41, sex='Male')

print()

more_info = ['Thom', 'Studnet']
details = {'Uni': 'Anglia University', 'city': 'Chelmsford', 'build': 2000}

user_details(more_info, details)

print('\n ==================')
user_details(*more_info, **details)