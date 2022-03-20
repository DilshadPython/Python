class Product:
    def calculate_total_price(self, i, j):
        return i * j


# Create an object of the class
obj = Product()

obj.item_name = str('Mobile')
obj.item_price = float(49.99)
obj.quantity = int(234)


# total_price = obj.item_price * obj.quantity
# The obj stand for self in the method, obj.item_price stand for i and obj.quantity stand for j
print(obj.item_name)
print(obj.calculate_total_price(obj.item_price, obj.quantity))

# Here we create another obj from the same class and adding new items the attribute not changed but the new obj1
# is given to display different result
obj1 = Product()
obj1.item_name = str('Television')
obj1.item_price = float(159.48)
obj1.quantity = int(74)

print(obj1.item_name)
print(obj1.calculate_total_price(obj1.item_price, obj1.quantity))

print(type(obj.item_name))
print(type(obj.item_price))
print(type(obj.quantity))
