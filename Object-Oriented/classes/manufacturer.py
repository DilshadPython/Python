
class Car:

    profit = 1.09

    def __init__(self, name, model, color, types, price):
        self.name = name
        self.model = model
        self.color = color
        self.types = types
        self.price = price

    def car_detail(self):
        return '{}, {}, {}, {}'.format(self.name, self.model, self.color, self.types, self.price)

    def payment(self):
        self.price = float(self.price * self.profit)

instance_audi = Car('Audi', 2017, 'Black', 'S3', 33.000)
instance_bmw = Car('BMW', 2016, 'Gray', 'Z3', 28.500)

print('Audi price before: ', instance_bmw.price)
instance_audi.payment()
print('Audi price with profit: ', instance_audi.price)

print('########################################################')

print('BMW price before: ', instance_bmw.price)
instance_bmw.payment()
print('BMW price with profit: ', instance_bmw.price)
