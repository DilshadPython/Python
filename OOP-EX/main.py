class Product:
    def calculate_total_price(self, i, j):
        return i * j


# Create an object of the class
obj = Product()

obj.item_name = str('Moble')
obj.item_price = float(49.99)
obj.quantity = int(234)

# total_price = obj.item_price * obj.quantity
# The obj stand for self in the method, obj.item_price stand for i and obj.quantity stand for j
obj.calculate_total_price(obj.item_price, obj.quantity)

print(type(obj.item_name))
print(type(obj.item_price))
print(type(obj.quantity))
