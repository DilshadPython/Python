# coding: utf8

# Class is a blueprint for an instance
# Type: Indectats the class the instance belong to
# Attribute: Any object value
# Method: A callable attribute define in the class
class Book:
    pass

# obj_1 is instance: A constructed object of the class
obj_1 = Book()
obj_2 = Book()

obj_1.first = 'Data Science'
obj_2.last = 'Computer Science'
obj_1.cost = 20
obj_2.cost = 39

obj_1.owner = 'Martin SHulter'
obj_2.owner = 'Tomas Adam'

print(obj_1.cost)
print(obj_2.cost)
print(obj_1.owner)
print(obj_2.owner)
