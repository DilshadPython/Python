# very important in every method you create in the class the first arguments self

class Employee:
	def __init__(self, name, pay_rate):
		self.name = name
		self.pay_rate = pay_rate

	def __str__(self):
		return self.name + ', ' + str(self.pay_rate)

	def to_pay(self, hours_work):
		return self.pay_rate * hours_work

class Manager(Employee):
	def __init__(self, name, pay_rate, isSalaried):
		Employee.__init__(self, name, pay_rate)
		self.salaried = isSalaried

	def __str__(self):
		the_empl = Employee.__str__(self)
		the_empl += " salaried: " + str(self.salaried)
		return the_empl

	def to_pay(self, hours_work):
		if self.salaried:
			return self.pay_rate
		else:
			return self.pay_rate * hours_work


empl = Employee('Tom John', 12.50)
print('Employee details: ', empl)
print('The total payment is: ' + str(empl.to_pay(int(input('Enter hours working: ')))))

mng = Manager('Jone Smith',  1350, True)
print('Details: ', mng)

print('Manager gross pay: ' + str(mng.to_pay(int(input('Enter hours work: ')))))

mng1 = Manager('Jone Smith', 17, False)
print('Details: ', mng1)

print('Manager gross pay: ' + str(mng1.to_pay(int(input('Enter hours work: ')))))
