
class Car:

	def __init__(self, name, model, color, types, price):
		self.name = name
		self.model = model
		self.color = color
		self.types = types 
		self.price = price


	def car_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.model, self.color, self.types, self.price)


	def payment(self):
		self.price = float(self.price * 1.01)

instance_audi = Car('Audi', 2017, 'Black', 'S3', 33.000)
instance_bmw = Car('BMW', 2016, 'Gray', 'Z3', 28.500)

print('Audi price before: ', instance_bmw.price)
instance_audi.payment()
print('Audi price after: ', instance_audi.price)

########################################################
print('BMW price before: ', instance_bmw.price)
instance_bmw.payment()
print('BMW price after: ', instance_bmw.price)
