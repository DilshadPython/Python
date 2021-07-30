# InstanceCounter
class Car:
    # class variable/attribute
    number_in_the_store = 0

    def __init__(self, number):
        self.number = number
        # instance variable/attribute we can't increment by 1 because set as 0
        Car.number_in_the_store += 1

    def set_number(self, new_num):
        self.number = new_num

        
    def get_number(self):
        return self.number

    def get_count(self):
        return Car.number_in_the_store

obj_1 = Car(4)
obj_2 = Car(12)
obj_3 = Car(27)

for obj in (obj_1, obj_2, obj_3):
    # We initialized numer (4, 12, 27)
    print('number of obj is: %s' % (obj.get_number()))
    # the result will be 3 because we have define 3 objects with different 
    # number as kwarg
    print('Count is %s' % obj.get_count()) 