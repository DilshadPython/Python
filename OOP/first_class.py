'''
'''

class Dog(object):
	# Here we initionlise the class, self represent an instance of Dog
	def __init__(self, name, age, color, gender):
		self.name = name
		self.age = age
		self.color = color
		self.gender = gender


	def description(self):
		print(f'My dog name is {self.name}, age {self.age}, color {self.color} and he is {self.gender}.')

	# This method has weight which is not define in __init__, we can define it this way
	# if we want
	def get_weight(self, weight):
		self.weight = weight


'''
When you create an object of the class Dog the first method automatically
fired. mydog and other_dog represent self.
'''
mydog = Dog('Raffi', 8, 'white', 'male')
mydog.description()

print(mydog.name)
print(mydog.age)
print(mydog.color)
print(mydog.gender)

mydog.get_weight(12)
print(mydog.weight)
##########################
other_dog = Dog('Tilly', 8, 'brown-white', 'female')
other_dog.description()

other_dog.get_weight(11)
print(other_dog.weight)




