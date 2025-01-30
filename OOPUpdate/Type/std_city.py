import random

class Student:
    def __init__(self):
        self.cities = ['London', 'New York', 'Paris', 'Brentwood']

    def sort(self, fullname):
        print("This full name is " + fullname, ' is live in ',  random.choice(self.cities))

# create an object
student = Student()
student.sort('James')
