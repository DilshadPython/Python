class Person:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

instance_obj = Person('Tomas')
print('\n List of functions owned to the instance_obj to class Person:')
print(dir(instance_obj))