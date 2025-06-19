from calendar import weekday


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
        return self.firstname, self.lastname, self.salary

    def pay_raise(self):
        self.salary = int(self.salary * self.raise_payment)

    # This only to explain not need here
    # def format_timestamp(cls, dt):
    #     y, m, d, hour, minute, second, weekday, jday, dst = _time.localtime(dt)
    #     return cls(y, m, d)
    #
    # @classmethod
    # def to_day(cls):
    #     dt = _time.time()
    #     return cls.format_timestamp(dt)

    # create class method
    @classmethod
    def set_raise_payment(cls, amount):
        cls.raise_payment = amount

    @classmethod
    def fromat_str(cls, emp_str):
        fname, lname, salary = emp_str.split('-')
        return cls(fname, lname, salary)

    @staticmethod
    def is_workiny_day(day):
        # weekday start from 0 Mo, 1 Tu, 2 We, 3 Th, 4 Fr, 5 St, 6 Su
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


first_emp = Employee('Dilshad', 'Abdulla', 47000)
second_emp = Employee('Tom', 'Smith', 55000)
# Before change raise payment (amount)
# print(Employee.raise_payment)
# print(first_emp.raise_payment)
# print(first_emp.raise_payment)

# print('===========================\n')
# After change raise payment (amount)
# Employee.set_raise_payment(1.08)
# print(Employee.raise_payment)
# print(first_emp.raise_payment)
# print(first_emp.raise_payment)

add_emp_1 = 'George-Adam-59000'
add_emp_2 = 'Julia-Smith-62000'
add_emp_3 = 'Monika-Boston-73500'

new_emp_1 = Employee.fromat_str(add_emp_1)
new_emp_2 = Employee.fromat_str(add_emp_2)
new_emp_3 = Employee.fromat_str(add_emp_3)

print(new_emp_1.email)
print(new_emp_1.salary)

print(new_emp_1.firstname, new_emp_1.lastname, new_emp_1.salary)
print(new_emp_2.firstname, new_emp_2.lastname, new_emp_2.salary)
print(new_emp_3.firstname, new_emp_3.lastname, new_emp_3.salary)

print('==============================\n')

import datetime
today = datetime.date(2024, 9, 13)
print(Employee.is_workiny_day(today))

today = datetime.date(2024, 9, 14)
print(Employee.is_workiny_day(today))