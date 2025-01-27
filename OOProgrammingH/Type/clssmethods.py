import random


class Student:
    cities = ['London', 'New York', 'Paris', 'Brentwood']

    # we add @classmethod decorator and change the self to cls
    @classmethod
    def sort(cls, fullname):
        print("This full name is " + fullname, ' is live in ',  random.choice(cls.cities))

# we don't create an object here we will use the class itself
Student.sort('Tony')