"""
Demonstrates custom object sorting using lambda functions and operator.attrgetter.
"""

from operator import attrgetter

class Student:
    def __init__(self, student_id: int, fname: str, lname: str):
        self.id = student_id
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'<Student ID={self.id} Name="{self.fname} {self.lname}">'

def demo_custom_object_sorting():
    students = [
        Student(1254, 'John', 'Smith'),
        Student(3254, 'Michael', 'David'),
        Student(3124, 'James', 'Smith'),
    ]
    print('Original students list:', students)

    # Sort using lambda key by ID
    by_id = sorted(students, key=lambda s: s.id)
    print('\nSorted by ID (lambda):', by_id)

    # Sort using lambda key by first name
    by_fname = sorted(students, key=lambda s: s.fname)
    print('Sorted by First Name (lambda):', by_fname)

    # Sort using operator.attrgetter (faster C implementation)
    by_lname = sorted(students, key=attrgetter('lname'))
    print('Sorted by Last Name (attrgetter):', by_lname)

    return by_id, by_fname, by_lname

if __name__ == '__main__':
    demo_custom_object_sorting()
