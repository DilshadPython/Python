# We create class Product

# obj = Product() create an object of the class

# create an method in the class and self has to be given as first parameter in the function
# which is repersents the instance of this class, by using self keyword we can access the
# attribute s and methods of this class in python.

def calcuate_total_price(self):

# create constractor method __init__ and added the attribute to the constructor, next assignedall
# attribute in constructor method by using self and we can access to each attribut in second
# method
# using self whithout given any parameter in th calculate_total_price method.

# def __init__(self, name, price, quantity=0):
# we assiged each attribute type
def __init__(self, name: str, price: float, quantity=0):


# We use assert as validations method which is show the number must be posative always
# if we add -5 or -7 it will automatically tell must be posative
assert price >= 0, f'Price {price} is not greater than or equal to 0 !'
assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to 0 !'

# Adding __dict__ to the class display all attribute of this model and use the same method
# __dict__ for object or instance display all attribiute for instance level.

# Create a Class attribute:
Use __dict__ to shows the attribute for both class attribut and instance attribute saperate pay_discount
belong to class attribut from instance attribute. next we created get_discount() method to showing how
the class attribute works when we use Product.pay_discount and self.pay_discount and explain the
different when the pay_discount updated to different numbers.'
class-attribute a003e0a] Use __dict__ to shows the attribute for both class attribut and instance
attribute saperate pay_discount belong to class attribut from instance attribute.
Next we created get_discount() method to showing how the class attribute works when we use
Product.pay_discount and self.pay_discount and explain the different when the pay_discount updated
to different numbers

# Create CSV file :
Installed some csv file from sublime text to show the tables in csv file better

# To read the use magic method __repr__()
