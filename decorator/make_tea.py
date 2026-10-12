import time

def make_tea(func):
    def mix_tea(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(f'Tea time: {end_time - start_time}, seconds.')
    return mix_tea


@make_tea
def new_tea(type_tea, time_need):
    print('Start make a new tea to drink.')
    time.sleep(time_need)
    print(f'Tea time: {time_need}, seconds.')

new_tea('Balck Tea', 2)

@make_tea
def match_tea():
    time.sleep(2)
    print(f'Time match')

match_tea()