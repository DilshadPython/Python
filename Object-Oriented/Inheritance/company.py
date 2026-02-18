class Company:
    pay_more = 1.03
    staff_number = 10

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@mail.com'

    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)

    def increase_salary(self):
        self.salary = int(self.salary * self.pay_more)

class Staff(Company):
    pay_more = 1.07
                # this staff class arguments
    def __init__(self, fname, lname, salary, skill):
        # super here means the company class
        super().__init__(fname, lname, salary)
        self.skill = skill

class Manager(Company):
                # this is manager class arguments
    def __init__(self, fname, lname, salary, employees=None):
        super().__init__(fname, lname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_empl(self, employee):
        if employee is self.employees or None: # we can't say not in because we already set employees=None
            self.employees.append(employee)

    def remove_empl(self, employee):
        if employee is not self.employees:
            self.employees.remove(employee)

    def total_empl(self):
        for employee in self.employees:
            print('\n:', employee.full_name())

# print(help(Manager))
stf = Staff('Tome', 'Henrry', 55000, 'Python')
print(stf.full_name())

print()
# Here where increase the salary by staff request
new_staff = Staff('Goe', 'Philips', 7000, 'Java')
new_staff_1 = Staff('Maya', 'Alpha', 6500, 'PHP')

print(new_staff.salary)
new_staff.increase_salary()
print(new_staff.salary)
print(new_staff.skill)
print(new_staff.email)
print(new_staff.full_name())

print()
# Create new manager
mang = Manager('Georgina', 'Holland', 6000, '[new_staff]')

# we have employee one new_staff
# print(mang.total_empl())
print(mang.email)
print(mang.full_name())

# now we employee new staff by manager
mang.add_empl(new_staff_1)
# print(mang.total_empl()) get an error not sure why
print(isinstance(mang, Company))
print(isinstance(mang, Manager))
print(isinstance(new_staff, Staff))
print(isinstance(new_staff, Company))

# But here is false
print(isinstance(new_staff, Manager))
print(isinstance(mang, Staff))

print()
# This is True
print(issubclass(Manager, Company))
print(issubclass(Staff, Company))

# this is not False
print(issubclass(Manager, Staff))
print(issubclass(Staff, Manager))