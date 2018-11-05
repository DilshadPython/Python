'''
The special method is always suround by double __ like __dilshad__ as an example
double under scawre __ or Dundder __
'''


class Account:

    extra_pay = 1.17

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.email = f_name + '.' + l_name + '@account.com'

    def full_name(self):
        return '{} - {}'.format(self.f_name, self.l_name)

    # def email(self):
    # 	return '{}.{}'.format(self.f_name + self.l_name) +  '@account.com'

    def pay_me(self):
        self.salary = int(self.salary * self.extra_pay)

    '''
	Unimbiguation representaion of an object, used for debugging and login like that
	'''

    def __repr__(self):
        return "Account('{}', '{}', '{}')".format(self.f_name, self.l_name, self.salary)

    '''
	is used for reading and represenation of an object, used as display to the end of user
	'''

    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)


account_1 = Account('Math', 'George', 60500)
account_2 = Account('Tom', 'Alan', 82500)

'''
First print display
<__main__.Account object at 0x7efd32911c18>
###################################
<__main__.Account object at 0x7efd32911c18>
<__main__.Account object at 0x7efd32911c18>
We nee to make it more readable and friendly layout after add __repr__ ,  and __str__
'''
print(account_1)

print('\n###################################\n')

print(repr(account_1), ' <<< __repr__')
print(str(account_1), ' <<< __str__')

print('\n###################################\n')

print(repr(account_2), ' <<< __repr__')
print(str(account_2), ' <<< __str__')

print('\n###################################\n')

print(account_1.__repr__())
print(account_1.__str__())
