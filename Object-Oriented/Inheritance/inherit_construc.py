import random
'''
# __init__ is like any other method; it can be inherited 
if the class doesn't have __init__ constructor, Python will check its parent class
to see if can fine one
# As soon as it findes one, Python calls it and stops looking
# We use the super()function to call methods in the parents class
# We may want to intialize in the parents as well as our own class
'''
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
