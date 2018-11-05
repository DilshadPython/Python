import datetime
import pytz
# To run this file use python3 iso_format_dt.py
# just look at in free time for more idea
# https://pendulum.eustace.io/blog/a-faster-alternative-to-pyz.html

eu_time = datetime.datetime.now(tz=pytz.timezone('Europe/Berlin'))

print(eu_time.isoformat())

print('\n ===============')
print('\n Convert datetime to string style: ', eu_time.strftime('%B %d, %Y'))

print('\n ===============')
date_time_string = 'October 01, 2018'
new_dt_style = datetime.datetime.strptime(date_time_string, '%B %d, %Y')
print('\n Convert string to datetime style: ', new_dt_style)

# strftime  convert Datetime to String AND strptime Convert String to Datetime
