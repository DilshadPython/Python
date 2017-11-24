
class Book:

	def __init__(self, first_name, last_name, author, year):
		self.first_name = first_name
		self.last_name = last_name
		self.author = author
		self.year = year 
		

	@property
	def full_name(self):
		return '{}.{}'.format(self.first_name, self.last_name)

	'''
	property will give access to the new overwriting to get the update to the email when the names 
	has been change look at the obj_1.email with out () print(obj_1.email) in other word we have access
	to the email method as an attribute not as a method
	'''
	@property
	def email(self):
		return '{} {}@book.edu'.format(self.first_name, self.last_name)

	@full_name.setter 
	def full_name(self, name):
		first_name, last_name = name.split(' ')
		self.first_name = first_name
		self.last_name = last_name

	@full_name.deleter 
	def full_name(self):
		print(' You have deleted the fullname')
		self.first_name = None 
		self.last_name = None 


obj_1 = Book('Claus', 'Timo', 'The Europe', 2014)
obj_2 = Book('Alan', 'Alex', 'Sun of Sand', 2001)

print(obj_1.first_name)
print(obj_1.email)
print(obj_1.full_name)

print('\nOverwrite the first name see what is change')
print('\n###########################################')

obj_1.full_name = 'Raffi Tilly'

print(obj_1.first_name)
print(obj_1.email)
print(obj_1.full_name)

print('\nThanks you clear the name or deleted')
del obj_1.full_name