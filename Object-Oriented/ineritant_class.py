
class Employee:

    raise_payment = 1.05
    # we use the __init__() function to assign values for name and salary and access to it
    def __init__(self, fname, lname, city, salary):
        self.firstname = fname
        self.lastname = lname
        self.city = city
        self.salary = salary
        self.email = fname + '.' + lname + '@gcompany.com'

    def details(self):
        return self.firstname, self.lastname, self.city, self.salary

    def pay_raise(self):
        self.salary = int(self.salary * self.raise_payment)

class Dev(Employee):
    pass


dev_one = Dev('Dilshad', 'Abdulla', 'Berlin', 45000)
dev_two = Dev('Tom', 'Smith', 'Paris', 54000)

# To find some more info use help() func
# print(help(Dev))

print(dev_one.details())
print(dev_one.email)
print('==============================\n')
print(dev_two.details())
print(dev_two.email)