class Staff:

    number_of_staff = 0
    pay_more = 1.06

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.mail = fname + '.' + lname + '@mail.com'

        Staff.number_of_staff += 1

    def full_name(self):
        return self.fname + ' ' + self.lname

    def show_email(self):
        return  self.mail

    def increase_salary(self):
        self.salary = int(self.salary * self.pay_more)

new_staff = Staff('John', 'Doe', 4100)
print(new_staff.full_name())
print(new_staff.show_email())
print(new_staff.salary)
new_staff.increase_salary()
print(new_staff.salary)

print()

new_staff_1 = Staff('Jack', 'Wall', 3900)
print(new_staff_1.full_name())
print(new_staff_1.show_email())
print(new_staff_1.salary)
new_staff_1.increase_salary()
print(new_staff_1.salary)

print()
print(Staff.pay_more)
print(new_staff.pay_more)
print(new_staff_1.pay_more)