''' 
regular method and class method will taken the instance as first argument which 
is self in the car_detail or payment method in this example
'''

# clas variables
class Car:

	profit = 1.09
	number_in_the_strore = 0

	def __init__(self, name, model, color, types, price):
		self.name = name
		self.model = model
		self.color = color
		self.types = types 
		self.price = price


		Car.number_in_the_strore += 1

		# regular methods
	def car_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.model, self.color, self.types, self.price)

		# regular method
	def payment(self):
		self.price = float(self.price * self.profit)

	'''
	create class method
	'''
	@classmethod
	def set_payment(cls, value):
		cls.profit = value

	@classmethod
	def from_string(cls, car_str):
		name, model, color, types, price = car_str.split('-')
		return cls(name, model, color, types, price)	


obj_one = 'Ford-2010-Black-S3-33.100'
obj_two = 'Mini-2018-Red-M1-28.500'

new_obj = Car.from_string(obj_one)
new_obj_1 = Car.from_string(obj_two)
# name, model, color, types, price = obj_two.split('-')



print(new_obj.name + ' ' + new_obj.model + ' ' + new_obj.color + ' ' + new_obj.types + '|'  + new_obj.price)
print(new_obj_1.name + ' ' + new_obj_1.model + ' ' + new_obj_1.color + ' ' + new_obj_1.types + '|'  + new_obj_1.price)
