class Staff:
    number_of_staff = 0
    raise_to_pay = 1.1
    def __init__(self, fname, lname, payment):
        self.fname = fname
        self.lname = lname
        self.payment = payment
        self.mail = fname + '.' + lname + '@mail.com'

        Staff.number_of_staff += 1

    def full_name(self):
        return self.fname + ' ' + self.lname

    def increase_payment(self):
        self.payment = int(self.payment * self.raise_to_pay)

# This is before we instance any user the number of all staff is:
print('\nThis is before we instance any user:', Staff.number_of_staff)
user = Staff('Tom', 'George', 2800)
user_1 = Staff('Jane', 'Tim', 3400)
print('Now we create or instance a users class: ', Staff.number_of_staff)


print(user.full_name())
print(user.mail)
print(user.payment)
# We are make extra payment
user.increase_payment()
print(user.payment)

print()

print(user_1.full_name())
print(user_1.mail)
print(user_1.payment)
user_1.increase_payment()
# After increase the pay
print(user_1.payment)

print()
print(Staff.raise_to_pay)
print(user.raise_to_pay)
print(user_1.raise_to_pay)

print()

# Here we can see the raise_to_pay but in instance obj of the staff we can't see the raise_to_pay
print(Staff.__dict__)
# we can't see the raise_to_pay in instance obj
print(user.__dict__)