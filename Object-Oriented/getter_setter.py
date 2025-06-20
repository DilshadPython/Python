# Getter and setter method
class Employee:

    # we use the __init__() function to assign values for name and access to it
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.myemail = fname + '.' + lname + '@company.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.fname, self.lname)

    def details(self):
        return '{} {} {} {}'.format(self.fname, self.lname, self.myemail)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.fname = None
        self.lname = None

emp_one = Employee('Dilshad', 'Abdulla')
emp_two = Employee('Tom', 'Smith')

print(emp_one.fname)
print(emp_one.myemail)
print(emp_one.fullname)

print('==============================\n')
emp_one.fname = 'Claudia'
print(emp_one.fname)
# here we have used property decorator in both function we can change email() to email & fullname() to fullname
print(emp_one.email)
print(emp_one.fullname)
print(emp_two.fullname)

print('#############################\n')
emp_two.fullname = 'George Alan'
print(emp_two.fname)
print(emp_two.email)
print(emp_two.fullname)

print('=============================\n')
del emp_one.fullname

print(emp_one.email)
print(emp_one.fname)
print(emp_one.fullname)
