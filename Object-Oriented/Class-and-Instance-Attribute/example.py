# class variables or class attribute and instance attribute
class Car:
    # class veriable
    class_var = 20
    number_in_the_store = 0

    def set_price(self):
        self.instance_var = 25
        self.number_in_the_store = 3



obj = Car()
# Here we call the number_in_the_store before instance method set_price
print('\nCalling class variable: ', obj.class_var)
print('\nthe number in the store is: ', obj.number_in_the_store)

# To access the instance variable or attribute we must call the set_price() method first
# to access instance_var otherwise display an error
obj.set_price()

print('\nCalling instance variable: ', obj.instance_var)
print('\nThe number in the store is: ', obj.number_in_the_store)