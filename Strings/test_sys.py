import sys
print(sys.executable)
print(sys.version)


class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def test_function(self):
        pass

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname, self.lastname)

    @property
    def full_name(self):
        return '{} {}'.format(self.firstname, self.lastname)


myobj = Employee('Dilshad', 'Abdulla')
print(myobj.email)
print(myobj.full_name)
