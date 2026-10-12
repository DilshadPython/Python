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
    print('Start make a new tea {type_tea} to drink.')
    start_time = time.time()
    time.sleep(time_need)
    end_time = time.time()
    print(f'Tea time: {end_time - start_time}, seconds.')

new_tea('Balck Tea', 2)

@make_tea
def match_tea():
    print('Time match')
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    print(f'Time match: {end_time - start_time}')

match_tea()