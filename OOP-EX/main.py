import csv


class Product:
    # we create attribute for the class attribute, this is if the payment more then 25% discount
    pay_discount = 0.73
    all = []

    # we initionalise the class by creating __init__ method or constractor
    # we can also give the quantity to each product in init method directly and removed from created obj

    def __init__(self, name: str, price: float, quantity=0):
         # We use assert as validations method which is show the number must be posative always
        # if we add -5 or -7 it will automatically tell must be posative
        assert price >= 0, f'Price {price} is not greater than or equal to 0 !'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to 0 !'

        print(f'We initialized the class by created an instance: {name}, {price}, {quantity}')
        # we assigned the class to each attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Product.all.append(self)

    # def calculate_total_price(self, i, j):
    #     return i * j
    # while we assiged the price and quantity in the class we can access to the attribute by using self
    # and removed i, j from the method
    def calculate_total_price(self):
        return self.price * self.quantity

    # create method to access to pay_discount
    def get_discount(self):
        '''
        if you use Product instead of self when you update pay_discount doesn't change the
        discount for instance item, but if you changed to self the discount will be update in line
        where we update pay_discount: obj1.pay_discount = 0.623
        '''
        # self.price = self.price * Product.pay_discount
        self.price = self.price * self.pay_discount

    # Read data from csv file
    @classmethod
    def read_instance_date_from_csv_file(cls):
        # we will convert instance method to klass method instead of self use cls
        with open('csv_files.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = list(reader)

        for product in products:
            # print(product)
            Product(
                name=product.get('name'),
                price=float(product.get('price')),
                quantity=int(product.get('quantity')),
            )

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


# Create an object of the class
# obj = Product()
# now we add the name directly to the class
# obj = Product('Mobile', 49.99, 44)
obj = Product('Mobile', 49.99, 17)
# obj.name = str('Mobile')
# obj.price = float(49.99)
# obj.quantity = int(234)

# Here we create another obj from the same class and adding new items the attribute not changed but the
# new obj1
# is given to display different result
# obj1 = Product()
# obj1 = Product('Television', 159.48, 17)
obj1 = Product('Television', 159.48, 29)
# obj1.item_name = str('Television')
# obj1.item_price = float(159.48)
# obj1.quantity = int(74)


# total_price = obj.price * obj.quantity
# The obj stand for self in the method, obj.item_price stand for i and obj.quantity stand for j
# print(obj.name)
# print(obj.calculate_total_price(obj.price, obj.quantity))
print(obj.calculate_total_price())

# print(obj1.name)
# print(obj1.calculate_total_price(obj1.price, obj1.quantity))
print(obj1.calculate_total_price())

# print(type(obj.name))
# print(type(obj.price))
# print(type(obj.quantity))

# This is the class attribute
print('This is the class attribute: ', Product.pay_discount)
# This is instance attribute, because the pay_discount has not been define in instance level (__init__)
print('This instance level: ', obj.pay_discount)
print('This instance level: ', obj1.pay_discount)

print()
# This will display all attributes belong to class level
print('This will display all attributes belong to class level: ', Product.__dict__, '\n')
'''
Infor the __dict__ will saperate which attribute belong to class level and which which
attribute belong to instance level, inother words you can see the pay_discount in class attribute but
you don't see the pay_discount in instance attribute, you can use as debug I mean __dict__
'''
# This will display all attributes belong to instance level
print('This will display all attributes belong to instance level: ', obj.__dict__, '\n')

# Here calculte the get_discount
obj.get_discount()
print('Here we get discount for the price it will be 0.73 : ', obj.price)

obj1 = Product('Mobile', 49.99, 4)
obj1.pay_discount = 0.623
obj1.get_discount()
print('After update the pay desicount it will be 0.623 : ', obj1.price)


print()
print('Product.all', ' \t Here all use __repr__ method ')
print(Product.all)

# print()
# obj2 = Product('Desktop', 450.99, 17)
# obj3 = Product('Samsung', 399.99, 12)
# obj4 = Product('IPad 10', 689.99, 22)
# obj5 = Product('Iphone 13', 799.59, 34)
# obj6 = Product('Ausus Laptop 15', 500.48, 11)

# print('Use for loops:')
# # print(Product.all)
# for obj in Product.all:
#     print(obj.name, '\t', obj.price, '\t', obj.quantity)

print()
print('Here we use read_instance_date_from_csv_file() as classmethod to display all date from csv file:')
# Product.read_instance_date_from_csv_file()
print(Product.all)

# stopped at 1:03 minutes and the float dispaly an error NoneType line 56 and 143
