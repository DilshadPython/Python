class Product:
    pass


# Create an object of the class
obj = Product()

obj.item_name = str('Moble')
obj.item_price = float(49.99)
obj.quantity = int(234)

total_price = obj.item_price * obj.quantity

print(type(obj.item_name))
print(type(obj.item_price))
print(type(obj.quantity))
