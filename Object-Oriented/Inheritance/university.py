import random
'''
# __init__ is like any other method; it can be inherited 
if the class doesn't have __init__ constructor, Python will check its parent class
to see if can fine one
# As soon as it finds one, Python calls it and stops looking
# We use the super()function to call methods in the parents class
# We may want to initialize in the parents as well as our own class
'''
class University:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return '%s %s' % (self.fname, self.lname)


class Student(University):
    pass
# This will tell you how to inherited each new classes from university class and initialized
# print(help(Student))

first_std = Student('Dilshad', 'Abdulla')
second_std = Student('Claudia', 'Tom')

print(first_std.full_name())
print(second_std.full_name())
