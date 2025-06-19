class Employee:
    # we use the __init__() function to assign values for name and age and access to it
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.email = fname + '.' + lname + '@company.com'

    def details(self):
        return '{}, {}, {}'.format(self.firstname, self.lastname, self.age)
        # or another way still works
        # return self.firstname, self.lastname, self.age

first_emp = Employee('Dilshad', 'Abdulla', 44)
second_emp = Employee('Tom', 'Smith', 54)

print(first_emp.details())
print(first_emp.email)
print('==============================\n')
print(second_emp.details())
print(second_emp.email)