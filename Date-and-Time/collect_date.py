import datetime


current_date = datetime.date.today()

print('\n Today date and time is: ', current_date)

time_delta = datetime.timedelta(days=12)

print('\n\t', current_date - time_delta)

print('\n Important')

print('\n - If we add or subtract date with timedelta we get another date as a result')
# date1 = date2 + timedelta

print('\n - If we add or subtract date with another date we get time delta as a result')
# timedelta = date2 + date1
nawroz = datetime.date(2026, 3, 21)

total_days = nawroz - current_date
print(f'\n We have {total_days} days until new year for Kurdish year!')
# or
print(f'\n Until new year to Kurdish new year we have {total_days.days} remain')
