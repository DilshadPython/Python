# if tax is 0 - 10000 0%
# if tax is 11000 - 35000 17% 
# if tax is > 36000 27%

def pay_tax(salary):
	if salary <= 10000:
		return 0
	elif salary > 11000 and salary <= 35000:
		return salary * 0.17
	else:
		return salary * 0.27


def neto_pay(grosspay):
	grosspay = grosspay - pay_tax(grosspay)
	return grosspay

salary=int(input('Enter your salary: '))
print('You have to pay ', pay_tax(salary), '£ taxes each year.')
print('Your income after tax is: ', neto_pay)