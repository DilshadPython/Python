
def view_email(email):
	return f'{email} is your email.'

print(view_email(input('Enter your email address: ')))


def welcome(name):
	return ' Hello {} welcome to function!.'.format(name) + view_email(input('\n Enter your email: '))

print(welcome(' Tome '))