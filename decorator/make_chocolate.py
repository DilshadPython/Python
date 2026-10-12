import time
from datetime import datetime, timedelta

def make_chocolate(func):
    def mix_chocolate(*args, **kwargs):
        start_time = time.time()
        ready = func(*args, **kwargs)
        end_time = time.time()
        print(f'Chocolate time: {end_time - start_time}, seconds.')
        return ready
    return mix_chocolate


@make_chocolate
def new_chocolate(type_chocolate, time_need):
    print(f'Start make a new Chocolate to drink from now {datetime.now()}.')
    time.sleep(time_need)
    print(f'Chocolate time: {time_need}, seconds.')


new_chocolate('Hot Chocolate', 2)

@make_chocolate
def match_time():
    time.sleep(2)
    print(f'Time match')

    # this line tell the function when the function run doesn't wait another 5 minute at the ned return date and time ready
    return f'Chocolate read in exact: {datetime.now() + timedelta(minutes=5)}, say after 5 minutes.'

print(match_time())