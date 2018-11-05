import datetime


current_local_time = datetime.datetime.today()
current_date_time = datetime.datetime.now()
current_date_time_utc = datetime.datetime.utcnow()

print('\n - Return current locale datetime with timezone of None: ', current_local_time)
print('\n - Give us an option passing the timezone: ', current_date_time)
print('\n - This is the timezone where datetime but utc time set to None: ',
      current_date_time_utc)
