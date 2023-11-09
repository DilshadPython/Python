class Car:
	def __init__(self, name, models):
		self.name = name
		self.models = models

	def __str__(self):
		return self.name + ' : '+ str(self.models)

ob_a = Car('Audi', 'A7')
print(ob_a)
print('\nDisplay name only')
print(ob_a.name)

print('\nDisplay only models')
print(ob_a.models)

print('\nSelf is an instead of the methods which is called and it is the same like ob_a')
try:
	print(self.name)
except:
		print('\nWe can not use self as instance object to call the attribute of the methods in the class!')

ob_f = Car('Ford', 'Kuga')
print(ob_f)
