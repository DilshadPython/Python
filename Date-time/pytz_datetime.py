import pytz
import datetime


# To run this file use python3 pytz_datetime.py

date_time = datetime.datetime(2017, 10, 21, 19, 18, 56, tzinfo=pytz.UTC)

print('\n\t: ', date_time)

# How it work for now()
date_time_now = datetime.datetime.now(tz=pytz.UTC)
print('\n - For now(): ', date_time_now)

# How it work for utc
date_time_utcnow = datetime.datetime.now(datetime.UTC).replace(tzinfo=pytz.UTC)
print('\n - For UTC now: ', date_time_utcnow)
