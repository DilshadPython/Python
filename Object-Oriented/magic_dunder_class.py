
class Employee:

    raise_payment = 1.05
    # we use the __init__() function to assign values for name and salary and access to it
    def __init__(self, fname, lname, city, salary):
        self.fname = fname
        self.lname = lname
        self.city = city
        self.salary = salary
        self.email = fname + '.' + lname + '@gcompany.com'

    def details(self):
        return '{} {} {} {}'.format(self.fname, self.lname, self.city, self.salary)

    def pay_raise(self):
        self.salary = int(self.salary * self.raise_payment)

    def __repr__(self):
        return "Employee('{}', '{}', '{}, '{}')".format(self.fname, self.lname, self.city, self.salary)

    # any func start with __str__ or __repr__ or __init__ are called dunder method
    def __str__(self):
        return '{} - {}'.format(self.details(), self.email)

    # create another dunder method to calculate amout of salary
    def __add__(self, other):
        return self.salary + other.salary

    # this method is use to read the len of the name character
    def __len__(self):
        return len(self.details())

emp_one = Employee('Dilshad', 'Abdulla', 'Berlin', 45000)
emp_two = Employee('Tom', 'Smith', 'Paris', 54000)

print(emp_one)
print('===============================\n')
print(repr(emp_one))
print(str(emp_one))
print('###############################\n')
print(repr(emp_two))
print(str(emp_two))

print('*******************************\n')
print(emp_one.__repr__())
print(emp_one.__str__())

print('===============================\n')
print(str.__add__('Tom', 'Smith'))
print(int.__add__(23, 76))

print('################################\n')
# Here we use __add__ method to calculate both salary
print(emp_one + emp_two)

# Here we read the length of details employee one (Dilshad Abdulla Berlin 45000 == 28)
print('*******************************\n')
print(len(emp_one))