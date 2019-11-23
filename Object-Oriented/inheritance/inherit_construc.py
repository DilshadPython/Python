import random


class University(object):
    def __init__(self, name):
        self.name = name


class Student(University):
    def __init__(self, name):
        super(Student, self).__init__(name)
        self.departments = random.choice(['Business and Law', 'Science and Engineering',
                                          'Humanities and Social Sciences', 'English and Media'])

    def study(self, depart):
        print('%s is study at %s departments in Anglia Ruskin Univeristy' %
              self.name, self.depart)


std_obj = Student('Dilshad')

print(std_obj.name)
print(std_obj.departments)
