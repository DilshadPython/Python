
student_name = 'Dilshad Abdulla'

student = 'Dilshad Abdulla'

print(student_name == student)

print('\n ')

print(student_name is student)

print('\n ')
print(id(student_name))
print(id(student))

print('\n====================================')

mylist = ['Python', 3.6, 2018]
yourlist = ['Python', 3.6, 2018]

print(mylist == yourlist)

print('\n ')
print(mylist is yourlist)

print('\n ')

print(id(mylist))
print(id(yourlist))

print('\n ')
print('\n==================================')
mylist = yourlist
print(mylist == yourlist)

print('\n ')
print(mylist is yourlist)

print('\n ')

print(id(mylist))
print(id(yourlist))

print('\n ')
print(id(mylist) == id(yourlist))
print(id(mylist) is id(yourlist))
