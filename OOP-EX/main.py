class Product:
    # We use assert as validations method which is show the number must be posative always
    # if we add -5 or -7 it will automatically tell must be posative
    assert price >= 0, f'Price {price} is not greater than or equal to 0 !'
    assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to 0 !'

    # we initionalise the class by creating __init__ method or constractor
    # we can also give the quantity to each product in init method directly and removed from created obj
    def __init__(self, name: str, price: float, quantity=0):
        print(f'We initialized the class by created an instance: {name}, {price}, {quantity}')
        # we assigned the class to each attribute
        self.name = name
        self.price = price
        self.quantity = quantity

    # def calculate_total_price(self, i, j):
    #     return i * j
    # while we assiged the price and quantity in the class we can access to the attribute by using self
    # and removed i, j from the method
    def calculate_total_price(self):
        return self.price * self.quantity


# Create an object of the class
# obj = Product()
# now we add the name directly to the class
# obj = Product('Mobile', 49.99, 44)
obj = Product('Mobile', 49.99, 17)

# obj.name = str('Mobile')
# obj.price = float(49.99)
# obj.quantity = int(234)


# total_price = obj.price * obj.quantity
# The obj stand for self in the method, obj.item_price stand for i and obj.quantity stand for j
# print(obj.name)
# print(obj.calculate_total_price(obj.price, obj.quantity))
print(obj.calculate_total_price())

# Here we create another obj from the same class and adding new items the attribute not changed but the new obj1
# is given to display different result
# obj1 = Product()
# obj1 = Product('Television', 159.48, 17)
obj1 = Product('Television', 159.48, 29)
# obj1.item_name = str('Television')
# obj1.item_price = float(159.48)
# obj1.quantity = int(74)

# print(obj1.name)
# print(obj1.calculate_total_price(obj1.price, obj1.quantity))
print(obj1.calculate_total_price())

# print(type(obj.name))
# print(type(obj.price))
# print(type(obj.quantity))
