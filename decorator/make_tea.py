import time
from datetime import datetime, timedelta

def make_tea(func):
    def mix_tea(*args):
        start_time = time.time()
        ready = func(*args)
        end_time = time.time()
        print(f'Tea time: {end_time - start_time}, seconds.')
        return ready
    return mix_tea


@make_tea
def new_tea(type_tea, time_need):
    print('Start make a new tea to drink.')
    time.sleep(time_need)
    print(f'Tea time: {time_need}, seconds.')
    # this line tell the function when the function run doesn't wait another 5 minute at the ned return None, not ready
    return f'To make the Tea read need {datetime.now() + timedelta(minutes=5)}'

new_tea('Black Tea', 2)

@make_tea
def match_tea():
    time.sleep(2)
    print(f'Time match')

match_tea()
print(match_tea())