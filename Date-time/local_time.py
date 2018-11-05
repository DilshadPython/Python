import datetime
import pytz
# To run this file use python3 plocal_time.py

date_time_utcnow = datetime.datetime.now(tz=pytz.UTC)
print('\n - UTC: ', date_time_utcnow)

date_time_now = datetime.datetime.now()
print(date_time_now)

eu_time = pytz.timezone('Europe/Berlin')
locale_eu_time_now = eu_time.localize(date_time_now)
print('\n - Localize Europe now: ', locale_eu_time_now)

print('###########################################')

uas_time = pytz.timezone('US/Eastern')
local_usa_time = uas_time.localize(date_time_now)
usa_east_time = local_usa_time.astimezone(pytz.timezone('US/Eastern'))

print('\n - Localize East USA now: ', usa_east_time)
