# class variables
class Car:
    # class veriable
    class_var = 20
    number_in_the_store = 0

    def set_price(self):
        self.instance_var = 25
     

        # instance variable
        Car.number_in_the_store += 1

obj = Car()
# To access the instance variable or attribute we must call the set_price() method first
# to call instance_var otherwise display an error
obj.set_price()

print('Calling class variable: ',obj.class_var)
print('Calling instance variable: ', obj.instance_var)