import datetime

create_date_time = datetime.datetime(2018, 3, 19, 12, 37, 19, 100000)
print(create_date_time)
print(create_date_time.time())

time_delta = datetime.timedelta(hours=43)

print(f'\n - Now is { create_date_time } go back last 43 hours the time was: ', 
														create_date_time - time_delta)

print(f'\n - Now is { create_date_time } go back next 43 hours the time will be: ', 
														create_date_time + time_delta)