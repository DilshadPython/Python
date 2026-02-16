class User:
    pass


first_user = User()
second_user = User()
third_user = User()

print(first_user)
print(second_user)
print(third_user)

first_user.fname = 'Dilshad'
first_user.lname = 'Abdulla'

print()

second_user.fname = 'Jack'
second_user.lname = 'Johnson'

first_user.email = 'dilshad.abdulla' + '@mail.com'
second_user.email = 'jack.johnson' + '@mail.com'
first_user.payment = 3000
second_user.payment = 4000

pay_raise = 1.1
print(pay_raise)
print()

print(first_user.fname, first_user.lname)
print(first_user.email)
print(first_user.payment)
print('Pay rise: ', first_user.payment * pay_raise)

print()

print(second_user.fname, second_user.lname)
print(second_user.email)
print(second_user.payment)
print('Pay rise:', second_user.payment * pay_raise)

