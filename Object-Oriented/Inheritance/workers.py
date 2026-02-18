class Company:
    pay_more = 1.03
    staff_number = 10

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def full_name(self):
        return self.fname + ' ' + self.lname

    def increase_salary(self):
        self.salary = self.salary * self.pay_more

class Staff(Company):
    pay_more = 1.07

comp_staff = Company('Goe', 'Philips', 6000)
comp_staff_1 = Company('Maya', 'Alpha', 6500)

# this where paid by company and increase the salary
print(comp_staff.salary)
comp_staff.increase_salary()
print(comp_staff.salary)

print()
# Here where increase the salary by staff request
new_staff = Staff('Goe', 'Philips', 6000)
new_staff_1 = Staff('Maya', 'Alpha', 6500)

print(new_staff.salary)
new_staff.increase_salary()
print(new_staff.salary)
print(new_staff.full_name())