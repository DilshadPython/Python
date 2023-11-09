# Notice: in __str__ we just need self as arg to write 
# self come to each methods ib both class base and drive as first argmument
class Account:
	def __init__(self, account_nr, name, balance):
		self.account_nr = account_nr
		self.balance = balance
		self.name = name

	def __str__(self):
		return "Account Nr: " + str(self.account_nr) + ", Name: " + str(self.name) + \
				", Blanace: " + str(self.balance)

	# The ida is we had deposit function in both drive class in accounts.py
	# we moved to base class and can used for both without repeat again
	def deposit(self, amount):
		self.balance += amount


class Checking(Account):
	def __init__(self, account_nr, balance, name, fee):
		Account.__init__(self, account_nr, balance, name)
		self.fee = fee

	def __str__(self):
		retn_str = "Account type: Checking\t"
		retn_str += Account.__str__(self)
		return retn_str

	def get_fee(self):
		return self.fee

	def withdraw(self, amount):
		if amount > self.balance:
			print('Insufficient funds')
		else:
			self.balance = self.balance - amount - self.fee


class Saving(Account):
	def __init__(self, account_nr, balance, name):
		Account.__init__(self, account_nr, balance, name)

	def __str__(self):
		the_acc = "Account type: Saving\t" + Account.__str__(self)
		return the_acc

	def withdraw(self, amount):
		if amount > self.balance:
			print('Insufficient funds')
		else:
			self.balance = self.balance - amount


check = Checking('2467', 'Tomas', 700, .67)
print('Account Detail', check)

check.withdraw(300)
print('Withdraw:', check)

check.deposit(500)
print('Deposit: ', check)

print('***' * 10)

save = Saving('3232', 'Jack', 700)
print('Saving', save)

save.withdraw(300)
print('Withdraw:', save)

save.deposit(500)
print('Deposit: ', save)

print('###' * 20)
# Now we try to display all in one lis both account Checking and Saving
# create a list

acc_list = [check, save]
print('Display both accounts in account list:')
# now we running throw the list
for x in range(0, len(acc_list)):
	print(acc_list[x])
