# coding: utf8

class Book:
	pass


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