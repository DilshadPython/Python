# Notice: in __str__ we just need self as arg to write 
# self come to each methods ib both class base and drive as first argmument
class Account:
	def __init__(self, account_nr, name, balance):
		self.account_nr = account_nr
		self.balance = balance
		self.name = name


	def __str__(self):
		return "Account number: " + str(self.account_nr) + ", Name: " + str(self.name) + \
				", Blanace: " + str(self.balance)


class Checking(Account):
	def __init__(self, account_nr, balance, name, fee):
		Account.__init__(self, account_nr, balance, name)
		self.fee = fee


	def __str__(self):
		# the_acc = "Account type: Checking\t"
		# the_acc += Account.__str__(self)
		# or
		the_acc = "Account type: Checking\t" + Account.__str__(self)
		return the_acc

	def get_fee(self):
		return self.fee

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if amount > self.balance:
			print('Insufficient funds')
		else:
			self.balance = self.balance - amount - self.fee


cal = Checking('2467', 'Tomas', 700, .67)
print('Account Detail', cal)

cal.withdraw(300)
print(cal)

cal.deposit(500)
print(cal)

