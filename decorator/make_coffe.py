import time

def make_coffe(func):
    def mix_coffe(type_coff, time_need):
        print('start time:', time.time())
        start_time = time.time()
        func(type_coff, time_need)
        end_time = time.time()
        print(f'coffe time: {end_time - start_time}, seconds.')
    return mix_coffe


@make_coffe
def new_coffe(type_coff, time_need):
    start_time = time.time()
    time.sleep(time_need)
    end_time = time.time()

new_coffe('Back coffe', 2)