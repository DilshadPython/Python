days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	''' Check the years if is leap year then return True, if not leap year then False '''
	return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

def days_in_month(year, month):
	''' Return how many days in that month for this year '''
	# The if will check iif the month is between 1-12 
	# if not then there is no month greater than 12
	if not 1 <= month <= 12:
		return 'Invalid month'

	if month == 2 and is_leap(year):
		return 29

	return days[month]

print(is_leap(2015))
print(is_leap(2012))
print(is_leap(2020))
# check_year = input('Please enter any year, example 2031, 1990 etc ... : ')
# a = int(check_year)
# if a:
# 	print(f'\n - {a} is ', is_leap(a))

# check_y = input('Please enter a year example, 2014, etc ... :')
# b = int(check_y)

# check_month = input('Please enter a month between 1-12 :')
# c = input(check_month)
# if b and c:
# 	print(f'\n {b}, {c} is', days_in_month(b, c))
print(days_in_month(2016, 2))
print(days_in_month(2014, 2))
print(days_in_month(2030, 2))