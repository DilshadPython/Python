'''
Animal are inheiate from object 
'''
class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name

	def eat(self, food):
		print('%s is eating %s' % (self.name, food))


class Dog(Animal):
	def fetch(self, thing):
		print('%s goes after the %s' % (self.name, thing))

class Cat(Animal):
	def swatstring(self):
		print('%s shreds the string!' % (self.name))

dog_obj = Dog('Raffi')
cat_obj = Cat('Smikey')

dog_obj.fetch('paper') # Raffi  goest after paper
cat_obj.swatstring()

dog_obj.eat('Dog food')
cat_obj.eat('Cat food')
print('The dog object has no access Cat object \
and the cat object has no access to the dog Object \
but both cat and dog objects has access to Animal object because the inheritae \
from Animal Class which is Parent class.')
'''
The dog object has no access Cat object
and the cat object has no access to the dog Object
but both cat and dog objects has access to Animal object because the inheritae
from Animal Class which is Parent class.
Traceback (most recent call last):
  File "animal1.py", line 28, in <module>
    x.swatstring()
AttributeError: 'Dog' object has no attribute 'swatstring'
'''
print('\n')
''' This is error just to show how it works '''
dog_obj.swatstring() 
cat_obj.fetch()

