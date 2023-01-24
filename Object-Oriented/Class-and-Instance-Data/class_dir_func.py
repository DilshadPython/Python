class Person:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


instance_obj = Person('Tomas')
print('\n List of functions owned to Person class:')
print('===========================================')
print(dir(Person))
print('==================================================\n')
print(' A - ', instance_obj.__class__)
print(' B - ', instance_obj.__delattr__)
print(' C - ', instance_obj.__dict__)
print(' D - ', instance_obj.__dir__)
print(' E - ', instance_obj.__doc__)
print(' F - ', instance_obj.__eq__)
print(' G - ', instance_obj.__format__)
print(' H - ', instance_obj.__ge__)
print(' I - ', instance_obj.__getattribute__)
print(' J - ', instance_obj.__gt__)
print(' K - ', instance_obj.__hash__)
print(' L - ', instance_obj.__init__)
print(' M - ', instance_obj.__init_subclass__)
print(' N - ', instance_obj.__le__)
print(' O - ', instance_obj.__lt__)
print(' P - ', instance_obj.__lt__)
print(' Q - ', instance_obj.__ne__)
print(' R - ', instance_obj.__new__)
print(' S - ', instance_obj.__reduce__)
print(' T - ', instance_obj.__reduce_ex__)
print(' U - ', instance_obj.__repr__)
print(' V - ', instance_obj.__setattr__)
print(' W - ', instance_obj.__sizeof__)
print(' X - ', instance_obj.__str__)
print(' Y - ', instance_obj.__subclasshook__)
print(' Z - ', instance_obj.__weakref__)

