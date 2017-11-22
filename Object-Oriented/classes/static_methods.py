''' 
regular method and class method will taken the instance as first argument which 
is self in the car_detail or payment method in this example
'''
import datetime


# clas variables
class Car:

	profit = 1.09
	number_in_the_store = 0

	def __init__(self, name, model, color, types, price):
		self.name = name
		self.model = model
		self.color = color
		self.types = types 
		self.price = price


		Car.number_in_the_store += 1


	def car_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.model, self.color, self.types, self.price)


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

	@staticmethod
	def is_not_workday(day):
		if day.weekday == 5 or day.weekday == 6:
			return False
		return True

obj_one = Car('Audi', 2017, 'Black', 'S3', 33.000)
obj_two = Car('BMW', 2016, 'Gray', 'Z3', 28.500)


off_days = datetime.date(2017, 3, 28)

print(' The date of 28 March 2017 is Tuesday not weekend the answer is\
		 true but if is 25 or 26 than is Saturday and Sundy')
print(Car.is_not_workday(off_days))