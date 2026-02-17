class Staff:

    number_of_staff = 0
    increase_pay = 1.06

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
        self.salary = int(self.salary * self.increase_pay)

    # This is class method style using cls
    @classmethod
    def set_increase_pay(cls, money):
        cls.increase_pay = money

    # This is another class method use for split the fname and lname created but split by - line 48, 49
    @classmethod
    def format_string(cls, new_name):
        fname, lname, salary = new_name.split('-')
        return cls(fname, lname, salary)

new_staff = Staff('John', 'Doe', 4100)
new_staff_1 = Staff('Jack', 'Wall', 3900)

# Before use set_increase_pay
print(Staff.increase_pay)
print(new_staff.increase_pay)
print(new_staff_1.increase_pay)

print()
# From here we are using class method, now we increase_pay to 1.09
Staff.set_increase_pay(1.09)
print(Staff.increase_pay)
print(new_staff.increase_pay)
print(new_staff_1.increase_pay)

print()
# now we split the fname, lname and salary using class method
staff_1 = 'George-Bill-2750'
staff_2 = 'Julia-smith-3050'

new_staff = Staff.format_string(staff_1)
print(new_staff.full_name())
print(new_staff.show_email())
print(new_staff.salary)