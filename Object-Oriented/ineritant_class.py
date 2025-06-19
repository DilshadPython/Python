
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
        return self.fname, self.lname, self.city, self.salary

    def pay_raise(self):
        self.salary = int(self.salary * self.raise_payment)

class Dev(Employee):
    # pass
    raise_payment = 1.07
    def __init__(self, fname, lname, city, pay, program):
        super().__init__(fname, lname, city, pay)
        self.program = program

class Manager(Employee):

    def __init__(self, fname, lname, city, pay, employees=None):
        super().__init__(fname, lname, city, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def total_emp(self):
        for emp in self.employees:
            print('Total is : ', emp.details())



dev_one = Dev('Dilshad', 'Abdulla', 'Berlin', 45000, 'Python')
dev_two = Dev('Tom', 'Smith', 'Paris', 54000, 'Java')

# To find some more info use help() func
# print(help(Dev))

mag_one = Manager('Elmot', 'David', 'Cologne', 85300, [dev_one])
mag_two = Manager('Elen', 'Tommas', 'Munichen', 89800, [dev_two])

print(dev_one.details())
print(dev_one.program)
print(dev_one.email)
print('==============================\n')

print(dev_two.details())
print(dev_two.program)
print(dev_two.email)
print('=============================\n')

# print(dev_one.salary)
# dev_one.pay_raise()
# print(dev_one.salary)
#
# print('=============================\n')
# print(dev_two.salary)
# dev_two.pay_raise()
# print(dev_two.salary)

print(mag_one.details())
print(mag_one.email)
print('=============== Adding developer ===============\n')

# we adding the second dev to the manager one
mag_one.add_emp(dev_two)
mag_one.total_emp()

print('=============== remove developer ===============\n')
# we remove the first emp
mag_one.remove_emp(dev_one)
mag_one.total_emp()

# Check if Manager one is instance from the correct class
print(isinstance(mag_one, Employee))
print(isinstance(mag_one, Manager))
print(isinstance(mag_one, Dev))

print('################################################\n')
# Testing developer
print(isinstance(dev_one, Dev))
print(isinstance(dev_one, Manager))

print('----------------------------------------------\n')
print(issubclass(Dev, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Dev, Manager))