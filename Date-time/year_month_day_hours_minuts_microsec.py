import datetime

create_time = datetime.time(11, 51, 49, 100000)

print('\n\t ', create_time)

print('\n\t Hours', create_time.hour)
print('\n\t Minutes', create_time.minute)
print('\n\t Seconds', create_time.second)

create_date = datetime.date(2021, 7, 17)

print('\n\t Created Date', create_date)
print('\n\t Year ', create_date.year)
print('\n\t Month', create_date.month)
print('\n\t Day', create_date.day)

# create date include year, month, day, hours, minute, and second

all_date = datetime.datetime(2025, 8, 25, 13, 35, 44, 100000)
print('\n\t All Date', all_date)

print('\n\t Date only', all_date.date())
print('\n\t Time Only', all_date.time())

# Three different date and time, what is the difference between this thee date

today_a = datetime.datetime.today()
today_now = datetime.datetime.now()
# today_utcnow = datetime.datetime.utcnow() << before but now >> need update utcnow() change to now(datetime.UTC)
today_utcnow = datetime.datetime.now(datetime.UTC)

print('\n\t Today', today_a) # return the current date time of default which is mean today timzone=None
print('\n\t Today now', today_now) # return the timezone of today timzone=None if now() is empty
print('\n\t Today utcnow', today_utcnow) # this is the date and time zone of the location enter