import datetime
import pytz
# To run this file use python3 country_timezone.py

date_time_utcnow = datetime.datetime.now(tz=pytz.UTC)
print('\n - : ', date_time_utcnow)

date_time_usa = date_time_utcnow.astimezone(pytz.timezone('US/Mountain'))
print('\n - USA: ', date_time_usa)

date_time_paris = date_time_utcnow.astimezone(pytz.timezone('Europe/Paris'))
print('\n - Europe Paris: ', date_time_paris)

for tz in pytz.all_timezones:
	print(tz)