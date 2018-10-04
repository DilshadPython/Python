
def username():
	fname = input('Enter your first name: ')
	a = str(fname)
	lname = input('Enter your last name: ')
	b = str(lname)
	age = input('Enter you age: ')
	c = int(age)
	details = a.upper() + ' ' + b.upper() 
	return f'\n Your full name is {details} and your age is {c}'

print(username())