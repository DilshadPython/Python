import datetime


create_date = datetime.date(2001, 9, 21)
print(create_date)

print('\n=============')
create_curren_date = datetime.date.today()
print(create_curren_date)

print('\n=============')
create_curren_date_1 = datetime.datetime.now()
print(create_curren_date_1)

print('\n========================')
current_date = datetime.datetime.now()

print('\n Full date and time: ', current_date)
print('\n Year: ', current_date.year)
print('\n Month: ', current_date.month)
print('\n Days: ', current_date.day)
print('\n Hour: ', current_date.hour)
print('\n Minutes: ', current_date.minute)
print('\n Seconds: ', current_date.second)
print('\n Weekday: ', current_date.weekday())
print('\n Isoweekday', current_date.isoweekday())

print('\n Weekday means Monday = 0 and Sunday = 6')
print('\n IsoWeekday means Monday = 1 and Sunday = 7')

for day in range(current_date.weekday()):
    print(day)

print('\n####')
for day in range(current_date.isoweekday()):
    print(day)
