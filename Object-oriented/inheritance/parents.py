''' 
Inheritance allowed us to inheritace a attribute and method in the parent class 
'''

# clas variables
class Parent:

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age


	def parent_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.last_name, self.age)

	def fullname(self, first_name, last_name):
		return '{} {}'.format(self.first_name, self.last_name)



	def email_address(self):
		return '{}.{}'.format(self.first_name, self.last_name) + '@' + 'gmail.com'


class Son(Parent):
	pass

class Daughter(Parent):
	pass


obj_1 = Daughter('Adam', 'Sophia', '25')
obj_2 = Daughter('Adam', 'Claudia', '31')
obj_3 = Son('David', 'Tom', '33')
obj_4 = Son('David', 'Jeff', '29')


print(obj_1.first_name + ' ' + obj_1.last_name + ' ' + obj_1.age)
print(obj_1.email_address())
print(obj_2.first_name + ' ' + obj_2.last_name + ' ' + obj_2.age)
print(obj_2.email_address())

print('=============================================================')

print(obj_3.first_name + ' ' + obj_3.last_name + ' ' + obj_3.age)
print(obj_3.email_address())
print(obj_4.first_name + ' ' + obj_4.last_name + ' ' + obj_4.age)
print(obj_4.email_address())