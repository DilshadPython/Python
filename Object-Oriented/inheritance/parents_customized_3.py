''' 
Inheritance allowed us to inheritace a attribute and method in the parent class 
'''

# clas variables
class Parent:

	increse_pay = 0.07

	def __init__(self, first_name, last_name, age, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.salary = salary


	def parent_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.last_name, self.age)

	def fullname(self, first_name, last_name):
		return '{} {}'.format(self.first_name, self.last_name)

	def email_address(self):
		return '{}.{}'.format(self.first_name, self.last_name) + '@' + 'gmail.com'

	def pay_raise(self):
		self.salary = int(self.salary * self.increse_pay + self.salary)


obj = Parent('Tim', 'Alan', '44', 39000)
print(obj.first_name + ' ' + obj.last_name + ' ' + obj.age)
print(obj.email_address())
print(obj.salary)
obj.pay_raise()
print(obj.salary)

print('##############################')

class Son(Parent):
	increse_pay = 0.15

	def __init__(self, first_name, last_name, age, salary, skills):
		'''
		To avoid repeate what is in __init__ method in parent class for all arguments are created first
		we will make a short cut like below
		'''
		super().__init__(first_name, last_name, age, salary)
		# or both correct
		# Parent.__init__(self, first_name, last_name, age, salary)
		self.skills = skills


class Daughter(Parent):
	increse_pay = 0.25
	def __init__(self, first_name, last_name, age, salary, nationality):
		'''
		To avoid repeate what is in __init__ method in parent class for all arguments are created first
		we will make a short cut like below
		'''
		super().__init__(first_name, last_name, age, salary)
		# or both correct
		# Parent.__init__(self, first_name, last_name, age, salary)
		self.nationality = nationality


daughter_1 = Daughter('Adam', 'Sophia', '25', 25000, 'German')
daughter_2 = Daughter('Adam', 'Claudia', '31', 21100, 'American')
son_1 = Son('David', 'Tom', '33', 27000, 'JavaScript')
son_2 = Son('David', 'Jeff', '29', 24500, 'Python language')


print(daughter_1.first_name + ' ' + daughter_1.last_name + ' ' + daughter_1.age, daughter_1.nationality)
print(daughter_1.email_address())
print(daughter_1.salary)
daughter_1.pay_raise()
print(daughter_1.salary)

print('##############################')

print(daughter_2.first_name + ' ' + daughter_2.last_name + ' ' + daughter_2.age, daughter_2.nationality)
print(daughter_2.email_address())
print(daughter_2.salary)
daughter_2.pay_raise()
print(daughter_2.salary)

print('==============================')

print(son_1.first_name + ' ' + son_1.last_name + ' ' + son_1.age, son_1.skills)
print(son_1.email_address())
print(son_1.salary)
son_1.pay_raise()
print(son_1.salary)

print('##############################')

print(son_2.first_name + ' ' + son_2.last_name + ' ' + son_2.age, son_2.skills)
print(son_2.email_address())
print(son_2.salary)
son_2.pay_raise()
print(son_2.salary)


class Director(Parent):
	def __init__(self, first_name, last_name, age, salary, staffs=None):
		'''
		To avoid repeate what is in __init__ method in parent class for all arguments are created first
		we will make a short cut like below
		'''
		super().__init__(first_name, last_name, age, salary)
		# or both correct
		# Parent.__init__(self, first_name, last_name, age, salary)
		if staffs is None:
			self.staffs = []
		else:
			self.staffs = staffs

	def add_staff(self, staff):
		if staff not in self.staffs:
			self.staffs.append(staff)

	def remove_staff(self, staff):
		if staff in self.staffs:
			self.staffs.remove(staff)

	def display_staffs(self):
		for staff in self.staffs:
			print('>>>', staff.fullname(self.first_name, self.last_name))


print('##############################')

director_1 = Director('Nick', 'Herriot', 50, 88500, [son_1])
print(director_1.email_address())

director_1.add_staff(son_2)
director_1.add_staff(daughter_2)
director_1.add_staff(daughter_1)
print('##############################')
director_1.display_staffs()


director_1.remove_staff(son_2)
print('##############################')
director_1.display_staffs()

## Using two methods in python
print(isinstance(director_1, Director))
print(isinstance(daughter_2, Daughter))
print(isinstance(son_1, Son))

print('##############################')
print(isinstance(director_1, Daughter))
print(isinstance(daughter_2, Son))
print(isinstance(son_1, Parent))

print('##############################')
print(issubclass(Daughter, Parent))
print(issubclass(Son, Parent))
print(issubclass(Daughter, Son))
print(issubclass(Son, Director))