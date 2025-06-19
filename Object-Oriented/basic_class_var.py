class Employee:

    add_new_employ = 0
    raise_payment = 1.05
    # we use the __init__() function to assign values for name and salary and access to it
    def __init__(self, fname, lname, salary):
        self.firstname = fname
        self.lastname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'

        Employee.add_new_employ += 1

    def details(self):
        return '{}, {}, {}'.format(self.firstname, self.lastname, self.salary)
        # or another way still works
        # return self.firstname, self.lastname, self.salary

    def pay_raise(self):
        self.salary = int(self.salary * self.raise_payment)

# Display the employee before we employee or adding two employee in the line 22 and 23
print('Total Employee: ', Employee.add_new_employ)

first_emp = Employee('Dilshad', 'Abdulla', 47000)
second_emp = Employee('Tom', 'Smith', 55000)

print('==========================\n')
# Tips
# we can't access to instance variable here like raise_payment
print(first_emp.__dict__)
print('==========================\n')
# we can access to raise_payment here
print(Employee.__dict__)

print(first_emp.salary)
first_emp.pay_raise()
print('Calculate pay extra salary by 1.05 ')
print(first_emp.salary)

print('==========================\n')
# Tips
print(first_emp.__dict__)
print('==========================\n')
print(Employee.__dict__)

# Here we can make a payment different for the first employee only not the second employee
first_emp.raise_payment = 1.08
print('Calculate pay extra salary by 1.08 ')
first_emp.pay_raise()
print(first_emp.salary)
print(second_emp.salary)

# Display the employee after adding two employee in the line 22 and 23
print('Total Employee: ', Employee.add_new_employ)
