# InstanceCounter
class Car:
    # class variable/attribute or class Data
    attr_count = 0

    def __init__(self, number):
        # number is instance Data
        self.number = number
        # instance variable/attribute we can't increment by 1 because set as 0
        Car.attr_count += 1
        # This is still working but doesn't count the instance value of Car(), here the count == 0
        # self.attr_count += 1

    def set_number(self, new_num):
        self.number = new_num

        
    def get_number(self):
        return self.number

    def get_count(self):
        return Car.attr_count
        # This is still working but doesn't count the instance value of Car() here the count == 0
        # return self.attr_count

# instance object, we created 5 instance obj
obj_1 = Car(4)
obj_2 = Car(12)
obj_3 = Car(27)
obj_4 = Car(33)
obj_5 = Car(9)

for obj in (obj_1, obj_2, obj_3, obj_4, obj_5):
    # We initialized numer (4, 12, 27)
    print('\nNumber of obj is: %s' % (obj.get_number()))
    # the result will be 3 because we have define 3 objects with different 
    # number as kwarg
    print('\nCount is %s' % obj.get_count()) 
    print(obj.attr_count, ' < calling instance obj to class attribut display same aboout like get_count()')
