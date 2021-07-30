# class variables or class attribute and instance attribute
class Car:
    # class veriable
    class_var = 20
    number_in_the_store = 0

    def set_price(self):
        self.instance_var = 25
        self.number_in_the_store = 3



obj = Car()
# To access the instance variable or attribute we must call the set_price() method first
# to call instance_var otherwise display an error
obj.set_price()

print('Calling class variable: ', obj.class_var)
print('the number in the store is: ', obj.number_in_the_store)

print('Calling instance variable: ', obj.instance_var)
