# import regular expression
import re

def sorted_date(date_now):
	# the regular expression make sure the date format should be like YYYY-MM_DD
	if not re.search(r"\d\d\d\d-\d\d-\d\d", date_now):
		raise ValueError('Please enter date in YYYY-MM-DD format.')

	print('The formatted date is {0}'.format(date_now))

sorted_date('2023-02-12')

try:
	print(sorted_date('12/2/2023'))
except ValueError as re:
	print('Sorted date must follow >>', re)
