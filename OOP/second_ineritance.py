
class Dog(object):
	# Here we initionlise the class, self represent an instance of Dog
	def __init__(self, name, age, gender):
		self.name = name
		self.age  = age
		self.gender = gender


	def description(self):
		print(f'My pets name is {self.name}, age {self.age}, and he is {self.gender}.')

	def speak(self):
		print('Bark !')


# Inheritance

class Cat(Dog):
	# This is constructor method and super() stand for Dog class here.
	# if I define description method here we will overwrite the privouse one
	# in dog class
	def __init__(self, name, age, gender, color):
		super().__init__(name, age, gender)
		self.color = color

	def speak(self):
		print('Meow !')


mydog = Dog('Raffi', 8, 'male')
mydog.description()
mydog.speak()


mycat = Cat('Mimi', 2, 'female', 'black')
mycat.description()
mycat.speak()


