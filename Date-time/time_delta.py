import datetime

# Monday 0 Sunday 6
# Monday 1 Sunday 7
current_date = datetime.date.today()

weekly_date = datetime.timedelta(days=7)

print('\n Next week date is: ', current_date + weekly_date)
print('\n Last week date is: ', current_date - weekly_date)

monthly_date = datetime.timedelta(days=30)
print('\n Next 30 days date is: ', current_date + monthly_date)
print('\n Last 30 days date is: ', current_date - monthly_date)
