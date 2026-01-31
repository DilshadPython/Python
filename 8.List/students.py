class Student:
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.id} {self.fname} {self.lname}'

std_one = Student(1254, 'John', 'Smith')
std_two = Student(3254, 'Michael', 'David')
std_three = Student(3124, 'James', 'Smith')

students = [std_one, std_two, std_three]
# use Lambda is a compute service that lets you run code without provisioning or managing services.
std_sorted = sorted(students, key=lambda student: student.id)

print()
print('\t sorted by ID ', std_sorted)

def sort_student(stdn):
    return stdn.id #, stdn.fname, stdn.lname

print()
print('\t std_one ID ', sort_student(std_one))

print()
lst_student = sorted(students, key=sort_student)
print('\t', lst_student)

print()
revese_student = sorted(students, key=sort_student, reverse=True)
print('\t reverse ', revese_student)

def sort_student(stdn):
    return stdn.fname

print()
fname_student = sorted(students, key=sort_student)
print('\t sorted by fname ', fname_student)

def sort_student(stdn):
    return stdn.lname

print()
lname_student = sorted(students, key=sort_student)
print('\t sorted by lname ', lname_student)

# Another way to sorted use the attrgetter
from operator import attrgetter
std_list = sorted(students, key=attrgetter('fname'))

print()
print('\t sorted by fname ', std_list)

std_list = sorted(students, key=attrgetter('lname'))

print()
print('\t sorted by lname ', std_list)