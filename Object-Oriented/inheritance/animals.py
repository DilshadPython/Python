class Animals:

	def can_fly(self):
		return False

	def can_speak(self):
		# print('No can\'t speak')
		return False


class Cat(Animals):
	def __init__(self):
		print('Cat is animal')
		self.number_of_foot = 4
		self.run = True

	def can_fly(self):
		print('No cat can\'t fly')
		return False


class Pigen(Animals):
	def __init__(self):
		print('Pigen is not animal')
		self.can_fly()
		self.number_of_foot = 2
		self.run = True

	def can_fly(self):
		print('Yes Pigen can fly')
		return True

my_cat = Cat()
my_cat.can_fly()
my_cat.can_speak()
print(isinstance(my_cat, Cat))
print(issubclass(Cat, Animals))

print('\nAll False')
print(isinstance(my_cat, Pigen))
print(issubclass(Cat, Pigen))

print('')
my_pigen= Pigen()
my_pigen.can_speak()




