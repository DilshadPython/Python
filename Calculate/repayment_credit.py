import datetime
import calendar


## cc balance
balance = 5000
interest_rate = 13 * .02
monthly_payment = 204

today = datetime.date.today()

month = datetime.datetime.now()
print(month.strftime('%B'))

today_of_current_month = calendar.monthrange(today.year, today.month)
print('0 is Monday and 31 is end of the month which is january 2018')
print(today_of_current_month)

today_of_current_month = calendar.monthrange(today.year, today.month)[1]
print(today_of_current_month)

# how_many_days_let_to_end_of_this_month
day_left = today_of_current_month - today.day
print(day_left, ' days left to the end of this month')

print('\n#######################################################################\n')

start_date = today + datetime.timedelta(days=day_left + 1)

print('\nThe next payment will start : ')
print(start_date)

end_date = start_date 


while balance > 0:
	# calculate the interest of one month
	interest_charge = (interest_rate/12) * balance
	balance += interest_charge
	print('\nInterest one month will be: ', balance, '£')

	balance -= monthly_payment
	print('\nSubstract the payment of the balance: ', balance)

	balance = round(balance, 2)
	if balance < 0:
		balance = 0

	# or you can write the above if 3 line in one line
	# balance = 0 if balance < 0 else round(balance, 2)
	print('End date: ',end_date, 'Your balance: ', balance)
	 
	today_of_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
	print('\nEnd date of the next month: ', today_of_current_month)

	end_date = end_date + datetime.timedelta(days=today_of_current_month)
	print('\nEnd of the date: ', end_date)
	# break