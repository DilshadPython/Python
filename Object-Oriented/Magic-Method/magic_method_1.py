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

    def __add__(self, more):
        return self.salary + more.salary

    def __len__(self):
        return len(self.full_name())


account_1 = Account('Math', 'George', 60500)
account_2 = Account('Tom', 'Alan', 82500)

print(account_1)

print('\n###################################\n')

print(account_1 + account_2)

print('\n###################################\n')

print(len(account_1), ' length of first account full name')
print(len(account_2), ' length of second account full name')
