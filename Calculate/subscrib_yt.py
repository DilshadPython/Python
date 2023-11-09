import datetime
import math


our_goal = 100000
current_goal = 65000

achive_to_go = our_goal - current_goal

avg_per_day = 40

days_to_go = math.ceil(achive_to_go / avg_per_day)
today = datetime.date.today()

print(today + datetime.timedelta(days=days_to_go))