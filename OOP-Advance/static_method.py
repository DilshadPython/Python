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

    # This is static methods
    @staticmethod
    def workday_or_weekend(day):
        # workday start from 0 to 6. 5 is saturday and 6 is sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False # 'Weekend'
        return True # (monday to Friday)

new_staff = Staff('John', 'Doe', 4100)
new_staff_1 = Staff('Jack', 'Wall', 3900)


print()
# now we split the fname, lname and salary using class method
staff_1 = 'George-Bill-2750'
staff_2 = 'Julia-smith-3050'

new_staff = Staff.format_string(staff_1)
print(new_staff.full_name())
print(new_staff.show_email())
print(new_staff.salary)

print()
# We use static methods here
import datetime

today_is = datetime.date.today()
print(today_is)

check_day = datetime.date(2023, 5, 15)
print(Staff.workday_or_weekend(check_day))

check_day = datetime.date(2023, 5, 14) # 14/5/2023 is Sunday the results is False
print(Staff.workday_or_weekend(check_day))