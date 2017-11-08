# coding: utf8

class Student:
	# initialse methode or constracture methods
	def __init__(self, first_name, last_name, id_num):
		self.first_name = first_name
		self.last_name = last_name
		self.id_num = id_num 
		self.email = first_name + '.' + last_name + '@anglia.edu'



obj_1 = Student('Dilshad', 'Abdulla', '0814747')
obj_2 = Student('Tom', 'Eduard', '0815474')

print(obj_1.first_name, obj_1.last_name, obj_1.id_num, obj_1.email)
print(obj_2.first_name, obj_2.last_name, obj_2.id_num, obj_2.email)

print('{} {}'.format(obj_1.first_name, obj_1.last_name))
print('{} {}'.format(obj_2.first_name, obj_2.last_name))
print('{}'.format(obj_1.id_num))
print('{}'.format(obj_2.id_num))

# overwritten
obj_1.first_name = 'Helen'
print(obj_1.first_name)

obj_2.first_name = ' Ellen'
obj_2.id_num = '8798765'

print(obj_2.first_name + ' << | >> ' + obj_2.id_num)

print('###'*20)

obj_3 = Student('Tilly', 'Raffi', 67)

print(obj_3.id_num)
