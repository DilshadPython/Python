class User:
    def __init__(self, fname, lname, payment):
        self.fname = fname
        self.lname = lname
        self.payment = payment
        self.email = fname + '.' + lname + '@mail.com'

    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)

print()

obj_user = User('Dilshad', 'Abdulla', 3300)
print('{} {}'.format(obj_user.fname, obj_user.lname))
print(obj_user.payment)
print(obj_user.email)
print()

obj_user_1 = User('Jo', 'Sam', 3550)
print('{} {}'.format(obj_user_1.fname, obj_user_1.lname))
print(obj_user_1.payment)
print(obj_user_1.email)

print()

obj_user_2 = User('Clear', 'Smith', 3700)
print('{} {}'.format(obj_user_2.fname, obj_user_2.lname))
print(obj_user_2.payment)
print(obj_user_2.email)

print('')


print('\nAfter we created full name method how we call the fname and lname of each users:\n'.upper())

print(obj_user.full_name())
print(obj_user.email)
print()

print(obj_user_1.full_name())
print(obj_user_1.email)
# But if we use the class itself that is what look like
print(User.full_name(obj_user_1))
print()

print(obj_user_2.full_name())
print(obj_user_2.email)
# But if we use the class itself that is what look like
print(User.full_name(obj_user_2))

